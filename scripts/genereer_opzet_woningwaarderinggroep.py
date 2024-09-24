import locale
import string
from datetime import date
from pathlib import Path

import inquirer  # noqa
from jinja2 import Environment, PackageLoader, select_autoescape

from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)

locale.setlocale(locale.LC_ALL, "nl_NL")

environment = Environment(
    loader=PackageLoader("woningwaardering"),
    autoescape=select_autoescape(),
    keep_trailing_newline=True,
)


def validate_date(answers: dict[str, str], answer: str) -> bool:
    try:
        date.fromisoformat(answer)
        return True
    except (TypeError, ValueError):
        return False


def check_write(file_path: Path) -> bool:
    write_file = False

    if file_path.exists():
        print(f"{file_path} bestaat al.")
        overwrite = inquirer.text(message="Type 'Ja' om te overschrijven")
        if overwrite == "Ja":
            write_file = True
    else:
        write_file = True

    return write_file


questions = [
    inquirer.List(
        "stelsel",
        message="Voor welk stelsel wil je een stelselgroep implementeren?",
        choices=[(stelsel.naam, stelsel.name) for stelsel in Woningwaarderingstelsel],
    ),
    inquirer.Text(
        "begindatum",
        message=lambda answers: f"Vanaf welke datum is het {Woningwaarderingstelsel[answers.get('stelsel')].naam} stelsel geldig?",
        default=date(date.today().year, 7, 1),
        validate=validate_date,
    ),
    inquirer.List(
        "stelselgroep",
        message="Welke stelselgroep wil je implementeren?",
        choices=lambda answers: [
            (stelselgroep.naam, stelselgroep.name)
            for stelselgroep in Woningwaarderingstelselgroep
            if stelselgroep.value.parent is not None
            and stelselgroep.value.parent.code
            == Woningwaarderingstelsel[answers.get("stelsel")].code
        ],
    ),
]

answers = inquirer.prompt(questions)

stelsel = str(answers.get("stelsel"))
begindatum = str(answers.get("begindatum"))
stelselgroep = str(answers.get("stelselgroep"))
woningwaarderingstelsel = Woningwaarderingstelsel[stelsel]
woningwaarderingstelselgroep = Woningwaarderingstelselgroep[stelselgroep]

if woningwaarderingstelselgroep.value.naam is None:
    raise TypeError(f"{woningwaarderingstelselgroep} heeft geen naam")

stelselgroep_class_naam = string.capwords(
    woningwaarderingstelselgroep.name, "_"
).replace("_", "")

stelsels_folder = Path("woningwaardering") / "stelsels"
stelsel_folder = stelsels_folder / stelsel
stelsel_folder.mkdir(parents=True, exist_ok=True)

stelsel_file_path = stelsel_folder / f"{stelsel}.py"

stelsel_class_naam = string.capwords(woningwaarderingstelsel.name, "_").replace("_", "")

stelselgroep_folder = stelsel_folder / stelselgroep
stelselgroep_file_path = stelselgroep_folder / f"{stelselgroep}.py"

if check_write(stelselgroep_file_path):
    stelselgroep_template = environment.get_template(
        "stelsels/stelsel/stelselgroep/stelselgroep.py.j2"
    )

    stelselgroep_result = stelselgroep_template.render(
        className=stelselgroep_class_naam,
        stelsel=woningwaarderingstelsel,
        stelselgroep=woningwaarderingstelselgroep,
        begindatum=begindatum,
    )
    stelselgroep_folder.mkdir(parents=True, exist_ok=True)
    stelselgroep_file_path.write_text(stelselgroep_result)

stelselgroep_directories = [
    f
    for f in stelsel_folder.iterdir()
    if f.is_dir() and f.name in Woningwaarderingstelselgroep.__members__
]

stelselgroepen = sorted(
    [
        (directory.name, string.capwords(directory.name, "_").replace("_", ""))
        for directory in stelselgroep_directories
    ],
    key=lambda d: d[0],
)

stelselgroep_init_template = environment.get_template(
    "stelsels/stelsel/stelselgroep/__init__.py.j2"
)

stelselgroep_init_result = stelselgroep_init_template.render(
    stelselgroep=stelselgroep,
    className=stelselgroep_class_naam,
)

(stelselgroep_folder / "__init__.py").write_text(stelselgroep_init_result)


stelsel_template = environment.get_template("stelsels/stelsel/stelsel.py.j2")
stelsel_result = stelsel_template.render(
    className=stelsel_class_naam,
    stelsel=woningwaarderingstelsel,
    begindatum=begindatum,
    stelselgroepen=stelselgroepen,
)
stelsel_file = stelsel_file_path.write_text(stelsel_result)

huurprijzen_file_path = stelsel_folder / "maximale_huurprijzen.csv"

if check_write(huurprijzen_file_path):
    huurprijzen_template = environment.get_template(
        "stelsels/stelsel/maximale_huurprijzen.csv"
    )
    huurprijzen_result = huurprijzen_template.render()
    huurprijzen_file = huurprijzen_file_path.write_text(huurprijzen_result)

stelsel_init_template = environment.get_template("stelsels/stelsel/__init__.py.j2")

stelsel_init_result = stelsel_init_template.render(stelselgroepen=stelselgroepen)

(stelsel_folder / "__init__.py").write_text(stelsel_init_result)
