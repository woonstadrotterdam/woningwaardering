import csv
import re
from typing import Dict, Set
import unidecode
from jinja2 import Environment
from itertools import groupby
from operator import itemgetter
import os
from zoneinfo import ZoneInfo
import datetime
import requests

output_folder = "woningwaardering/vera/referentiedata"
soort_folder = f"{output_folder}/soort"
current_time = datetime.datetime.now(ZoneInfo("Europe/Amsterdam"))


# url = "https://vera-service.azurewebsites.net/api/referentiedata?Version=latest"
# response = requests.get(url)
# source_data = json.load(loads(response.text)

url = "https://raw.githubusercontent.com/Aedes-datastandaarden/vera-referentiedata/main/Referentiedata.csv"
response = requests.get(url, timeout=10)
source_data = csv.DictReader(response.text.splitlines(), delimiter=";")


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

# Create output directory if not exists
if not os.path.exists(soort_folder):
    os.makedirs(soort_folder)

# group items by 'soort'
grouped_data = [(k, list(g)) for k, g in groupby(active_data, key=itemgetter("soort"))]


environment = Environment(autoescape=True)


def regex_replace(s, find, replace) -> str:
    return re.sub(find, replace, s)


environment.filters["regex_replace"] = regex_replace


def split_long_line(s) -> str:
    return re.sub(r"(.{1,84})(\s|$)", r"\1\n    ", s).rstrip()


environment.filters["split_long_line"] = split_long_line


def remove_accents(s) -> str:
    return unidecode.unidecode(s)


environment.filters["remove_accents"] = remove_accents


def normalize_variable_name(item):
    s = item["naam"]
    if "+" in s:
        s = item["code"]
    s = re.sub(
        r"^\(.*\)", "", s
    )  # remove parenthesized text at the beginning of the string
    s = re.sub(r"[\(|\)]", "", s)  # remove other parentheses
    s = unidecode.unidecode(s)  # remove accents
    s = s.replace("/", " of ")  # replace slashes with 'of'
    s = re.sub(r"[^A-Za-z0-9]", "_", s)  # replace non-alphanumeric characters with _
    s = re.sub(r"_+", "_", s)  # replace multiple underscores with a single underscore
    s = s.strip("_")  # remove leading and trailing underscores
    if s[0].isdigit():
        s = (
            item["soort"] + "_" + s
        )  # add soort prefix if the first character is a digit
    s = s.lower()  # convert to lowercase
    return s


environment.filters["normalize_variable_name"] = normalize_variable_name


# define your Jinja2 template for soort
soort_template = environment.from_string(
    """
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class {{ soort|remove_accents }}:
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
    with open(f"{soort_folder}/{soort}.py", "w") as file:
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
    """
from woningwaardering.vera.referentiedata.soort import (
{%- for soort in soorten %}
    {{ soort }},
{%- endfor %}
)


class {{ domein|remove_accents }}:
{%- for soort in soorten %}
    {{ soort }} = {{ soort }}.{{ soort }}
{% endfor %}
"""
)

# render the domein template with domeinen and soorten
for domein, soorten in domein_to_soorten.items():
    domein_filename = remove_accents(domein).lower()
    rendered_code = domein_template.render(domein=domein, soorten=sorted(soorten))
    with open(f"{output_folder}/{domein_filename}.py", "w") as file:
        file.write(rendered_code)
