# test_energie_index_zonder_waarde_wordt_met_waarschuwing_op_het_bouwjaar_gewaardeerd

Een energie-index zonder waarde wordt met een waarschuwing op het bouwjaar gewaardeerd.

Bron: implementatietoelichting zelfstandige woonruimten, 2.4.3: "Een
energieprestatie van een ander soort dan energie-index in de periode
2015-2021, of een energie-index zonder bruikbare `waarde`, telt niet mee
(2.4.3, punt 4); de waardering valt dan terug op het bouwjaar (2.4.5). Bij
een energie-index zonder `waarde` gebeurt dit met een `UserWarning`
(standaard een error)."

Een eengezinswoning met bouwjaar 1990 krijgt 14 punten.

Bron: wettekst, Bijlage I onder A, onderdeel 4.1, tabel met de kolommen
energielabel, energie-index, bouwjaar, eengezinswoning en meergezinswoning:
"D 1,8 < EI ≤ 2,1 1984 t/m 1991 14 11".

## Rapport

```text
ENERGIEPRESTATIE
  Bouwjaar 1990                                                                  14.00 pt
                                                                                ------
  Totaal                                                                         14.00 pt
```

## Waarschuwingen

- UserWarning: Eenheid (eenheid): energie-index mist waarde en kan daarom niet worden gewaardeerd onder stelselgroep Energieprestatie.

## Input

```json
{
  "id": "eenheid",
  "bouwjaar": 1990,
  "energieprestaties": [
    {
      "soort": {
        "code": "EI",
        "naam": "Energie-index"
      },
      "status": {
        "code": "DEF",
        "naam": "Definitief"
      },
      "begindatum": "2018-06-01",
      "einddatum": "2028-06-01",
      "label": {
        "code": "A",
        "naam": "A"
      }
    }
  ],
  "monumenten": [],
  "panden": [
    {
      "soort": {
        "code": "EGW",
        "naam": "Eengezinswoning"
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
  "punten": 14.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "energieprestatie__bouwjaar",
        "naam": "Bouwjaar 1990"
      },
      "punten": 14.0
    }
  ]
}
```
