<!-- Schrijf volgens ASD-STE100, met de termen uit GLOSSARY.md (zie AGENTS.md, sectie Documentatie). Pas de lengte aan de wijziging aan: een eenvoudige PR blijft kort.
     Schrijf in de hele PR "vóór deze PR" en "na deze PR", ook onder Ook gewijzigd. -->

## Gerelateerde issue(s)

<!-- Vink opties aan met ☑ (niet met - [x]; GitHub telt dat als PR-tasks). -->
<!-- Kies één optie. Gebruik Closes/Fixes/Resolves #123 als het issue met deze PR wordt opgelost. -->

- ☐ Gerelateerde issue: <!-- bijv. Closes #123 of #456 -->
- ☐ Geen gerelateerde issue — waarom is deze PR nodig?

<!-- Indien geen issue: leg hier kort uit waarom deze wijziging nodig is. -->

## Context

<!-- Wat moet een reviewer weten die de code niet kent: welk deel van het package raakt dit
     (bij domeinlogica: welke stelselgroep en welke rekenstap), en wat betekenen de codes die je gebruikt?
     Neem de Context van het issue over en pas hem aan de PR aan. Bij een kleine PR is één zin genoeg. -->

## Samenvatting

<!-- Wat verandert en waarom? Wijkt de PR af van een acceptatiecriterium van het issue, zeg dan welk criterium en waarom.
     Veranderen punten of huurprijs, toon dan per situatie voor en na met de test
     waarvan de testreferentie de input bevat, in de vorm uit docs/agents/voor-en-na.md. Bijvoorbeeld:
     Doorgerekend met de huurprijscheck op 1 november 2026, tijdvak 1 januari 2026 - 31 december 2026.
     |       | Situatie                                                                  | Voor  | Na        | Huurprijscheck |
     | **A** | [ZEL] Sanitair, toilet met fontein in badkamer                            | 3,75  | **2,75**  | gelijk         |
     | **B** | [ZEL] Punten voor de WOZ-waarde, woonkamer 30 m², `PIP` 15 m² bij 1 adres | 55,00 | **42,50** | 44,25          |
     - A: `test_…`
     - B: `test_…`. De huurprijscheck rekent met 12 m² per plek, de package met de werkelijke 15 m². -->

## Soort wijziging

- ☐ Domeinlogica / puntberekening (vul **Bronverwijzing** hieronder in)
- ☐ Documentatie
- ☐ Stijl / refactor (geen gedragswijziging)
- ☐ CI / tooling / build
- ☐ Overig

## Impact op eindgebruiker

<!-- Ziet een gebruiker na upgraden iets anders? Bij ja krijgt de PR het label `impact eindgebruiker`
     (zie docs/voor-ontwikkelaars/releases.md). Punten en huurprijs staan in de tabel onder
     Samenvatting; noem bij de andere aangevinkte soorten wat er verandert. Bijvoorbeeld:
     ☑ Warnings of errors: nieuwe UserWarning bij ontbrekende `afmetingen.hoogte` (was: error) -->

- ☐ Nee
- ☐ Ja, dit verandert voor de gebruiker:
  - ☐ Punten of huurprijs
  - ☐ Criteriumnamen of criterium-id's
  - ☐ Rapport
  - ☐ Warnings of errors
  - ☐ Publieke API of input

## Bronverwijzing

<!-- Alleen invullen als 'Domeinlogica / puntberekening' is aangevinkt; anders overslaan.
     Domeinlogica omvat onder meer wijzigingen in woningwaardering/stelsels/, waarschuwings-
     of foutgedrag, lookup-tabellen, modeluitbreidingen en tests met gewijzigde verwachte punten.
     Lees eerst de relevante implementatietoelichting; check daarna tegen het online beleidsboek en wettekst (zie `docs/voor-ontwikkelaars/bronnen.md`).
     Herhaal het onderstaande blok per gewijzigde domeinregel. -->

### [Stelselgroep / onderwerp]

**Bron:**

- ☐ Beleidsboek Huurcommissie (online, actueel)
- ☐ Wettekst ([wetten.overheid.nl](https://wetten.overheid.nl/BWBR0003237/2026-01-01))
- ☐ Huurprijscheck (wettekst en beleidsboek niet sluitend; datum, tijdvak en input staan in de implementatietoelichting)

**Link:** <!-- pagina van het online beleidsboek of artikel van de wettekst waar de quote staat -->

**Quote:**

> Relevante tekst uit de gekozen bron (met paragraaf- of artikelnummer)

**Opmerking (optioneel):** toelichting op de gemaakte keuze of interpretatie.

## Checklist

<!-- Handmatige follow-ups die CI niet afdwingt. -->

- ☐ Relevante implementatietoelichting geraadpleegd (bij domeinlogica)
- ☐ Bronverwijzing ingevuld (bij domeinlogica)
- ☐ Tests toegevoegd/aangepast (bij gewijzigde domeinlogica)
- ☐ Doorgerekend met de huurprijscheck (bij gewijzigde punten of huurprijs)
- ☐ Waarschuwings- of errorlogica bewust gecontroleerd (indien van toepassing)
- ☐ Documentatie geüpdatet
