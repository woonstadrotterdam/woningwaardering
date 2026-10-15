# test_energieprestatievergoeding_geeft_een_vast_aantal_punten_per_m2

Bij een energieprestatievergoeding krijgt de woonruimte 0,50 punt per m² van de vertrekken.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.6.3.

## Rapport

```text
ENERGIEPRESTATIE
  Energieprestatievergoeding                                         10.00 m²     5.00 pt
                                                                                ------
  Totaal                                                                          5.00 pt
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
      "begindatum": "2017-02-23",
      "einddatum": "2027-02-23",
      "label": {
        "code": "C",
        "naam": "C"
      },
      "waarde": "1.48"
    }
  ],
  "monumenten": [],
  "prijscomponenten": [
    {
      "detailSoort": {
        "code": "EPV",
        "naam": "Energieprestatievergoeding"
      }
    }
  ],
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
  "punten": 5.0,
  "woningwaarderingen": [
    {
      "aantal": 10.0,
      "criterium": {
        "id": "energieprestatie__energieprestatievergoeding",
        "naam": "Energieprestatievergoeding",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": 5.0
    }
  ]
}
```
