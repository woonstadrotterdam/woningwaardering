# Testing

De tests draaien met [pytest](https://docs.pytest.org/). Installatie en de pre-commit-checks staan onder [Project opzetten](index.md#project-opzetten) en [Tests en checks](index.md#tests-en-checks).

```bash
uv run python -m pytest
```

## Uitgangspunt

Een wijziging in het rapport of de output-JSON van een woningwaardering gebeurt altijd bewust én intentioneel. Daarom vergelijkt `pytest` de output met de verwachte output, maar schrijft hij die nooit. Alleen `task genereer-test-output` werkt de verwachte output bij, en een reviewer beoordeelt de wijziging in de diff van de pull request. Wanneer je die opdracht gebruikt, staat in `AGENTS.md` onder "Verwachte output"; die afspraken gelden voor agents en voor ontwikkelaars.

## Welke test schrijf je?

| Wat je test | Wat je schrijft |
| --- | --- |
| Een beleidsregel binnen één stelselgroep, ook als ze het puntentotaal van andere rubrieken nodig heeft | Een [waarderingstest](#een-waarderingstest-schrijven) |
| Een beleidsregel die over meer dan één stelselgroep gaat | Een [model op stelselniveau](#model-op-stelselniveau) |
| Een functie die op zichzelf staat | Een unittest |

Een waarderingstest waardeert een stelselgroep, controleert de punten die de beleidsregel toekent en vergelijkt de uitkomst met een testreferentie. Een unittest roept een functie rechtstreeks aan en heeft geen testreferentie, zoals `tests/stelsels/utils/test_rond_af_op_kwart.py`. Hij is bedoeld voor een functie waarvan de uitkomst volgt uit haar argumenten, zoals `rond_af_op_kwart` en `classificeer_ruimte`.

Een privéfunctie van een stelselgroep test je via een waarderingstest: die blijft geldig wanneer de functie wordt herschreven. Test een privéfunctie alleen rechtstreeks wanneer het scenario via de stelselgroep onevenredig veel input vraagt, zoals de grensgevallen van `_cap_punten` van de stelselgroep punten voor de WOZ-waarde, waarvoor je de punten van alle andere stelselgroepen precies zou moeten sturen.

### Model op stelselniveau

Een model onder `tests/data/<stelsel>/input/` wordt door het hele stelsel gewaardeerd en per stelselgroep vergeleken met de verwachte output in `output/`. Kies het voor een beleidsregel die over meer dan één stelselgroep gaat. Een laadpaal op een parkeerplek komt bijvoorbeeld in rubriek 10 óf in rubriek 12 terecht; dat een plek niet in beide punten krijgt, is alleen zichtbaar wanneer beide rubrieken in dezelfde uitkomst staan. Zie `tests/data/zelfstandige_woonruimten/input/parkeerruimten_en_laadpalen.json`.

Reken de verwachte output van een nieuw model met de hand na, zoals in stap 1 van een waarderingstest. Een model op stelselniveau moet zonder waarschuwing te waarderen zijn. Een scenario dat een `UserWarning` oproept, hoort daarom in een waarderingstest.

## Een waarderingstest schrijven

De stappen:

1. Zoek de beleidsregel op in de bron en bereken zelf hoeveel punten het scenario oplevert, zonder de bestaande code te gebruiken. Zo controleert de test de beleidsregel en niet de code.
2. Schrijf de test. De onderdelen hieronder beschrijven hoe.
3. Draai `pytest`. De nieuwe test faalt met de melding `Geen testreferentie`; alle andere tests slagen. Faalt er meer, los dat dan eerst op: de volgende stap overschrijft alle verwachte output.
4. Draai `task genereer-test-output`. Die schrijft de testreferentie van de test: een Markdown-bestand in `testreferenties/` naast de testmodule, met de docstring, het rapport, de waarschuwingen, de input en de output-JSON. Controleer in de diff dat alleen die testreferentie erbij is gekomen, en lees het rapport erin na: het moet overeenkomen met wat je in stap 1 hebt berekend.
5. Draai `pytest` en de pre-commit hooks.

Hernoem of verwijder je een test, verwijder dan zelf zijn oude testreferentie: het bijwerken verwijdert geen bestanden.

Een volledige test ziet er zo uit:

```python
def test_meerdere_kastruimtes_tellen_samen_als_een(
    sanitair, vergelijk_met_testreferentie
):
    """Meerdere kastruimtes in een badkamer krijgen samen 0,75 punt.

    Bron: wettekst, Bijlage I onder A, onderdeel 6.2: "Kastruimte (minimale
    breedte van 40 cm, en minimale hoogte van 40 cm) 0,75 punt (tot een maximum
    van 0,75)".
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.badkamer,
                Installatiesoort.bad,
                Installatiesoort.wastafel,
                Installatiesoort.kastruimte,
                Installatiesoort.kastruimte,
            )
        ]
    )

    groep = sanitair.waardeer(eenheid)

    punten = punten_per_naam(groep)
    assert punten[Installatiesoort.kastruimte.naam] == 1.5
    assert punten["Max 0.75 punten voor Kastruimte"] == -0.75
    assert groep.punten == 7.75
    vergelijk_met_testreferentie(eenheid, groep)
```

### Bestand

De tests van een stelselgroep staan in `tests/stelsels/<stelsel>/<stelselgroep>/`, in `test_<stelselgroep>_zel.py` of `test_<stelselgroep>_onz.py`. Het achtervoegsel is nodig omdat `pytest` geen twee testbestanden met dezelfde naam accepteert.

### Eén beleidsregel per test

Een test controleert één beleidsregel, of één keuze van de package, zoals een waarschuwing bij onvolledige input. Je toetst dat aan de eerste zin van de docstring: die zegt in één bewering wat de test controleert. Heb je daar "en" voor nodig, schrijf dan twee tests. Zo belooft de naam van de test precies wat de asserts controleren.

Een tabel uit één onderdeel van de bron, zoals de punten per aanrechtlengte in onderdeel 5.1 van de wettekst, is één beleidsregel. De eerste zin van de docstring noemt dan wat de tabel bepaalt, bijvoorbeeld "De punten voor een aanrecht hangen af van zijn lengte", en de asserts tonen de grenzen.

### Naam

De naam beschrijft het gedrag in gewone taal: `test_meerdere_kastruimtes_tellen_samen_als_een`. De stelselgroep staat al in het pad en hoeft niet in de naam. De naam wordt de bestandsnaam en de kop van de testreferentie, en is daarmee het eerste wat een reviewer in de pull request leest.

### Docstring

De docstring is verplicht en bestaat uit twee delen:

1. De beleidsregel in één zin. In de testreferentie staat die zin direct onder de kop. Hij moet zonder de rest te lezen zeggen wat de test controleert.
2. De bron, met een letterlijk citaat en de vindplaats. Gebruik de bron die de beleidsregel draagt, in de volgorde van autoriteit uit `CONTEXT.md`: wettekst, online beleidsboek, implementatietoelichting. Bewaakt de test een keuze van de package, dan is de bron de toelichting waarin die keuze staat.

De asserts laten zien hoe de beleidsregel uitpakt; de docstring bevat geen berekening.

### Input

Bouw de input op met de functies uit `tests/input.py`, zoals `ruimte(...)`, `element(...)` en `aanrecht(...)`. Wat de beleidsregel raakt, geef je in de test mee; de rest krijgt een standaardwaarde in de functie. Heeft een eenheid meer ruimten van dezelfde detailsoort, nummer ze dan met `naam` (`Badkamer1`, `Badkamer2`). Heeft de beleidsregel het puntentotaal van andere rubrieken nodig, gebruik dan een volledige woning uit `tests/input.py`, zoals `meergezinswoning_van_71_m2(...)`, en geef ook daar mee wat de beleidsregel raakt.

Ontbreekt er een functie voor wat je nodig hebt, voeg hem dan toe aan `tests/input.py`. Een functie hoort daar als ze velden afleidt of een standaardwaarde geeft die de beleidsregel niet raakt. Geeft ze alleen haar argumenten door, gebruik dan het VERA-model zelf, zoals `EenhedenEnergieprestatie(...)`.

Fixtures zijn bedoeld voor context en niet voor scenario's: de stelselgroep (`sanitair`), de `peildatum` en `vergelijk_met_testreferentie`. Een scenario dat in een fixture staat, is in de test niet meer te lezen.

### Asserts

Assert de waarderingen die de beleidsregel raakt, plus het totaal (`groep.punten`); de overige waarderingen staan in de testreferentie. In het voorbeeld hierboven horen het bad en de wastafel bij het scenario, maar de beleidsregel gaat over de kastruimte.

Gebruik de helpers uit `tests/utils.py`: `punten_per_naam(groep)`, of `punten_per_bovenliggende(groep)` wanneer dezelfde naam in meer dan één ruimte voorkomt. Raakt de beleidsregel elke waardering in het scenario, vergelijk dan de hele uitkomst; het totaal heeft dan geen eigen assert nodig:

```python
assert punten_per_naam(groep) == {Installatiesoort.bad_en_douche.naam: 7.0}
```

In een stelselgroep waarin een waardering geen eigen punten heeft, zoals de oppervlakte van vertrekken, assert je het aantal (daar de oppervlakte in m²) met `aantal_per_naam` of `aantal_per_bovenliggende`. Het totaal staat dan op de stelselgroep en krijgt een eigen assert:

```python
assert aantal_per_naam(groep) == {"Slaapkamer2": 4.0}
assert groep.punten == 4.0
```

Schrijf de naam van een waardering zoals je de input schrijft. Is het de naam van een referentiedata-object, gebruik dan dat object: `Installatiesoort.kastruimte.naam`, niet `"Kastruimte"`. Een naam die de package zelf samenstelt, zoals `"Max 0.75 punten voor Kastruimte"`, of die je in de test zelf als tekst meegeeft, zoals `"Badkamer1"`, schrijf je als tekst, zoals hij in het rapport staat.

Sluit de test af met `vergelijk_met_testreferentie(eenheid, groep)`. Wat die controleert, staat in zijn docstring in `tests/conftest.py`.

### Waarschuwingen

Roept een scenario een `UserWarning` op, vang die dan op met `pytest.warns` en geef de opgevangen waarschuwingen als derde argument mee aan `vergelijk_met_testreferentie`. Alleen meegegeven waarschuwingen komen in de testreferentie.

```python
with pytest.warns(UserWarning, match="wastafel") as waarschuwingen:
    groep = sanitair.waardeer(eenheid)

assert punten_per_naam(groep) == {}
vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)
```

### Meerdere gevallen in één test

Verschillen de gevallen van een beleidsregel alleen in wat er in een ruimte staat, zet ze dan samen in één test. Geef elk geval een eigen, genummerde ruimte en vergelijk de hele uitkomst met `punten_per_bovenliggende`. Zo staan alle gevallen naast elkaar in één rapport. Dit kan alleen wanneer de ruimten elkaars waardering niet beïnvloeden.

```python
eenheid = EenhedenEenheid(
    ruimten=[
        ruimte(Ruimtedetailsoort.badkamer, Installatiesoort.douche, naam="Badkamer1"),
        ruimte(Ruimtedetailsoort.badkamer, Installatiesoort.bad, naam="Badkamer2"),
        ruimte(
            Ruimtedetailsoort.badkamer, Installatiesoort.bad_en_douche, naam="Badkamer3"
        ),
    ]
)

groep = sanitair.waardeer(eenheid)

assert punten_per_bovenliggende(groep) == {
    "Badkamer1": {Installatiesoort.douche.naam: 4.0},
    "Badkamer2": {Installatiesoort.bad.naam: 6.0},
    "Badkamer3": {Installatiesoort.bad_en_douche.naam: 7.0},
}
```

### Parametriseren

Parametriseer wanneer de gevallen niet samen in één eenheid passen, of wanneer een geval een eigen toelichting nodig heeft. Bij een geparametriseerde test delen alle gevallen dezelfde docstring. Kies daarom per geval een van drie treden:

1. **Tabel.** De gedeelde docstring en de id verklaren het geval volledig: dezelfde beleidsregel met een ander getal.
2. **Tabel met toelichting.** Het geval hoort bij dezelfde beleidsregel, maar heeft één zin uitleg nodig, bijvoorbeeld een grenswaarde. Geef die mee met `pytest.mark.toelichting`; de zin komt in de testreferentie.
3. **Eigen test.** Het geval heeft een eigen reden of bron, of is een uitzondering op de beleidsregel. Kies bij twijfel deze trede.

```python
@pytest.mark.parametrize(
    ("aanrecht_mm", "verwachte_punten"),
    [
        pytest.param(
            999, {"Wastafel (spoelbak in aanrecht < 1m)": 1.0}, id="net_onder_1m"
        ),
        pytest.param(
            1000,
            {},
            id="precies_1m",
            marks=pytest.mark.toelichting(
                "de keuken heeft een aanrecht van minimaal 1 meter, dus de "
                "spoelbak hoort bij de keuken en is geen wastafel"
            ),
        ),
    ],
)
def test_spoelbak_in_aanrecht_korter_dan_1m_telt_als_wastafel(
    sanitair, vergelijk_met_testreferentie, aanrecht_mm, verwachte_punten
):
    """Een spoelbak in een aanrecht korter dan 1 meter telt als wastafel.

    Bron: beleidsboek zelfstandige woonruimten, 2.6.1: niet als wastafel wordt
    gewaardeerd "een spoelbak in het keukenaanrecht, tenzij deze onderdeel
    uitmaakt van een keukenaanrecht dat korter is dan één meter".
    """
    eenheid = EenhedenEenheid(
        ruimten=[ruimte(Ruimtedetailsoort.keuken, elementen=[aanrecht(aanrecht_mm)])]
    )

    groep = sanitair.waardeer(eenheid)

    assert punten_per_naam(groep) == verwachte_punten
    vergelijk_met_testreferentie(eenheid, groep)
```

Geef elk geval een id met `pytest.param(..., id="...")`, als letterlijke tekst. De id noemt de situatie (`precies_1m`), niet de uitkomst; de verwachting staat in de kolom ernaast.

## Testreferenties beoordelen in een pull request

De wijzigingen onder `**/testreferenties/**` zijn het overzicht van wat een pull request aan de output verandert. Elk bestand begint met de naam van de test, de beleidsregel en de bron, zodat de diff zelf zegt welke beleidsregel geraakt is. Beoordeel bij elke gewijzigde testreferentie of de wijziging de bedoeling is, en of de input, de output of beide zijn gewijzigd. De input staat erin omdat de functies uit `tests/input.py` velden invullen die niet in de test staan, zoals de id en de oppervlakte van een ruimte; verandert zo'n functie, dan zie je dat hier per test.
