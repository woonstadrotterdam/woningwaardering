# Bronnen en projectgrenzen

De primaire context is de publieke `woningwaardering`-package. Lokale of organisatie-interne datastromen vallen buiten deze context, tenzij ze expliciet in de repositorydocumentatie zijn opgenomen. Zie [`GLOSSARY.md`](https://github.com/woonstadrotterdam/woningwaardering/blob/main/GLOSSARY.md) voor de domeintaal.

## Bronnen van waarheid

- `README.md` beschrijft het doel, de juridische disclaimer, de actuele beleidsboekreferentie en de gebruikte VERA-versies.
- `pyproject.toml` bevat de package-metadata, Python-versie en vastgelegde VERA-databronnen.
- `docs/aan-de-slag/index.md` beschrijft gebruik, warnings-gedrag en outputstructuur voor gebruikers.
- `docs/voor-ontwikkelaars/` bevat ontwikkelaarsafspraken over installatie, repository-structuur, naamgeving, tests, data, logging, releases en de criteriumstrategie (builders).
- `docs/implementatietoelichtingen/` legt per stelselgroep vast welke beleidsboekregels wel of niet zijn geïmplementeerd en waarom.
- Het online beleidsboek van de Huurcommissie is de officiële, actuele bron: [zelfstandige woonruimte](https://www.huurcommissie.nl/support/beleidsboeken/waarderingsstelsel-zelfstandige-woonruimte) en [onzelfstandige woonruimte](https://www.huurcommissie.nl/support/beleidsboeken/waarderingsstelsel-onzelfstandige-woonruimte). Hiermee worden de HTML-pagina's bedoeld waarnaar deze pagina's doorlinken. De PDF-versie is een momentopname die gedurende het jaar kan achterlopen op de HTML-versie.
- [Wettekst](https://wetten.overheid.nl/BWBR0003237/2026-01-01) (Besluit huurprijzen woonruimte). Een lokale XML-kopie van deze versie staat in `wettelijke-documenten/BWBR0003237_2026-01-01_0.xml`.
- De [huurprijscheck](https://huurprijscheck.huurcommissie.nl/) van de Huurcommissie ([zelfstandig](https://huurprijscheck.huurcommissie.nl/zelfstandige-woonruimte), [onzelfstandig](https://huurprijscheck.huurcommissie.nl/onzelfstandige-woonruimte)).

## Volgorde van autoriteit

Controleer deze bronnen bij wijzigingen in domeinlogica. Voor puntberekeningen geldt de volgende volgorde van autoriteit: **wettekst > online beleidsboek > huurprijscheck > implementatietoelichting**.

- De implementatietoelichting is een kopie van het online beleidsboek en kan achterlopen; bij twijfel of tegenstrijdigheid is de hoger geplaatste bron leidend. Een afwijking is een signaal dat de toelichting moet worden bijgewerkt.
- De huurprijscheck is pas leidend als wettekst en beleidsboek niet sluitend zijn; is de wettekst wél eenduidig, dan blijft die leidend, ook als de tool afwijkt.
- Tegenstrijdigheden tussen bronnen moeten altijd worden vermeld.

Als wettekst en beleidsboek niet sluitend zijn, rekenen agents het scenario door met de skill [`huurprijscheck`](https://github.com/woonstadrotterdam/woningwaardering/blob/main/.claude/skills/huurprijscheck/SKILL.md). Lukt dat niet, dan vragen ze een mens de huurprijscheck te controleren; ze vullen nooit zelf een uitkomst in. Leg de uitkomst vast in de implementatietoelichting.

## Projectgrenzen

- De package berekent woningwaarderingen op basis van een digitale representatie van een woonruimte.
- De berekening volgt het beleidsboek van de Huurcommissie.
- De input en output volgen de VERA-standaard, met de concrete versies vastgelegd in `pyproject.toml`.
- Aan berekeningen en output kunnen geen rechten worden ontleend. Gebruikers moeten documentatie, implementatietoelichtingen en openstaande issues raadplegen om resultaten goed te interpreteren.
- Wanneer VERA of beschikbare inputdata een beleidsregel niet volledig kan dragen, wordt de gekozen interpretatie in de implementatietoelichtingen beschreven. Lokale uitbreidingen op de VERA-modellen staan in `docs/implementatietoelichtingen/datamodel-uitbreidingen.md`.
