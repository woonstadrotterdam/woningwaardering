# Bugbot-regels — woningwaardering

Beoordeel pull requests op concrete risico's en regressies. Vermijd stijlcommentaar zonder duidelijke meerwaarde.

Bij wijzigingen onder `woningwaardering/stelsels/` en `woningwaardering/vera/` gelden ook de geneste `.cursor/BUGBOT.md`-bestanden in die mappen.

## Documentatie en bronnen

Betrek bij reviews expliciet de documentatie die bij het soort wijziging hoort:

- `README.md` voor doel, disclaimer, actuele beleidsboekverwijzingen en gebruikte VERA-versies.
- `AGENTS.md` voor repo-afspraken over bronnen, tests, documentatie-updates, warnings en codeconventies.
- `CONTEXT.md` voor bronvolgorde, terminologie en projectgrenzen.
- `docs/index.md` en `docs/voor-ontwikkelaars/index.md` als ingangen naar gebruikers- en ontwikkelaarsdocumentatie.
- `docs/aan-de-slag/index.md` bij wijzigingen in warnings, voorbeeldgebruik, outputstructuur of inline voorbeeld-output.
- `docs/voor-ontwikkelaars/criteriumstrategie.md` bij wijzigingen in outputopbouw, builders, `bovenliggendeCriterium`, subgroepen of gedeeld-met-lagen.
- `docs/implementatietoelichtingen/` bij beleidsinterpretaties, implementatiestatus of bekende beperkingen per stelselgroep.

Bij domeinlogica of puntberekeningen geldt de autoriteitsvolgorde uit `CONTEXT.md` en `AGENTS.md`: wettekst > online beleidsboek > implementatietoelichting.

- Zoek eerst in `wettelijke-documenten/BWBR0003237_2026-01-01_0.xml`, en verifieer daarna tegen de officiële online wettekst op `wetten.overheid.nl`.
- Behandel het online beleidsboek van de Huurcommissie als actueler dan onze lokale implementatietoelichting.
- Signaleer tegenstrijdigheden tussen wettekst, online beleidsboek en implementatietoelichting expliciet in plaats van stilzwijgend één bron te volgen.

## Terminologie

Bewaak de terminologie uit `CONTEXT.md`:

- gebruik `test-case` of `test-cases`, niet `fixture` of `fixtures`;
- gebruik bij outputstructuur termen als `waardering`, `criterium`, `subgroep`, `bovenliggende` en `onderliggende`, niet generiek boomjargon zoals "node", "leaf" of "root";
- sluit bij stelsels, stelselgroepen en referentiedata aan op de VERA-benamingen uit `CONTEXT.md` en `woningwaardering/vera/referentiedata`.

## Tests

Als een PR code onder `woningwaardering/` wijzigt, controleer of passende tests zijn toegevoegd of aangepast.

Naamgeving (gecontroleerd in `tests/`):

- Module- of functie-tests: snake_case gelijk aan de module of functie, bijvoorbeeld `tests/stelsels/test_utils.py`, `tests/stelsels/utils/test_rond_af_op_kwart.py`, `tests/stelsels/gedeelde_logica/test_sanitair_groepering.py`.
- Stelsel- of stelselgroep-tests (classes): PascalCase gelijk aan de klassenaam, bijvoorbeeld `tests/stelsels/test_ZelfstandigeWoonruimten.py`, `tests/data/zelfstandige_woonruimten/stelselgroepen/punten_voor_de_woz_waarde/test_PuntenVoorDeWozWaarde.py`.
- Testfuncties beginnen met `test_`.

Overige testregels:

- Stelselgroeptests staan vaak onder `tests/data/<stelsel>/stelselgroepen/<stelselgroep>/`; detailtests op helpers onder `tests/stelsels/`.
- Gebruik `tests/data/...` voor VERA-inputmodellen en verwachte output.
- Geef bij regressies de voorkeur aan scenariotests (bijv. `test_waardeer_sanitair_groepeert_per_ruimte`)
- Signaleer geen ontbrekende tests bij pure documentatie-, configuratie- of chore-wijzigingen.

### Test-cases

Test-cases onder `tests/data/**/input/` horen zo klein mogelijk te zijn, zonder irrelevante of ongebruikte velden, maar wel groot genoeg om de bedoelde regel te bewijzen.

- Goed: `tests/data/onzelfstandige_woonruimten/stelselgroepen/sanitair/input/toilet_aparte_ruimte.json` — alleen de ruimte en installaties die de regel raken.
- Fout: ongebruikte velden meenemen, zoals `"gemeenschappelijk": false` in `tests/data/onzelfstandige_woonruimten/stelselgroepen/aftrekpunten/input/wel_aftrek.json` wanneer dat veld de testuitkomst niet beïnvloedt.

Onwaarschijnlijke of extreme test-cases zijn alleen wenselijk als ze bewust als randgeval dienen; verwacht dan een korte toelichting in testnaam, commentaar of implementatietoelichting.

- Goed (bewust randgeval): `bouwkundig_element_twee_bad_en_douche.json` met twee baden en twee douches in één badkamer, bedoeld om koppeling/maximering te forceren — alleen acceptabel met toelichting waarom dit scenario nodig is.
- Fout: dezelfde extreme test-case toevoegen zonder uitleg, alsof het een realistische standaardcase is.

### Outputwijzigingen

Als een PR output wijzigt, controleer ook:

- of expected outputs onder `tests/data/**/output/` en `tests/docs/output_json_*.json` zijn bijgewerkt;
- of de output-diffs inhoudelijk zijn beoordeeld en niet alleen blind opnieuw gegenereerd via `task genereer-test-output`;
- of `docs/aan-de-slag/index.md` is nagekeken wanneer output, namen of criterium-id's wijzigen.

## Implementatietoelichting

Vraag alleen om een update van `docs/implementatietoelichtingen/` wanneer de PR:

- een nieuwe afwijking of interpretatie van beleidsregels introduceert;
- laat zien dat VERA of het inputmodel onvoldoende informatie bevat;
- extra toelichting nodig maakt om de gekozen implementatie te begrijpen of te verantwoorden.

Vraag niet om documentatie-updates bij bugfixes of refactors die de bestaande implementatietoelichting gewoon volgen.

Als een update wel nodig is, verwacht een korte toelichting met bronverwijzing naar beleidsboek en/of wettekst. Volg de autoriteitsvolgorde: wettekst > online beleidsboek > implementatietoelichting.

Vraag waar mogelijk om de relevante pagina onder `docs/implementatietoelichtingen/` te actualiseren, niet alleen om een algemene documentatie-update zonder bestemming.

Bij ambigu of indirect beleid: verwacht inhoudelijke onderbouwing vanuit wet, beleidsboek en waar relevant een externe referentie zoals de huurprijscheck. Signaleer interpretaties die alleen op aannemelijkheid leunen.

## Comments en docstrings

Signaleer onnodige verwijdering van comments of docstrings die inhoudelijke waarde hadden, met name:

- beleids- of wetsverwijzingen (bijv. `# 2.2.2.3 Zolderruimte zonder vaste trap`);
- uitleg die de herleidbaarheid van domeinlogica vergroot;
- toelichting op niet-triviale keuzes of beperkingen van VERA.

Maak geen opmerkingen over triviaal commentaar zonder inhoudelijke waarde.

## VERA-gebruik in domeincode

Als een PR VERA-modellen, enums, referentiedata of modeluitbreidingen gebruikt of wijzigt:

- gebruikte types, enums en attributen moeten aansluiten op VERA-definities en referentiedata onder `woningwaardering/vera/referentiedata`;
- naamgeving van stelsels/stelselgroepen volgt de VERA-enums (bijv. `Woningwaarderingstelselgroep.oppervlakte_van_vertrekken`);
- modeluitbreidingen moeten al gedocumenteerd zijn in `docs/implementatietoelichtingen/datamodel-uitbreidingen.md`, of in dezelfde PR worden toegelicht.

## PR-scope

Signaleer wijzigingen die niet logisch bij de PR horen, zoals:

- code of tests voor een andere stelselgroep dan het beschreven probleem;
- documentatie- of implementatietoelichtingswijzigingen die geen direct gevolg zijn van deze PR;
- meelifter-refactors die beter in een aparte PR passen.

## Codekwaliteit

Wees streng op duidelijke verslechtering van de codekwaliteit, maar stel geen grote herschrijving voor zonder concreet voordeel.

Signaleer in ieder geval:

- nieuwe ad-hoc uitzonderingen in bestaande logica waar een helper of betere plaatsing duidelijker zou zijn;
- copy-paste terwijl bestaande canonieke helpers of gedeelde logica al beschikbaar zijn;
- dunne wrappers of extra abstracties zonder duidelijke meerwaarde.

Voorbeelden:

- Goed: hergebruik `parkeertype_punten_mapping` in `woningwaardering/stelsels/gedeelde_logica/gemeenschappelijke_parkeerruimten/gemeenschappelijke_parkeerruimten.py` als enige bron voor Type I/II/III-punten.
- Fout: een aparte frozenset of tweede mapping met dezelfde detailsoorten ernaast introduceren.
- Geen stijlcommentaar: hernoemen van een lokale variabele of herschrijven van een verder duidelijke list comprehension zonder gedrags- of herbruikbaarheidswinst.

Doe alleen een vereenvoudigingsvoorstel als dat het gedrag behoudt en de code aantoonbaar eenvoudiger of herbruikbaarder maakt.

## Overig

Signaleer secrets, credentials of org-interne datastromen in een PR.
