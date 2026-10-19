# test_energie_index_wordt_op_de_index_gewaardeerd_niet_op_het_label

Bij een energie-index bepaalt de index de punten per m², niet het label dat erbij is meegegeven.

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.4.4
- wettekst, Bijlage I onder B, onderdeel 4.1

## Rapport

```text
ENERGIEPRESTATIE
  A -> C (Energie-index)                                             10.00 m²     3.50 pt
                                                                                ------
  Totaal                                                                          3.50 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "bouwjaar": 1921,
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
      "begindatum": "2020-08-01",
      "einddatum": "2030-08-01",
      "label": {
        "code": "A",
        "naam": "A"
      },
      "waarde": "1.48"
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
  "punten": 3.5,
  "woningwaarderingen": [
    {
      "aantal": 10.0,
      "criterium": {
        "id": "energieprestatie__label",
        "naam": "A -> C (Energie-index)",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": 3.5
    }
  ]
}
```
