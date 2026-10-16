---
name: huurprijscheck
description: >-
  Rekent een scenario door in de huurprijscheck van de Huurcommissie (zelfstandige en
  onzelfstandige woonruimte) met een script dat de online wizard bedient, en leest de
  puntentelling per rubriek uit. Gebruik wanneer wettekst en online beleidsboek geen uitsluitsel
  geven over een beleidsregel, of wanneer de gebruiker vraagt wat de huurprijscheck voor een
  situatie berekent of of de package daarmee overeenkomt. Niet voor het doorrekenen van grote
  aantallen woonruimten.
---

# Huurprijscheck

De huurprijscheck is de rekentool van de Huurcommissie. Hij heeft geen API; `scripts/huurprijscheck.py` bedient de wizard via HTTP en leest veldnamen en keuzes uit de pagina zelf. Het script gebruikt alleen de standaardbibliotheek.

## Regels

- De huurprijscheck staat in de volgorde van autoriteit onder wettekst en online beleidsboek (zie Domeinregels in `AGENTS.md`). Is de wettekst eenduidig, dan blijft die leidend, ook als de tool iets anders berekent; meld het verschil dan.
- Rapporteer alleen wat het script heeft teruggegeven. Lukt het doorrekenen niet, zeg dat en vraag de gebruiker de tool zelf te controleren.
- Gebruik fictieve gegevens en vul WOZ-waarde en energielabel zelf in. Zoek alleen een adres op wanneer de uitkomst van de regio afhangt, en gebruik dan een adres dat de gebruiker geeft of dat al in `tests/data/` staat.
- Het is een publieke dienst: reken één scenario tegelijk door, niet in een lus over testdata.

## Werkwijze

Roep het script aan vanuit de root van de repository. Elk commando drukt de velden van de huidige pagina af, de links die je kunt volgen en de puntentelling tot nu toe.

```bash
python skills/huurprijscheck/scripts/huurprijscheck.py start zelfstandig
python skills/huurprijscheck/scripts/huurprijscheck.py volgende regime=39 wozValue=300000 wozReferenceDate=1-1-2025 energyPerformanceType="Energielabel vanaf 2021" energyPerformanceNewLabel="Label C" houseType=1
python skills/huurprijscheck/scripts/huurprijscheck.py kies Woonkamer
python skills/huurprijscheck/scripts/huurprijscheck.py vul size=20 heated=Ja
python skills/huurprijscheck/scripts/huurprijscheck.py kies "Woonkamer Toevoegen"
python skills/huurprijscheck/scripts/huurprijscheck.py volgende
python skills/huurprijscheck/scripts/huurprijscheck.py resultaat
```

| Commando                                     | Wat het doet                                                                                                                                                        |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `start zelfstandig` of `start onzelfstandig` | Begint een nieuwe, lege huurprijscheck                                                                                                                              |
| `toon`                                       | Toont de huidige pagina opnieuw; `toon --tekst` drukt ook alle tekst af, inclusief toelichting en meldingen                                                         |
| `vul veld=waarde ...`                        | Vult velden in en slaat tussentijds op, zonder de pagina te verlaten                                                                                                |
| `volgende [veld=waarde ...]`                 | Vult velden in en gaat naar de volgende stap                                                                                                                        |
| `kies "<linknaam>"`                          | Volgt een link uit de lijst `Links voor kies`: een ruimte of voorziening kiezen, `... Toevoegen`, `... Wijzigen`, `... Verwijderen`, of terug naar een eerdere stap |
| `adres <postcode> <huisnummer>`              | Zoekt op stap 1 een adres op; de wizard legt daarmee de gemeente vast                                                                                               |
| `resultaat`                                  | Drukt het volledige resultaat af: meldingen over ontbrekende gegevens, totaal, maximale huurprijs, opslagen en de puntentelling per rubriek                         |

Een veld benoem je met het laatste deel van de naam uit de veldenlijst (`size` voor `rooms.123.size`). Een keuze geef je als waarde (`heated=1`) of als label (`heated=Ja`). Ga af op de vraag in de middelste kolom, niet op de veldnaam: `serviceFlat` is bijvoorbeeld de vraag naar voorzieningen voor personen met een handicap.

Isoleer de regel die je onderzoekt: reken hetzelfde scenario twee keer door met één verschil en vergelijk de regel in de puntentelling waar het om gaat. Houd de rest van het scenario zo klein mogelijk.

## Valkuilen

- De wizard loopt in vaste stappen: woning of woonruimte, binnenruimtes, buitenruimtes, bijzonderheden, resultaat. Het tijdvak (`regime`) bepaalt welke regels gelden; kies het tijdvak van de peildatum.
- De wizard houdt je niet tegen bij ontbrekende gegevens. Controleer daarom met `resultaat` of er bovenaan een melding staat dat gegevens ontbreken; de puntentelling is dan onvolledig.
- De peildatum van de WOZ-waarde moet bij het tijdvak horen: per tijdvak accepteert de wizard twee peildata, anders meldt het resultaat een ongeldige peildatum.
- Bij het energielabel moet `energyPerformanceType` passen bij het veld dat je invult (`Energielabel vanaf 2021` hoort bij `energyPerformanceNewLabel`). Anders meldt het resultaat dat het energielabel ontbreekt.
- WOZ-punten verschijnen pas wanneer er oppervlakte is ingevuld. Bij onzelfstandige woonruimte hangen ze bovendien af van de regio: zonder `adres` rekent de wizard geen WOZ-punten.
- Een ruimte bestaat zodra je hem met `kies` hebt gekozen, ook als je niets invult. Vul hem met `vul` en sluit af met `kies "<ruimte> Toevoegen"`, of haal hem weg met `kies "<ruimte> Verwijderen"`.
- Een voorziening (keuken, sanitair, parkeerplek) zet je aan met `features.<nr>.select=1`; het aantal geef je met `features.<nr>.number`.
- Gedeelde ruimtes: bij zelfstandig eerst `hasSharedIndoorRooms=Ja` op stap 1, daarna staan de gedeelde ruimtes in de linklijst (bij een dubbele naam is de variant met `(2)` de gedeelde). Bij onzelfstandig heeft elke ruimte het veld `numberOfRoommates`, dat standaard op het aantal onzelfstandige woonruimten van stap 1 staat: zet het op 1 voor een ruimte voor eigen gebruik; `numberOfPeople` (aantal adressen) komt erbij na `hasSharedIndoorRooms=Ja` op stap 1.
- Keuzes en veldnamen verschillen tussen zelfstandig en onzelfstandig en per tijdvak. Lees ze uit `toon` in plaats van ze over te nemen uit een eerder scenario; bij een onbekende keuze noemt het script de geldige keuzes.
- De puntentelling die `toon`, `vul` en `kies` afdrukken is een tussenstand zonder opslagen. Gebruik `resultaat` voor de uitkomst.
- Het script leest de formulieren zoals de site ze nu opbouwt. Geeft een commando geen velden of geen puntentelling meer terug, dan is de site gewijzigd: meld dat en vraag de gebruiker de tool zelf te controleren.

## Vastleggen

Leg een uitkomst die een implementatiekeuze onderbouwt vast in de relevante pagina van `docs/implementatietoelichtingen/`: de datum van de controle, het tijdvak, de ingevulde gegevens en de regels uit de puntentelling waar het om gaat.
