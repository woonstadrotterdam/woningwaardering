# Testing

De tests draaien met [pytest](https://docs.pytest.org/).

## Uitgangspunt

Een wijziging in het rapport of de output-JSON van een woningwaardering gebeurt altijd bewust én intentioneel.

De testopzet dient dat uitgangspunt op drie manieren:

- `pytest` vergelijkt de output met de verwachte output, maar schrijft die nooit. Elke waarderingstest heeft een testreferentie, een bestand met zijn rapport en output-JSON, en dat bestand verandert alleen door een aparte opdracht: `task genereer-test-output`.
- `AGENTS.md` bepaalt wanneer een agent die opdracht mag gebruiken en wat hij daarover meldt.
- De bijgewerkte verwachte output staat in de diff van de pull request, waar een reviewer hem beoordeelt.

## Tests uitvoeren

Zorg dat de dev dependencies geïnstalleerd zijn (zie [Project opzetten](index.md#project-opzetten)), en run:

```bash
uv run python -m pytest
```

Met geactiveerde `.venv` mag je ook `python -m pytest` gebruiken. Coverage wordt automatisch meegenomen via de pytest-configuratie in `pyproject.toml`.

Na wijzigingen in code of tests draai je ook de pre-commit hooks (dezelfde set als CI); zie [Tests en checks](index.md#tests-en-checks).

## Twee soorten tests

Nieuwe of gewijzigde code lever je op met passende tests. Er zijn twee soorten:

| | Waarderingtest | Functietest |
| --- | --- | --- |
| Vraag | Kent de stelselgroep de punten toe die de beleidsregel voorschrijft? | Doet deze functie wat hij belooft? |
| Roept aan | een stelselgroep: `Sanitair(...).waardeer(eenheid)` | de functie zelf |
| Testreferentie | altijd | nooit |
| Voorbeeld | `tests/stelsels/zelfstandige_woonruimten/sanitair/test_sanitair.py` | `tests/stelsels/utils/test_rond_af_op_kwart.py` |

Een beleidsregel test je met een waarderingstest: de test waardeert een stelselgroep en controleert de punten die de beleidsregel toekent.

Een functietest is bedoeld voor een functie die op zichzelf staat: wat hij teruggeeft volgt uit zijn argumenten, zonder dat je een stelselgroep hoeft te waarderen. Voorbeelden zijn `rond_af_op_kwart` en `classificeer_ruimte`.

Een privéfunctie van een stelselgroep test je via een waarderingstest: die blijft geldig wanneer de functie wordt herschreven, en vergelijkt de output met een testreferentie. Test een privéfunctie alleen rechtstreeks wanneer het scenario via de stelselgroep onevenredig veel input vraagt. `_cap_punten` van de stelselgroep punten voor de WOZ-waarde is zo'n geval: de uitkomst hangt af van de punten van alle andere stelselgroepen.

### Welke test schrijf je?

Nog niet elke stelselgroep is omgezet naar waarderingstests. Een omgezette stelselgroep herken je aan de map `testreferenties/` naast de testmodule; op dit moment is dat alleen sanitair voor zelfstandige woonruimten. De overige stelselgroepen gebruiken [JSON-modellen](#json-modellen).

| Wat je test | Wat je schrijft |
| --- | --- |
| Een beleidsregel binnen één stelselgroep die is omgezet | Een [waarderingstest](#een-waarderingstest-schrijven) |
| Een beleidsregel binnen één stelselgroep die nog niet is omgezet | Een JSON-model in de map van de stelselgroep; zie [JSON-modellen](#model-op-stelselniveau-of-test-op-de-stelselgroep) |
| Een beleidsregel die over meer dan één stelselgroep gaat | Een JSON-model op stelselniveau; zie [JSON-modellen](#model-op-stelselniveau-of-test-op-de-stelselgroep) |
| Een functie die op zichzelf staat | Een [functietest](#een-functietest-schrijven) |

## Een waarderingstest schrijven

De stappen:

1. Zoek de beleidsregel op in de bron en bereken zelf hoeveel punten het scenario oplevert, zonder de bestaande code te gebruiken.
2. Schrijf de test. De onderdelen hieronder beschrijven hoe.
3. Draai `pytest`. De nieuwe test faalt met de melding `Geen testreferentie`; alle andere tests slagen. Faalt er meer, los dat dan eerst op: de volgende stap overschrijft alle verwachte output.
4. Draai `task genereer-test-output` en controleer in de diff dat alleen de testreferentie van de nieuwe test erbij is gekomen. Lees het rapport in dat bestand na: het moet overeenkomen met wat je in stap 1 hebt berekend.
5. Draai `pytest` en de pre-commit hooks.

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
            badkamer(
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

### Eén beleidsregel per test

Een test controleert één beleidsregel, of één keuze van de package, zoals een waarschuwing bij onvolledige input. Je toetst dat aan de eerste zin van de docstring: die zegt in één bewering wat de test controleert. Heb je daar "en" voor nodig, schrijf dan twee tests. Zo belooft de naam van de test precies wat de asserts controleren.

### Naam

De naam beschrijft het gedrag in gewone taal: `test_meerdere_kastruimtes_tellen_samen_als_een`, niet `test_Sanitair_kastruimte`. De naam wordt de bestandsnaam en de kop van de testreferentie, en is daarmee het eerste wat een reviewer in de pull request leest. De stelselgroep staat al in het pad en hoeft niet in de naam.

### Docstring

De docstring is verplicht en bestaat uit twee delen:

1. De beleidsregel in één zin. In de testreferentie staat die zin direct onder de kop. Hij moet zonder de rest te lezen zeggen wat de test controleert.
2. De bron, met een letterlijk citaat en de vindplaats. Gebruik de bron die de beleidsregel draagt, in de volgorde van autoriteit uit `CONTEXT.md`: wettekst, online beleidsboek, implementatietoelichting. Bewaakt de test een keuze van de package, dan is de bron de toelichting waarin die keuze staat.

Een berekening hoort niet in de docstring. De asserts laten zien hoe de beleidsregel uitpakt.

### Input

Bouw de input op met de functies uit `tests/input.py`, zoals `ruimte(...)`, `badkamer(...)` en `aanrecht(...)`. Wat de beleidsregel raakt, geef je in de test mee; de rest krijgt een standaardwaarde in de functie. Heeft een eenheid meer ruimten van dezelfde detailsoort, nummer ze dan met `naam` (`Badkamer1`, `Badkamer2`). Ontbreekt er een functie voor wat je nodig hebt, voeg hem dan toe aan `tests/input.py`.

Fixtures zijn bedoeld voor context en niet voor scenario's: de stelselgroep (`sanitair`), de `peildatum` en `vergelijk_met_testreferentie`. Een scenario dat in een fixture staat, is in de test niet meer te lezen.

### Asserts

Assert de waarderingen die de beleidsregel raakt, plus het totaal (`groep.punten`). De overige waarderingen vind je terug in de testreferentie. In het voorbeeld hierboven staan het bad en de wastafel niet in de asserts: ze horen bij het scenario, maar de beleidsregel gaat over de kastruimte.

`punten_per_naam(groep)` geeft de punten van elke waardering met punten, op naam van het criterium. Komt dezelfde naam in meer dan één ruimte voor, gebruik dan `punten_per_bovenliggende(groep)`: die groepeert de punten op de naam van het bovenliggende criterium. Raakt de beleidsregel elke waardering in het scenario, vergelijk dan de hele uitkomst. Het totaal volgt dan uit die waarderingen en heeft geen eigen assert nodig:

```python
assert punten_per_naam(groep) == {Installatiesoort.bad_en_douche.naam: 7.0}
```

Schrijf de naam van een waardering zoals je de input schrijft. Is het de naam van een referentiedata-object, gebruik dan dat object: `Installatiesoort.kastruimte.naam`, niet `"Kastruimte"`. Een naam die de package zelf samenstelt, zoals `"Max 0.75 punten voor Kastruimte"`, schrijf je als tekst, zoals hij in het rapport staat. Dat geldt ook voor een naam die je in de test zelf als tekst meegeeft, zoals `"Badkamer1"`.

Bereken de verwachte punten zelf uit de bron en neem ze niet over uit de output van de code, zodat de test de beleidsregel controleert en niet de code.

### Vergelijken met de testreferentie

Sluit de test af met `vergelijk_met_testreferentie(eenheid, groep)`. Die aanroep doet drie dingen, in deze volgorde:

1. Hij faalt bij een `UserWarning` die de test niet heeft meegegeven; zie [Waarschuwingen](#waarschuwingen).
2. Hij controleert wat voor elke gewaardeerde stelselgroep geldt: de criterium-id's zijn uniek, punten en aantallen staan niet zowel op een bovenliggende als op een onderliggende waardering, het totaal van de stelselgroep is de som van de waarderingen en is afgerond op kwarten, en punten hebben ten hoogste twee decimalen.
3. Hij vergelijkt de waardering met de [testreferentie](#testreferenties) van de test.

Roep de fixture één keer per test aan; een tweede aanroep laat de test falen.

### Waarschuwingen

Roept een scenario een `UserWarning` op, vang die dan op met `pytest.warns` en geef de opgevangen waarschuwingen als derde argument mee aan `vergelijk_met_testreferentie`:

```python
with pytest.warns(UserWarning, match="wastafel") as waarschuwingen:
    groep = sanitair.waardeer(eenheid)

assert punten_per_naam(groep) == {}
vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)
```

De volledige tekst van elke meegegeven waarschuwing komt in de testreferentie. Een `UserWarning` die je niet met `pytest.warns` opvangt, laat de test falen. Een waarschuwing die je wel opvangt maar niet meegeeft, ontbreekt ongemerkt in de testreferentie; geef ze daarom altijd mee.

### Meerdere gevallen in één test

Verschillen de gevallen van een beleidsregel alleen in wat er in een ruimte staat, zet ze dan samen in één test. Geef elk geval een eigen ruimte, zet de ruimten op volgorde van punten, van laag naar hoog, en vergelijk de hele uitkomst met `punten_per_bovenliggende`. Nummer ruimten van dezelfde detailsoort (`Badkamer1`, `Badkamer2`): de naam zegt dan in wat voor ruimte de voorziening staat, en het geval lees je af aan de voorziening zelf.

```python
eenheid = EenhedenEenheid(
    ruimten=[
        badkamer(Installatiesoort.douche, naam="Badkamer1"),
        badkamer(Installatiesoort.bad, naam="Badkamer2"),
        badkamer(Installatiesoort.bad_en_douche, naam="Badkamer3"),
    ]
)

groep = sanitair.waardeer(eenheid)

assert punten_per_bovenliggende(groep) == {
    "Badkamer1": {Installatiesoort.douche.naam: 4.0},
    "Badkamer2": {Installatiesoort.bad.naam: 6.0},
    "Badkamer3": {Installatiesoort.bad_en_douche.naam: 7.0},
}
```

Zo staan alle gevallen naast elkaar in één rapport. Dit kan alleen wanneer de ruimten elkaars waardering niet beïnvloeden.

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

Geef elk geval een id met `pytest.param(..., id="...")`, als letterlijke tekst. De id noemt de situatie (`precies_1m`), niet de uitkomst; de verwachting staat in de kolom ernaast. De id wordt onderdeel van de bestandsnaam van de testreferentie en mag daarom alleen letters, cijfers, `_` en `-` bevatten.

## Een functietest schrijven

Een functietest roept de functie rechtstreeks aan en assert de uitkomst, zoals `tests/stelsels/utils/test_rond_af_op_kwart.py`. Hij heeft geen testreferentie en gebruikt `vergelijk_met_testreferentie` dus niet.

## Testreferenties

Een testreferentie is een Markdown-bestand in de map `testreferenties/` naast de testmodule, met de naam van de test: `test_meerdere_kastruimtes_tellen_samen_als_een.md`, of `test_naam[id].md` voor een geval uit een tabel. Het bestand bevat de docstring van de test, het rapport, de waarschuwingen, de input als VERA-JSON en de output-JSON. Van de input staan alleen de velden erin die de test invult, niet de standaardwaarden van het model.

De input staat erbij omdat de test maar een deel van het inputmodel laat zien. De functies uit `tests/input.py` vullen ook velden van de `EenhedenEenheid` die niet in de test staan, zoals de id, de naam en de oppervlakte van een ruimte. Verandert iemand zo'n functie, dan laat de testreferentie per test zien dat de input is gewijzigd.

Een testreferentie heeft één schrijver: de fixture `vergelijk_met_testreferentie`, en die schrijft alleen bij [het bijwerken](#verwachte-output-bijwerken). Bewerk het bestand nooit met de hand. De map is uitgesloten van `prettier`.

### Wanneer een test faalt

`vergelijk_met_testreferentie` vergelijkt de waardering met de testreferentie en laat de test falen wanneer:

- de waardering afwijkt van de testreferentie; de melding toont het verschil;
- de testreferentie ontbreekt, zoals bij een nieuwe test.

Daarnaast controleert `vergelijk_met_testreferentie` de eigenschappen die voor elke gewaardeerde stelselgroep gelden: unieke criterium-id's, geen dubbeltelling van punten of aantallen in de hiërarchie, een totaal van de stelselgroep dat gelijk is aan de som van de waarderingen, afronding op kwartpunten en ten hoogste twee decimalen.

Een aparte test, `test_geen_verweesde_testreferenties`, faalt wanneer er een testreferentie is waar geen test meer bij hoort.

### Bijwerken en verwijderen

Hoe je een testreferentie bijwerkt, staat onder [Verwachte output bijwerken](#verwachte-output-bijwerken).

Bijwerken verwijdert geen bestanden. Heb je een test bewust verwijderd of hernoemd, verwijder dan zelf zijn testreferentie. Verwijder een testreferentie niet om een andere reden.

### Beoordelen in een pull request

De wijzigingen onder `**/testreferenties/**` zijn het overzicht van wat een pull request aan de output verandert. Elk bestand begint met de naam van de test, de beleidsregel en de bron, zodat de diff zelf zegt welke beleidsregel geraakt is. Beoordeel bij elke gewijzigde testreferentie of de wijziging de bedoeling is, en of alleen de input, alleen de output of beide zijn gewijzigd.

## Verwachte output bijwerken

De verwachte output van de tests staat op drie plekken: de testreferenties, `tests/data/**/output/` en `tests/docs/output_json_*.json`. Eén opdracht werkt ze alle drie bij:

```bash
task genereer-test-output
```

De task draait `scripts/genereer_test_output.py` en daarna de tests met de optie `--werk-testreferenties-bij`, en overschrijft daarbij alle verwachte output. Zonder die optie vergelijkt `pytest` alleen.

Na het bijwerken slaagt elke vergelijking met de verwachte output, ook als de nieuwe output fout is. Een groene suite zegt dan niet dat de code klopt, alleen dat de verwachte output is meegeschoven. Werk daarom alleen bij wanneer je vooraf weet dat de output gaat wijzigen. Wanneer dat zo is, en wat je doet als een test afwijkt terwijl de taak dat niet voorzag, staat in `AGENTS.md` onder "Verwachte output". Die afspraken gelden voor agents en voor ontwikkelaars.

`docs/aan-de-slag/index.md` bevat voorbeeld-output (JSON en rapport) die de opdracht niet bijwerkt. Wijzigen output, namen of criterium-id's, loop die voorbeelden dan met de hand na en werk ze bij.

## JSON-modellen

Sanitair voor zelfstandige woonruimten is omgezet naar waarderingstests. De overige stelselgroepen en de modellen op stelselniveau gebruiken eenheidmodellen in JSON onder `tests/data/...`, met verwachte output in `output/`.

### Verwachte output van JSON-modellen

De verwachte output staat onder `tests/data/**/output/*.json` en `tests/docs/output_json_*.json`. Hoe je hem bijwerkt, staat onder [Verwachte output bijwerken](#verwachte-output-bijwerken).

Naast elke output-JSON onder `tests/data/` schrijft het script een `*.txt` met de woningwaardering in leesbaar tabelformaat. Die bestanden zijn bedoeld om wijzigingen in de output in een pull request te beoordelen; `pytest` vergelijkt alleen de JSON-bestanden.

### Model op stelselniveau of test op de stelselgroep

Een model onder `tests/data/<stelsel>/input/` wordt door het hele stelsel gewaardeerd én per stelselgroep gecontroleerd: elke `test_<Stelselgroep>_output` draait erop. Eén model dekt daarmee alle stelselgroepen tegelijk.

Kies een model op stelselniveau wanneer een beleidsregel over meer dan één stelselgroep gaat. Een laadpaal op een parkeerplek komt bijvoorbeeld in rubriek 10 óf in rubriek 12 terecht; dat een plek niet in beide punten krijgt, is alleen zichtbaar wanneer beide rubrieken in dezelfde uitkomst staan. Zie `tests/data/zelfstandige_woonruimten/input/parkeerruimten_en_laadpalen.json`. Dezelfde input in een test per stelselgroep zetten geeft die zekerheid niet, en levert meerdere keren dezelfde input op.

Kies een test op de stelselgroep voor een beleidsregel die binnen één stelselgroep blijft, en voor elk scenario dat een `UserWarning` oproept: een model op stelselniveau moet zonder waarschuwing te waarderen zijn.

- Is de stelselgroep omgezet, dan schrijf je een [waarderingstest](#een-waarderingstest-schrijven).
- Is de stelselgroep nog niet omgezet, dan zet je een model in de map van de stelselgroep, zoals `tests/data/zelfstandige_woonruimten/stelselgroepen/keuken/input/aanrecht_1.json`.

## Test coverage rapport

Na het uitvoeren van `pytest` wordt er een code coverage report getoond. Hierin is per bestand te zien welk percentage van de code getest is.
Daarnaast wordt de code coverage naar het bestand `lcov.info` geschreven. Dat kan gebruikt worden in VSCode om de coverage weer te geven met een plugin zoals "Coverage Gutters".
