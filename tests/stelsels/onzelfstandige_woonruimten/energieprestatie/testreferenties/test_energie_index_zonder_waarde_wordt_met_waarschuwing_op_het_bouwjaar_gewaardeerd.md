# test_energie_index_zonder_waarde_wordt_met_waarschuwing_op_het_bouwjaar_gewaardeerd

Een energie-index zonder waarde wordt met een waarschuwing op het bouwjaar gewaardeerd.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.3.

## Rapport

```text
ENERGIEPRESTATIE
  Bouwjaar 1970                                                      10.00 m²    -1.50 pt
                                                                                ------
  Totaal                                                                         -1.50 pt
```

## Waarschuwingen

- UserWarning: Eenheid (eenheid): energie-index mist waarde en kan daarom niet worden gewaardeerd onder stelselgroep Energieprestatie.

## Input

```json
{
  "id": "eenheid",
  "bouwjaar": 1970,
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
      "einddatum": "2028-06-01"
    }
  ],
  "monumenten": [],
  "ruimten": [
    {
      "id": "slaapkamer",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer",
      "oppervlakte": 10.0
    }
  ]
}
```

## Output

```json
{
  "criteriumGroep": {
    "stelsel": {
      "code": "ONZ",
      "naam": "Onzelfstandige woonruimten"
    },
    "stelselgroep": {
      "code": "ENE",
      "naam": "Energieprestatie"
    }
  },
  "punten": -1.5,
  "woningwaarderingen": [
    {
      "aantal": 10.0,
      "criterium": {
        "id": "energieprestatie__bouwjaar",
        "naam": "Bouwjaar 1970",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": -1.5
    }
  ]
}
```
