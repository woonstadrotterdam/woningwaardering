import csv
import os
import re
import shutil
import string
import textwrap
import time
from collections import Counter, defaultdict
from datetime import date, datetime
from itertools import groupby
from operator import itemgetter
from typing import Any, Callable, Match, Pattern

import requests
import tomli
import unidecode
from jinja2 import Environment, select_autoescape
from loguru import logger

os.environ["TZ"] = "Europe/Amsterdam"
time.tzset()

output_folder = os.path.join("woningwaardering", "vera", "referentiedata")

# url = "https://vera-service.azurewebsites.net/api/referentiedata?Version=latest"
# response = requests.get(url)
# source_data = json.load(loads(response.text)

with open("pyproject.toml", "rb") as f:
    pyproject_data = tomli.load(f)

    woningwaardering_data = pyproject_data.get("tool", {}).get("woningwaardering", {})
    version = woningwaardering_data.get("datasources", {}).get("referentiedata", {})

url = f"https://raw.githubusercontent.com/Aedes-datastandaarden/vera-referentiedata/{version}/Referentiedata.csv"
response = requests.get(url, timeout=10)
source_data = csv.DictReader(response.text.splitlines(), delimiter=";")

# Convert all field names to lowercase
source_data.fieldnames = (
    [name.lower() for name in source_data.fieldnames]
    if source_data.fieldnames
    else None
)


filename = "woningwaardering/vera/referentiedata_uitbreiding.csv"
with open(filename, "r", encoding="utf-8") as file:
    uitbreiding_data = csv.DictReader(file.readlines(), delimiter=";")
    uitbreiding_data.fieldnames = (
        [name.lower() for name in uitbreiding_data.fieldnames]
        if uitbreiding_data.fieldnames
        else None
    )

# Filter out items with a past einddatum
active_data = sorted(
    [
        item
        for item in list(source_data) + list(uitbreiding_data)
        if (not item["einddatum"])
        or (datetime.strptime(item["einddatum"], "%d-%m-%Y").date() >= date.today())
    ],
    key=itemgetter("soort"),
)


def resolve_duplicate(
    duplicate_items: list[dict[str | Any, str | Any]],
) -> dict[str | Any, str | Any]:
    print(f"Er zijn {len(duplicate_items)} dezelfde items gevonden:")
    for idx, item in enumerate(duplicate_items):
        print("")
        print(f"{idx + 1}: {item}")
        print("")

    while True:
        try:
            choice = int(
                input("Geef het nummer van het item dat behouden moet blijven: ")
            )
            if 1 <= choice <= len(duplicate_items):
                return duplicate_items[choice - 1]
            else:
                print("Geen geldige keuze. Kies een geldig nummer.")
        except ValueError:
            print("Voer een nummer in.")


# Count the occurrences of each combination of "soort"/"naam" and "soort"/"code"
counts_code = Counter((item["soort"], item["code"]) for item in active_data)
counts_soort_naam = Counter((item["soort"], item["naam"]) for item in active_data)

resolved_parents: dict[str, dict[str | Any, str | Any]] = dict()

# Update the original list by suffixing duplicate names with the corresponding item code
for item in active_data:
    item["variabele"] = item["naam"]

    if counts_code[(item["soort"], item["code"])] > 1:
        duplicates = [
            active_data_item
            for active_data_item in active_data
            if active_data_item["soort"] == item["soort"]
            and active_data_item["code"] == item["code"]
        ]
        if len(duplicates) > 1:
            # Prompt the user to choose one item to keep
            logger.warning(
                f"Dubbele soort/code combinatie: {item['soort']}.{item['code']}"
            )
            chosen_item = resolve_duplicate(duplicates)

            # Remove the unchosen duplicates from the list
            active_data = [
                d for d in active_data if d == chosen_item or d not in duplicates
            ]

    elif counts_soort_naam[(item["soort"], item["naam"])] > 1:
        logger.warning(
            f"Dubbele soort/naam combinatie: {item['soort']}.{item['code']} {item['naam']}"
        )
        logger.info(
            f"Variabele naam \"{item['variabele']}\" wordt vervangen door \"{item['variabele']} {item['code']}\""
        )
        item["variabele"] += " " + item["code"]

    # Resolve parent information if the parent is not None or an empty string
    if item["parent"] is not None and item["parent"] != "":
        resolved_parent = resolved_parents.get(item["parent"])

        if resolved_parent is None:
            parent_soort = item["parent"].split(".")[0]
            parent_code = item["parent"].split(".")[1]

            parents = [
                active_data_item
                for active_data_item in active_data
                if active_data_item["soort"] == parent_soort
                and active_data_item["code"] == parent_code
            ]

            if parents is not None and len(parents) == 1:
                resolved_parent = resolved_parents[item["parent"]] = parents[0]
            else:
                logger.debug(
                    f"{len(parents)} parents gevonden voor {item['parent']}, verwachtte er 1"
                )

        if resolved_parent is not None:
            item["parent"] = resolved_parent

if os.path.exists(output_folder):
    shutil.rmtree(output_folder)

os.makedirs(output_folder)

# Group items by 'soort'
grouped_data = [(k, list(g)) for k, g in groupby(active_data, key=itemgetter("soort"))]

environment = Environment(autoescape=select_autoescape())


def regex_replace(
    s: str, find: str | Pattern[str], replace: str | Callable[[Match[str]], str]
) -> str:
    return re.sub(find, replace, s)


environment.filters["regex_replace"] = regex_replace


def split_long_line(s: str) -> str:
    lines = textwrap.wrap(s, width=84, break_on_hyphens=False, subsequent_indent="    ")
    return "\n".join(lines)


environment.filters["split_long_line"] = split_long_line


def remove_accents(s: str) -> str:
    return unidecode.unidecode(s)


environment.filters["remove_accents"] = remove_accents


def normalize_variable_name(item: dict[str | Any, str | Any]) -> str:
    name = item["variabele"]
    if "+" in item["variabele"]:
        name = item["code"]

    name = re.sub(
        r"^\(.*\)", "", name
    )  # remove parenthesized text at the beginning of the string
    name = re.sub(r"[\(|\)]", "", name)  # remove other parentheses
    name = unidecode.unidecode(name)  # remove accents
    name = name.replace("/", " en of ")  # replace slashes with 'of'
    name = re.sub(
        r"[^A-Za-z0-9]", "_", name
    )  # replace non-alphanumeric characters with _
    name = re.sub(
        r"_+", "_", name
    )  # replace multiple underscores with a single underscore
    name = name.strip("_")  # remove leading and trailing underscores

    if name[0].isdigit():
        name = f"{item['soort']}_{name}"  # add soort prefix if the first character is a digit
    name = name.lower()  # convert to lowercase
    return name


environment.filters["normalize_variable_name"] = normalize_variable_name

# Define the Jinja2 template for soort_folder/<soort>.py
soort_template = environment.from_string(
    """from woningwaardering.vera.bvg.generated import Referentiedata
{%- set parent_classes = items | map(attribute='parent.soort') | unique | select('string') -%}
{%- if parent_classes -%}
{%- for parentClass in parent_classes %}
from woningwaardering.vera.referentiedata.{{ parentClass | remove_accents | lower }} import (
    {{ parentClass | remove_accents | title }},
)
{%- endfor %}
{%- endif %}
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class {{ soort|remove_accents|title }}Referentiedata(Referentiedata):
    pass


class {{ soort|remove_accents|title }}(Referentiedatasoort):
{%- for item in items %}
    {{ item|normalize_variable_name }} = {{ soort|remove_accents|title }}Referentiedata(
        code="{{ item['code'] | safe }}",
        naam="{{ item['naam'] | safe }}",
        {%- if item['parent'] | safe %}
        parent={{item['parent'].soort | remove_accents | title}}.{{item['parent'] | normalize_variable_name}},
        {%- endif %}
    )
    {%- if item['omschrijving'] | safe %}
    \"\"\"
    {{ item['omschrijving']|split_long_line | safe }}
    \"\"\"
    {%- endif %}
{% endfor %}
"""
)

# Render the soort_folder/<soort>.py template with the grouped data and save to separate files
for soort, items in grouped_data:
    rendered_code = soort_template.render(soort=soort, items=items)
    with open(os.path.join(output_folder, f"{soort.lower()}.py"), "w") as file:
        file.write(rendered_code)

# Define the Jinja2 template for soort/__init__.py
soort_folder_init_template = environment.from_string(
    """
{%- for soort in grouped_data -%}
from .{{ soort[0]|remove_accents|lower }} import (
    {{ soort[0]|remove_accents|title }},
    {{ soort[0]|remove_accents|title }}Referentiedata
)
{% endfor %}
__all__ = [
{%- for soort in grouped_data %}
    "{{ soort[0]|remove_accents|title }}",
    "{{ soort[0]|remove_accents|title }}Referentiedata",
{%- endfor %}
]

"""
)

# render the output_folder/__init__.py template with the grouped data
rendered_code = soort_folder_init_template.render(grouped_data=grouped_data)
with open(os.path.join(output_folder, "__init__.py"), "w") as file:
    file.write(rendered_code)


# Create a mapping from domein to soorten
domein_to_soorten = defaultdict(set)  # Use a defaultdict for faster lookup
for item in active_data:
    if not item["informatiedomein"]:
        logger.warning(
            f"\"{item['soort']} {item['naam']}\" heeft geen informatiedomein. Default domein \"Vastgoed\" wordt gebruikt."
        )
        item["informatiedomein"] = "Vastgoed"
    for domein in string.capwords(item["informatiedomein"]).split(", "):
        domein_to_soorten[domein].add(item["soort"])

# Define the Jinja2 template for domein/__init__.py
domein_folder_init_template = environment.from_string(
    """from woningwaardering.vera.referentiedata import (
{%- for soort in soorten %}
    {{ soort|title }},
{%- endfor %}
)

__all__ = [
{%- for soort in soorten %}
    "{{ soort|title }}",
{%- endfor %}
]

"""
)

# Render the domein/__init__.py template with domeinen and soorten
for domein, soorten in domein_to_soorten.items():
    domein_name = remove_accents(domein).lower()
    rendered_code = domein_folder_init_template.render(
        domein=domein, soorten=sorted(soorten)
    )

    domein_folder = os.path.join(output_folder, domein_name)
    if not os.path.exists(domein_folder):
        os.makedirs(domein_folder)
    with open(os.path.join(domein_folder, "__init__.py"), "w") as file:
        file.write(rendered_code)


# Update README.md with the new version
readme_path = "README.md"

if os.path.exists(readme_path):
    with open(readme_path, "r") as readme_file:
        readme_content = readme_file.read()

    # Update the version using regex
    updated_content = re.sub(
        r"(\[referentiedata )v[\d\.]+(\])", f"\\1{version}\\2", readme_content
    )

    with open(readme_path, "w") as readme_file:
        readme_file.write(updated_content)
