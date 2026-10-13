# test_energieprestatie_zonder_soort_telt_niet_mee

Een energieprestatie zonder soort telt niet mee: de woning wordt op het bouwjaar gewaardeerd.

De package slaat een energieprestatie zonder soort over zonder te
waarschuwen. De implementatietoelichting noemt die keuze niet; de test legt
het huidige gedrag vast. Het label heeft hier alleen een naam, geen code.

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
                                                                                ------
  Totaal                                                                        -15.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "bouwjaar": 1921,
  "energieprestaties": [
    {
      "status": {
        "code": "DEF",
        "naam": "Definitief"
      },
      "begindatum": "2017-02-23",
      "einddatum": "2027-02-23",
      "label": {
        "naam": "C"
      },
      "waarde": "1.48"
    }
  ],
  "monumenten": [],
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
  "punten": -15.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "energieprestatie__bouwjaar",
        "naam": "Bouwjaar 1921"
      },
      "punten": -15.0
    }
  ]
}
```
