import difflib
from collections import Counter
from decimal import Decimal
from pathlib import Path
from typing import Iterator

from pytest import fail

from woningwaardering.rapport import naar_rapport
from woningwaardering.stelsels import utils
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelselgroep,
)


def get_stelselgroep_resultaten(
    resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
    stelselgroep: Woningwaarderingstelselgroep,
) -> list[WoningwaarderingResultatenWoningwaarderingGroep]:
    resultaten = [
        groep
        for groep in resultaat.groepen or []
        if groep.criterium_groep.stelselgroep == stelselgroep
    ]
    assert len(resultaten) < 2, (
        f"Meer dan 1 stelselgroepresultaat gevonden voor {stelselgroep.naam}: {resultaten}"
    )
    assert len(resultaten) == 1, (
        f"Geen stelselgroepresultaat gevonden voor: {stelselgroep.naam}"
    )
    return resultaten


def _gesorteerd_op_criterium_id(
    resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
) -> WoningwaarderingResultatenWoningwaarderingResultaat:
    """Geef een kopie waarin de waarderingen per groep op criterium-id zijn gesorteerd.

    Hiermee wordt de JSON-vergelijking ongevoelig voor de (functioneel irrelevante)
    volgorde van waarderingen binnen een groep.
    """
    gesorteerd = resultaat.model_copy(deep=True)
    for groep in gesorteerd.groepen or []:
        if groep.woningwaarderingen:
            groep.woningwaarderingen.sort(
                key=lambda waardering: (
                    waardering.criterium.id
                    if waardering.criterium and waardering.criterium.id
                    else ""
                )
            )
    return gesorteerd


def assert_output_model(
    resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
    verwacht_resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
    stelselgroep: Woningwaarderingstelselgroep | None = None,
):
    if stelselgroep:
        verwachte_groepen = get_stelselgroep_resultaten(
            verwacht_resultaat, stelselgroep
        )
        verwacht_resultaat = WoningwaarderingResultatenWoningwaarderingResultaat(
            groepen=verwachte_groepen
        )

        groepen = get_stelselgroep_resultaten(resultaat, stelselgroep)
        resultaat = WoningwaarderingResultatenWoningwaarderingResultaat(groepen=groepen)

    assert_unieke_criterium_ids(verwacht_resultaat)
    assert_unieke_criterium_ids(resultaat)

    difflines = list(
        difflib.unified_diff(
            fromfile="verwacht",
            tofile="testresultaat",
            a=naar_rapport(verwacht_resultaat).get_string().split("\n"),
            b=naar_rapport(resultaat).get_string().split("\n"),
            lineterm="",
            n=3,
        )
    )

    colored_diff = "\n".join(kleur_diff(difflines, use_loguru_colors=True))

    if colored_diff != "":
        fail(reason=f"Output komt niet overeen\n{colored_diff}", pytrace=False)

    # De volgorde van waarderingen binnen een groep is functioneel niet relevant
    # (de hiërarchie ligt vast in ``criterium.id`` en ``bovenliggende_criterium``).
    # We sorteren daarom op criterium-id voordat we de JSON vergelijken, zodat de
    # diff aantoont dat enkel de volgorde verschilt en niet de punten/aantallen.
    difflines_json = list(
        difflib.unified_diff(
            fromfile="verwacht",
            tofile="testresultaat",
            a=_gesorteerd_op_criterium_id(verwacht_resultaat)
            .model_dump_json(indent=2, exclude_none=True)
            .split("\n"),
            b=_gesorteerd_op_criterium_id(resultaat)
            .model_dump_json(indent=2, exclude_none=True)
            .split("\n"),
            lineterm="",
            n=3,
        )
    )

    colored_diff_json = "\n".join(kleur_diff(difflines_json, use_loguru_colors=True))

    if colored_diff_json != "":
        fail(
            reason=f"Json output komt niet overeen\n{colored_diff_json}", pytrace=False
        )

    assert_som_bovenliggend_criterium(resultaat)
    assert_punten_afgerond_op_kwarten(resultaat)
    assert_punten_op_twee_decimalen(resultaat)


def kleur_diff(diffresult: list[str], use_loguru_colors: bool = True) -> Iterator[str]:
    green = "\x1b[92m"
    red = "\x1b[91m"
    reset = "\x1b[0m"

    return (
        (green + diff + reset)
        if diff.startswith("+")
        else (red + diff + reset)
        if diff.startswith("-")
        else diff
        for diff in diffresult
    )


def assert_unieke_criterium_ids(
    resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
) -> None:
    """Binnen een stelselgroep heeft elke waardering een criterium met een uniek id."""
    for groep in resultaat.groepen or []:
        criterium_ids = [
            waardering.criterium.id
            for waardering in groep.woningwaarderingen or []
            if waardering.criterium and waardering.criterium.id
        ]
        dubbele_ids = sorted(
            criterium_id
            for criterium_id, aantal in Counter(criterium_ids).items()
            if aantal > 1
        )
        assert not dubbele_ids, (
            f"Criterium-id's komen meer dan één keer voor: {dubbele_ids} "
            f"(groep "
            f"{groep.criterium_groep and groep.criterium_groep.stelselgroep and groep.criterium_groep.stelselgroep.naam})"
        )


def assert_geen_dubbele_aantal_in_hierarchie(
    resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
) -> None:
    """Geen structurele ouder met aantal wanneer onderliggende waarderingen ook aantal hebben."""
    for groep in resultaat.groepen or []:
        waarderingen = groep.woningwaarderingen or []
        parent_ids = utils.parent_ids_met_onderliggende_aantal(waarderingen)
        for waardering in waarderingen:
            if (
                waardering.aantal is None
                or waardering.criterium is None
                or waardering.criterium.id is None
            ):
                continue
            if waardering.criterium.id not in parent_ids:
                continue
            if waardering.punten is not None:
                continue
            assert False, (
                f"Waardering {waardering.criterium.id} heeft aantal terwijl onderliggende "
                f"waarderingen ook aantal hebben "
                f"(groep "
                f"{groep.criterium_groep and groep.criterium_groep.stelselgroep and groep.criterium_groep.stelselgroep.naam})"
            )


def assert_geen_dubbele_punten_in_hierarchie(
    resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
) -> None:
    """Geen ouder met punten wanneer een onderliggende waardering ook punten heeft."""
    for groep in resultaat.groepen or []:
        waarderingen = groep.woningwaarderingen or []
        parent_ids = utils.parent_ids_met_onderliggende_punten(waarderingen)
        for waardering in waarderingen:
            if (
                waardering.punten is None
                or waardering.criterium is None
                or waardering.criterium.id is None
            ):
                continue
            assert waardering.criterium.id not in parent_ids, (
                f"Waardering {waardering.criterium.id} heeft punten terwijl onderliggende "
                f"waarderingen ook punten hebben "
                f"(groep "
                f"{groep.criterium_groep and groep.criterium_groep.stelselgroep and groep.criterium_groep.stelselgroep.naam})"
            )


def assert_groep_punten_is_som_van_waarderingen(
    resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
) -> None:
    """groep.punten is de som van de waarderingen wanneer die punten tonen."""
    for groep in resultaat.groepen or []:
        waarderingen = groep.woningwaarderingen or []
        if groep.punten is None:
            continue
        if not any(w.punten is not None for w in waarderingen):
            continue
        verwacht = utils.som_punten_waarderingen(waarderingen)
        groep_naam = (
            groep.criterium_groep
            and groep.criterium_groep.stelselgroep
            and groep.criterium_groep.stelselgroep.naam
        )
        assert groep.punten == verwacht, (
            f"groep.punten ({groep.punten}) != som van de waarderingen ({verwacht}) "
            f"in {groep_naam}"
        )


def assert_punten_op_twee_decimalen(
    resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
) -> None:
    """De punten van elke waardering staan in de output op ten hoogste twee decimalen.

    Het stelselgroeptotaal wordt apart berekend: de som van de onafgeronde
    builder-punten, afgerond op een kwart punt. De waardering Afronding op
    kwartpunten vangt het verschil tussen dat totaal en de som van de
    afgeronde vastgelegde waarderingen op. Samen met
    assert_groep_punten_is_som_van_waarderingen betekent dit dat de
    puntenkolom van een stelselgroep exact optelt tot het totaal.
    """
    for groep in resultaat.groepen or []:
        for waardering in groep.woningwaarderingen or []:
            if waardering.punten is None:
                continue
            punten = Decimal(str(waardering.punten))
            criterium_naam = waardering.criterium and waardering.criterium.naam
            assert punten == punten.quantize(Decimal("0.01")), (
                f"Waardering '{criterium_naam}' heeft punten {waardering.punten} "
                "met meer dan twee decimalen"
            )


def assert_som_bovenliggend_criterium(
    resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
) -> None:
    assert_geen_dubbele_punten_in_hierarchie(resultaat)
    assert_geen_dubbele_aantal_in_hierarchie(resultaat)
    assert_groep_punten_is_som_van_waarderingen(resultaat)


def assert_punten_afgerond_op_kwarten(
    resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
):
    """
    Controleert of alle punten in het resultaat zijn afgerond op kwarten (0.25).
    """
    for groep in resultaat.groepen or []:
        # Check groepstotaal
        if groep.punten is not None:
            remainder = round((groep.punten % 0.25) * 100) / 100
            assert remainder == 0.0, (
                f"Groep '{groep.criterium_groep.naam}' heeft punten {groep.punten} die niet zijn afgerond op kwarten"
            )


def assert_invarianten_van_groep(
    groep: WoningwaarderingResultatenWoningwaarderingGroep,
) -> None:
    """Controleer de eigenschappen die voor elke gewaardeerde stelselgroep gelden."""
    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat(groepen=[groep])
    assert_unieke_criterium_ids(resultaat)
    assert_som_bovenliggend_criterium(resultaat)
    assert_punten_afgerond_op_kwarten(resultaat)
    assert_punten_op_twee_decimalen(resultaat)


def punten_per_naam(
    groep: WoningwaarderingResultatenWoningwaarderingGroep,
) -> dict[str, float]:
    """Geef de punten van elke waardering met punten, op naam van het criterium."""
    punten: dict[str, float] = {}
    for waardering in groep.woningwaarderingen or []:
        if waardering.punten is None or waardering.criterium is None:
            continue
        naam = waardering.criterium.naam or ""
        assert naam not in punten, (
            f"De naam '{naam}' komt meer dan één keer voor; "
            "punten_per_naam kan deze waarderingen niet onderscheiden."
        )
        punten[naam] = waardering.punten
    return punten


def punten_per_bovenliggende(
    groep: WoningwaarderingResultatenWoningwaarderingGroep,
) -> dict[str | None, dict[str, float]]:
    """Geef de punten per waardering, gegroepeerd op de naam van het bovenliggende criterium.

    Een waardering direct onder de stelselgroep staat onder de sleutel `None`.
    """
    namen = {
        waardering.criterium.id: waardering.criterium.naam
        for waardering in groep.woningwaarderingen or []
        if waardering.criterium is not None
    }
    punten: dict[str | None, dict[str, float]] = {}
    for waardering in groep.woningwaarderingen or []:
        if waardering.punten is None or waardering.criterium is None:
            continue
        bovenliggende = waardering.criterium.bovenliggende_criterium
        groepsnaam = namen[bovenliggende.id] if bovenliggende else None
        naam = waardering.criterium.naam or ""
        onderliggend = punten.setdefault(groepsnaam, {})
        assert naam not in onderliggend, (
            f"De naam '{naam}' komt meer dan één keer voor onder '{groepsnaam}'."
        )
        onderliggend[naam] = waardering.punten
    return punten


def aantal_per_naam(
    groep: WoningwaarderingResultatenWoningwaarderingGroep,
) -> dict[str, float]:
    """Geef het aantal van elke waardering met een aantal, op naam van het criterium.

    Bedoeld voor stelselgroepen waarin een waardering geen eigen punten heeft,
    zoals de oppervlakte van vertrekken: daar is het aantal de oppervlakte in m²
    en staan de punten op de stelselgroep (`groep.punten`).
    """
    aantallen: dict[str, float] = {}
    for waardering in groep.woningwaarderingen or []:
        if waardering.aantal is None or waardering.criterium is None:
            continue
        naam = waardering.criterium.naam or ""
        assert naam not in aantallen, (
            f"De naam '{naam}' komt meer dan één keer voor; "
            "aantal_per_naam kan deze waarderingen niet onderscheiden."
        )
        aantallen[naam] = waardering.aantal
    return aantallen


def aantal_per_bovenliggende(
    groep: WoningwaarderingResultatenWoningwaarderingGroep,
) -> dict[str | None, dict[str, float]]:
    """Geef het aantal per waardering, gegroepeerd op de naam van het bovenliggende criterium.

    Een waardering direct onder de stelselgroep staat onder de sleutel `None`.
    """
    namen = {
        waardering.criterium.id: waardering.criterium.naam
        for waardering in groep.woningwaarderingen or []
        if waardering.criterium is not None
    }
    aantallen: dict[str | None, dict[str, float]] = {}
    for waardering in groep.woningwaarderingen or []:
        if waardering.aantal is None or waardering.criterium is None:
            continue
        bovenliggende = waardering.criterium.bovenliggende_criterium
        groepsnaam = namen[bovenliggende.id] if bovenliggende else None
        naam = waardering.criterium.naam or ""
        onderliggend = aantallen.setdefault(groepsnaam, {})
        assert naam not in onderliggend, (
            f"De naam '{naam}' komt meer dan één keer voor onder '{groepsnaam}'."
        )
        onderliggend[naam] = waardering.aantal
    return aantallen


def opslagpercentage_per_naam(
    groep: WoningwaarderingResultatenWoningwaarderingGroep,
) -> dict[str, float]:
    """Geef het opslagpercentage van elke waardering met een opslag, op naam van het criterium."""
    opslagpercentages: dict[str, float] = {}
    for waardering in groep.woningwaarderingen or []:
        if waardering.opslagpercentage is None or waardering.criterium is None:
            continue
        naam = waardering.criterium.naam or ""
        assert naam not in opslagpercentages, (
            f"De naam '{naam}' komt meer dan één keer voor; "
            "opslagpercentage_per_naam kan deze waarderingen niet onderscheiden."
        )
        opslagpercentages[naam] = waardering.opslagpercentage
    return opslagpercentages


def zolders_met_aftrek(
    groep: WoningwaarderingResultatenWoningwaarderingGroep,
) -> list[str]:
    """Geef de id's van de zolderruimten met een aftrek voor een zolder zonder vaste trap.

    De aftrek staat direct onder de stelselgroep en heet voor elke zolderruimte
    hetzelfde; alleen het criterium-id noemt de zolderruimte.
    """
    achtervoegsel = "__correctie_zolder_zonder_vaste_trap"
    return [
        waardering.criterium.id.removesuffix(achtervoegsel).rsplit("__", 1)[-1]
        for waardering in groep.woningwaarderingen or []
        if waardering.criterium is not None
        and waardering.criterium.id is not None
        and waardering.criterium.id.endswith(achtervoegsel)
    ]


def lees_model(pad: Path) -> tuple[EenhedenEenheid, str]:
    """Geef de eenheid en de beschrijving van een model op stelselniveau.

    De beschrijving staat in een Markdown-bestand met dezelfde naam naast de
    JSON; ze is verplicht, zoals de docstring bij een waarderingstest.
    """
    beschrijving = pad.with_suffix(".md")
    if not beschrijving.exists():
        fail(
            f"{pad.name} heeft geen beschrijving. Beschrijf in {beschrijving.name} "
            "wat het model laat zien.",
            pytrace=False,
        )
    eenheid = EenhedenEenheid.model_validate_json(pad.read_text())
    return eenheid, beschrijving.read_text().strip()
