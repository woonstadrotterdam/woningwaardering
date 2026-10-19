# test_energie_index_zonder_label_wordt_op_de_index_gewaardeerd

Een energie-index zonder label bepaalt de punten per m².

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.4.2
- implementatietoelichting onzelfstandige woonruimten, 2.4.4
- wettekst, Bijlage I onder B, onderdeel 4.1

## Rapport

```text
ENERGIEPRESTATIE
  Energie-index                                                      10.00 m²     6.50 pt
                                                                                ------
  Totaal                                                                          6.50 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
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
      "einddatum": "2028-06-01",
      "waarde": "1.0"
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
  "punten": 6.5,
  "woningwaarderingen": [
    {
      "aantal": 10.0,
      "criterium": {
        "id": "energieprestatie__label",
        "naam": "Energie-index",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": 6.5
    }
  ]
}
```
