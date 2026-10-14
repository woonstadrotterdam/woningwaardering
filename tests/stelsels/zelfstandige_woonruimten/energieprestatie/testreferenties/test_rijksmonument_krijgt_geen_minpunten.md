# test_rijksmonument_krijgt_geen_minpunten

Een rijksmonument krijgt geen minpunten voor de energieprestatie.

Bron: wettekst, Bijlage I onder A, onderdeel 4.2: "Indien de woonruimte
bestaat uit of deel uitmaakt van een rijksmonument, een provinciaal monument
of een gemeentelijke monument als bedoeld in artikel 8a worden voor deze
rubriek geen minpunten toegekend. Voor energielabel E, F en G en daaraan
gelijkgestelde Energie-indexen en bouwjaren, geldt in afwijking van de
bovenstaande tabellen in dat geval een toekenning van nul punten."

De eenheid heeft geen energieprestaties. De package waarschuwt daarvoor en
waardeert op het bouwjaar.

Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
genereert de package een `UserWarning`."

Bron: wettekst, Bijlage I onder A, toelichting rubriek 4.1: "Daar waar een
geldig energielabel ontbreekt, wordt de waardering van de energieprestatie
bepaald op basis van het bouwjaar van de woning."

Een meergezinswoning met bouwjaar 1921 krijgt -15 punten.

Bron: wettekst, Bijlage I onder A, onderdeel 4.1, tabel met de kolommen
energielabel, energie-index, bouwjaar, eengezinswoning en meergezinswoning:
"G EI > 2,7 1976 of ouder –15 –15".

## Rapport

```text
ENERGIEPRESTATIE
  Bouwjaar 1921                                                                 -15.00 pt
  Correctie monument                                                             15.00 pt
                                                                                ------
  Totaal                                                                          0.00 pt
```

## Waarschuwingen

- UserWarning: Eenheid (eenheid): 'energieprestaties' is None

## Input

```json
{
  "id": "eenheid",
  "bouwjaar": 1921,
  "energieprestaties": [],
  "monumenten": [
    {
      "code": "RIJ",
      "naam": "Rijksmonument"
    }
  ],
  "panden": [
    {
      "soort": {
        "code": "MGW",
        "naam": "Meergezinswoning"
      }
    }
  ]
}
```

## Output

```json
{
  "criteriumGroep": {
    "stelsel": {
      "code": "ZEL",
      "naam": "Zelfstandige woonruimten"
    },
    "stelselgroep": {
      "code": "ENE",
      "naam": "Energieprestatie"
    }
  },
  "punten": 0.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "energieprestatie__bouwjaar",
        "naam": "Bouwjaar 1921"
      },
      "punten": -15.0
    },
    {
      "criterium": {
        "id": "energieprestatie__correctie_monument",
        "naam": "Correctie monument"
      },
      "punten": 15.0
    }
  ]
}
```
