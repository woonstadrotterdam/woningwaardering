from collections import Counter
import csv
import re
from typing import Any, Callable, Dict, Set, Pattern, Match
import unidecode
from jinja2 import Environment
from itertools import groupby
from operator import itemgetter
import os
from zoneinfo import ZoneInfo
import datetime
import requests

output_folder = "woningwaardering/vera/referentiedata"
soort_folder = os.path.join(output_folder, "soort")
current_time = datetime.datetime.now(ZoneInfo("Europe/Amsterdam"))


# url = "https://vera-service.azurewebsites.net/api/referentiedata?Version=latest"
# response = requests.get(url)
# source_data = json.load(loads(response.text)

url = "https://raw.githubusercontent.com/Aedes-datastandaarden/vera-referentiedata/main/Referentiedata.csv"
response = requests.get(url, timeout=10)
source_data = csv.DictReader(response.text.splitlines(), delimiter=";")

# Convert all field names to lowercase
source_data.fieldnames = (
    [name.lower() for name in source_data.fieldnames]
    if source_data.fieldnames
    else None
)

# Filter out items with a past einddatum
active_data = [
    item
    for item in source_data
    if (not item["einddatum"])
    or (
        datetime.datetime.strptime(item["einddatum"], "%d-%m-%Y").date()
        >= current_time.date()
    )
]

# Count the occurrences of each combination of "soort" and "naam"
counts = Counter((item["soort"], item["naam"]) for item in active_data)

# Update the original list by suffixing duplicate names with the corresponding item code
for item in active_data:
    item["variabele"] = item["naam"]
    if counts[(item["soort"], item["naam"])] > 1:
        print(item["soort"] + "." + item["code"])
        item["variabele"] += "_" + item["code"]

# Create output directory if not exists
if not os.path.exists(soort_folder):
    os.makedirs(soort_folder)

# group items by 'soort'
grouped_data = [(k, list(g)) for k, g in groupby(active_data, key=itemgetter("soort"))]

environment = Environment(autoescape=True)


def regex_replace(
    s: str, find: str | Pattern[str], replace: str | Callable[[Match[str]], str]
) -> str:
    return re.sub(find, replace, s)


environment.filters["regex_replace"] = regex_replace


def split_long_line(s: str) -> str:
    return re.sub(r"(.{1,84})(\s|$)", r"\1\n    ", s).rstrip()


environment.filters["split_long_line"] = split_long_line


def remove_accents(s: str) -> str:
    return unidecode.unidecode(s)


environment.filters["remove_accents"] = remove_accents


def normalize_variable_name(item: dict[str | Any, str | Any]) -> str:
    s = item["variabele"]
    if "+" in item["variabele"]:
        s = item["code"]

    s = re.sub(
        r"^\(.*\)", "", s
    )  # remove parenthesized text at the beginning of the string
    s = re.sub(r"[\(|\)]", "", s)  # remove other parentheses
    s = unidecode.unidecode(s)  # remove accents
    s = s.replace("/", " en of ")  # replace slashes with 'of'
    s = re.sub(r"[^A-Za-z0-9]", "_", s)  # replace non-alphanumeric characters with _
    s = re.sub(r"_+", "_", s)  # replace multiple underscores with a single underscore
    s = s.strip("_")  # remove leading and trailing underscores

    if s[0].isdigit():
        s = f"{item['soort']}_{s}"  # add soort prefix if the first character is a digit
    s = s.lower()  # convert to lowercase
    return s


environment.filters["normalize_variable_name"] = normalize_variable_name

# define your Jinja2 template for soort
soort_template = environment.from_string(
    # """from vera.bvg.models import Referentiedata
    # """from vera.bvg.generated import Referentiedata
    """from vera.referentiedata.models import Referentiedata


class {{ soort|remove_accents|title }}:
{%- for item in items %}
    {{ item|normalize_variable_name }} = Referentiedata(
        code="{{ item['code'] }}",
        naam="{{ item['naam'] }}",
    )
    {%- if item['omschrijving'] %}
    \"\"\"
    {{ item['omschrijving']|split_long_line }}
    \"\"\"
    {%- endif %}
{% endfor %}
"""
)

# render the soort template with your grouped data and save to separate files
for soort, items in grouped_data:
    rendered_code = soort_template.render(soort=soort, items=items)
    with open(os.path.join(soort_folder, f"{soort.lower()}.py"), "w") as file:
        file.write(rendered_code)

# define your Jinja2 template for soort/__init__.py
soort_init_template = environment.from_string(
    """{%- for soort in grouped_data %}
from .{{ soort[0]|remove_accents|lower }} import {{ soort[0]|remove_accents|title }}
{%- endfor %}


__all__ = [
{%- for soort in grouped_data %}
    "{{ soort[0]|remove_accents|title }}",
{%- endfor %}
]

"""
)

# render the soort template with your grouped data
rendered_code = soort_init_template.render(grouped_data=grouped_data)
with open(os.path.join(soort_folder, "__init__.py"), "w") as file:
    file.write(rendered_code)


# define your Jinja2 template for __init__.py
soort_init_template = environment.from_string(
    """from .soort import (
{%- for soort in grouped_data %}
    {{ soort[0]|remove_accents|title }},
{%- endfor %}
)


__all__ = [
{%- for soort in grouped_data %}
    "{{ soort[0]|remove_accents|title }}",
{%- endfor %}
]

"""
)

# render the soort template with your grouped data
rendered_code = soort_init_template.render(grouped_data=grouped_data)
with open(os.path.join(output_folder, "__init__.py"), "w") as file:
    file.write(rendered_code)


# create a mapping from domein to soorten
domein_to_soorten: Dict[str, Set[str]] = {}
for item in active_data:
    domeinen = item["informatiedomein"].split(", ")
    for domein in domeinen:
        if domein not in domein_to_soorten:
            domein_to_soorten[domein] = set()
        domein_to_soorten[domein].add(item["soort"])

# define your Jinja2 template for domein
domein_template = environment.from_string(
    """from woningwaardering.vera.referentiedata.soort import (
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

# render the domein template with domeinen and soorten
for domein, soorten in domein_to_soorten.items():
    domein_name = remove_accents(domein).lower()
    rendered_code = domein_template.render(domein=domein, soorten=sorted(soorten))

    domein_folder = os.path.join(output_folder, domein_name)
    if not os.path.exists(domein_folder):
        os.makedirs(domein_folder)
    with open(os.path.join(domein_folder, "__init__.py"), "w") as file:
        file.write(rendered_code)
