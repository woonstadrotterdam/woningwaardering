# test_zonder_energieprestatie_en_bouwjaar_krijgt_de_woonruimte_met_waarschuwing_geen_punten

Zonder energieprestatie en zonder bouwjaar krijgt de woonruimte met een waarschuwing geen punten voor de energieprestatie.

## Rapport

```text
ENERGIEPRESTATIE

                                                                                ------
  Totaal                                                                          0.00 pt
```

## Waarschuwingen

- UserWarning: Eenheid (eenheid): 'energieprestaties' is None

## Input

```json
{
  "id": "eenheid",
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
  "punten": 0.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "energieprestatie__onbekend",
        "naam": ""
      }
    }
  ]
}
```
