# Testing

De tests draaien met [pytest](https://docs.pytest.org/). Installatie, de commando's en de pre-commit-checks staan onder [Project opzetten](index.md#project-opzetten) en [Tests en checks](index.md#tests-en-checks).

## Uitgangspunt

Een wijziging in het rapport of de output-JSON van een woningwaardering gebeurt altijd bewust. Daarom vergelijkt `pytest` de output met de verwachte output, maar schrijft hij die nooit. Hoe en wanneer je de verwachte output bijwerkt, staat in `AGENTS.md` onder "Verwachte output"; die afspraken gelden voor agents en voor ontwikkelaars.

## Welke test schrijf je?

| Wat je test | Wat je schrijft |
| --- | --- |
| Een beleidsregel binnen één stelselgroep, ook als ze het puntentotaal van andere rubrieken nodig heeft | Een [waarderingstest](#een-waarderingstest-schrijven) |
| Een beleidsregel die over meer dan één stelselgroep gaat | Een [model op stelselniveau](#model-op-stelselniveau) |
| Een functie die op zichzelf staat | Een unittest |

Een waarderingstest waardeert een stelselgroep, controleert de punten die de beleidsregel toekent en vergelijkt de uitkomst met een testreferentie. Een unittest roept een functie rechtstreeks aan en heeft geen testreferentie, zoals `tests/stelsels/utils/test_rond_af_op_kwart.py`. Hij is bedoeld voor een functie waarvan de uitkomst volgt uit haar argumenten, zoals `rond_af_op_kwart` en `classificeer_ruimte`.

Een privéfunctie van een stelselgroep test je via een waarderingstest: die blijft geldig wanneer de functie wordt herschreven. Test een privéfunctie alleen rechtstreeks wanneer het scenario via de stelselgroep onevenredig veel input vraagt, zoals de grensgevallen van `_cap_punten` van de stelselgroep punten voor de WOZ-waarde, waarvoor je de punten van alle andere stelselgroepen precies zou moeten sturen.

### Model op stelselniveau

Een model is een JSON onder `tests/stelsels/modellen/<stelsel>/`, met een beschrijving in een Markdown-bestand met dezelfde naam. Het hele stelsel waardeert het model, en `tests/stelsels/test_<Stelsel>.py` vergelijkt de uitkomst met een testreferentie, met de beschrijving bovenaan en de waarschuwingen die het model oproept. Kies het voor een beleidsregel die over meer dan één stelselgroep gaat. Een laadpaal op een parkeerplek komt bijvoorbeeld in rubriek 10 óf in rubriek 12 terecht; dat een plek niet in beide punten krijgt, is alleen zichtbaar wanneer beide rubrieken in dezelfde uitkomst staan. Zie `tests/stelsels/modellen/onzelfstandige_woonruimten/parkeerruimten_en_laadpalen.json`.

Controleer één keer met de hand dat de uitkomst klopt, maar alleen voor de beleidsregel waar het model over gaat. De punten van de andere rubrieken neem je over uit het rapport (`task toon-rapport -- <model.json>`). Gaat het model bijvoorbeeld over het minimum van 40 WOZ-punten, dan controleer je of de woning de 110 punten haalt en 40 WOZ-punten krijgt, niet hoeveel punten de keuken krijgt.

Beschrijf in het Markdown-bestand in één of twee zinnen wat het model laat zien.

## Een waarderingstest schrijven

De stappen:

1. Zoek de beleidsregel op in de bron en bereken zelf hoeveel punten het scenario oplevert, zonder de bestaande code te gebruiken. Zo controleert de test de beleidsregel en niet de code.
2. Schrijf de test. De onderdelen hieronder beschrijven hoe.
3. Draai `pytest`. De nieuwe test faalt met de melding `Geen testreferentie`, een geparametriseerde test per geval; alle andere tests slagen. Faalt er meer, los dat dan eerst op: de volgende stap overschrijft alle verwachte output.
4. Draai `task genereer-test-output`. Die schrijft de testreferenties van de test in `testreferenties/` naast de testmodule. Controleer met `git status` dat alleen die testreferenties erbij zijn gekomen, en dat het rapport erin overeenkomt met wat je in stap 1 hebt berekend.
5. Draai de [tests en checks](index.md#tests-en-checks).

Hernoem of verwijder je een test of een id, verwijder dan zelf de oude testreferentie: het bijwerken verwijdert geen bestanden.

Een voorbeeld is `test_meerdere_kastruimtes_tellen_samen_als_een` in `tests/stelsels/zelfstandige_woonruimten/sanitair/test_sanitair_zel.py`. Het achtervoegsel `_zel` of `_onz` van het testbestand is nodig omdat `pytest` geen twee testbestanden met dezelfde naam accepteert.

### Eén beleidsregel per test

Een test controleert één beleidsregel, of één keuze van de package, zoals een waarschuwing bij onvolledige input. Je toetst dat aan de eerste zin van de docstring: die zegt in één bewering wat de test controleert. Heb je daar twee beweringen voor nodig, schrijf dan twee tests.

Een tabel uit één onderdeel van de bron, zoals de punten per aanrechtlengte in onderdeel 5.1 van de wettekst, is één beleidsregel. De eerste zin van de docstring noemt dan wat de tabel bepaalt, bijvoorbeeld "De punten voor een aanrecht hangen af van zijn lengte", en de asserts tonen de grenzen.

### Naam

Begin de naam van een testfunctie met `test_`. Zonder dat voorvoegsel slaat `pytest` de functie stil over: de test draait nooit en de suite blijft groen.

De naam noemt de beleidsregel in gewone taal, niet de input of het rekenvoorbeeld: `test_minder_dan_8m2_aan_vertrekken_geeft_4_punten_aftrek`, niet `test_een_vertrek_van_7m2_geeft_4_punten_aftrek`, en `test_punten_worden_na_verdeling_over_de_adressen_gedeeld_door_de_woonruimten_op_het_adres`, niet `test_rekenvoorbeeld_met_keuken_en_toilet_uit_de_wettekst`. Getallen uit de bron, zoals een grens, een puntental of een percentage, mogen in de naam. Controleert de test een grens uit de bron, dan noemt de naam die grens, en is de input gelijk aan die grens of wijkt hij er één kleinste stap van af (1 mm, 0,01 m², één jaar, één ruimte, één punt): `test_precies_8m2_aan_vertrekken_geeft_geen_aftrek`.

### Docstring

De docstring is verplicht en bestaat uit twee delen, soms drie:

1. De beleidsregel in één zin, die zonder de rest te lezen zegt wat de test controleert. Net als de naam noemt hij geen waarde uit de input.
2. De bronverwijzing van de beleidsregel, zonder citaat: de diepste paragraaf van de implementatietoelichting waarin ze staat en, als ze ook in de wettekst staat, de wettekst erna. In de wettekst heet een regel uit de tabel `onderdeel 6.2` en een passage uit de toelichting `toelichting rubriek 6`, zo nodig met de verwijzing waarlangs ze geldt: `toelichting rubriek 9 (via Bijlage I onder B, toelichting, inleiding)`. `tests/test_bronverwijzingen.py` controleert de vorm en of de bronverwijzing bestaat.
3. Alleen als de asserts zonder een andere beleidsregel niet te volgen zijn: die andere beleidsregel in één zin, met haar bronverwijzing, zoals de deling door het aantal adressen in een test over verkoeling in gemeenschappelijke binnenruimten.

De asserts laten zien hoe de beleidsregel uitpakt; de docstring bevat geen berekening. Ook de punten en waarschuwingen van rubrieken die de beleidsregel niet raakt, leg je niet uit. Heb je die uitleg toch nodig om de test te begrijpen, dan is het scenario te groot: geef alleen de input mee die de beleidsregel raakt. De afronding van het totaal op een kwart punt hoort bij de uitkomst; je legt haar alleen uit als de test daarover gaat.

Volgt de package een beleidsregel niet, of legt de test gedrag vast dat wettekst en beleidsboek niet beschrijven, dan staat die keuze in de implementatietoelichting: doorgestreept of in een toelichtingsblok. Staat ze er nog niet, vul de implementatietoelichting dan aan in dezelfde pull request. Een test van een waarschuwing omdat input ontbreekt, waarna het onderdeel geen punten krijgt, heeft geen bron: de test controleert de waarschuwing zelf.

### Input

Bouw de input op met de functies uit `tests/input.py`. Wat de beleidsregel raakt, geef je in de test mee; de rest krijgt een standaardwaarde in de functie. Waarom je de input zo kiest, zet je in één regel commentaar bij die input. Heeft de beleidsregel het puntentotaal van andere rubrieken nodig, gebruik dan een volledige woning uit `tests/input.py`, zoals `meergezinswoning_van_71_m2(...)`.

Ontbreekt er een functie voor wat je nodig hebt, voeg hem dan toe aan `tests/input.py`. Een functie hoort daar als ze velden afleidt of een standaardwaarde geeft die de beleidsregel niet raakt. Geeft de functie alleen argumenten door, gebruik dan het VERA-model zelf, zoals `EenhedenEnergieprestatie(...)`.

Fixtures zijn bedoeld voor context en niet voor scenario's: de stelselgroep (`sanitair`), de `peildatum` en `vergelijk_met_testreferentie`. Een scenario dat in een fixture staat, is in de test niet meer te lezen.

### Asserts

Assert met de helpers uit `tests/utils.py` de waarderingen die de beleidsregel raakt, plus het totaal (`groep.punten`); de overige waarderingen staan in de testreferentie. Raakt de beleidsregel elke waardering in het scenario, vergelijk dan de hele uitkomst; het totaal heeft dan geen eigen assert nodig. Heeft een waardering geen eigen punten, zoals bij de oppervlakte van vertrekken, assert dan het aantal en het totaal op de stelselgroep. Hoe je op een verwachte waarde komt, mag als commentaar bij de assert staan.

Sluit de test af met `vergelijk_met_testreferentie(eenheid, groep)`. Wat die controleert, staat in zijn docstring in `tests/conftest.py`.

### Waarschuwingen

Roept een scenario een `UserWarning` op, vang die dan op met `pytest.warns` en geef de opgevangen waarschuwingen als derde argument mee aan `vergelijk_met_testreferentie`. Alleen meegegeven waarschuwingen komen in de testreferentie.

### Meerdere gevallen in één test

Verschillen de gevallen van een beleidsregel alleen in wat er in een ruimte staat, zet ze dan samen in één test. Geef elk geval een eigen, genummerde ruimte en vergelijk de hele uitkomst met `punten_per_bovenliggende`, zoals in `test_punten_voor_bad_en_douche` (sanitair, zelfstandig). Zo staan alle gevallen naast elkaar in één rapport. Dit kan alleen wanneer de ruimten elkaars waardering niet beïnvloeden, zoals via een gezamenlijk maximum of een opgetelde oppervlakte.

### Parametriseren

Parametriseer wanneer de gevallen niet samen in één eenheid passen, of wanneer een geval een eigen toelichting nodig heeft. Bij een geparametriseerde test delen alle gevallen dezelfde docstring. Kies daarom per geval een van drie treden:

1. **Tabel.** De gedeelde docstring en de id verklaren het geval volledig: dezelfde beleidsregel met een ander getal.
2. **Tabel met toelichting.** Het geval hoort bij dezelfde beleidsregel, maar heeft één zin uitleg nodig, bijvoorbeeld een grenswaarde. Geef die mee met `pytest.mark.toelichting`; de zin komt in de testreferentie.
3. **Eigen test.** Het geval heeft een eigen reden of bron, of is een uitzondering op de beleidsregel. Kies bij twijfel deze trede.

Geef elk geval een id met `pytest.param(..., id="...")`, als letterlijke tekst. De id noemt de situatie (`precies_1m`), niet de uitkomst; de verwachting staat in de kolom ernaast. Zie `test_spoelbak_in_aanrecht_korter_dan_1m_telt_als_wastafel` (sanitair, zelfstandig).

## Testreferenties beoordelen in een pull request

De wijzigingen onder `**/testreferenties/**` zijn het overzicht van wat een pull request aan de output verandert. Beoordeel bij elke gewijzigde testreferentie of de wijziging de bedoeling is, en of de input, de output of beide zijn gewijzigd. De input staat erin omdat de functies uit `tests/input.py` velden invullen die niet in de test staan, zoals de id en de oppervlakte van een ruimte; verandert zo'n functie, dan zie je dat hier per test.
