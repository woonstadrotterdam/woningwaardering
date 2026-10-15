# test_ruimte_met_onbekende_detailsoort_telt_niet_mee_als_vertrek

Een ruimte met een detailsoort die de package niet kent, wordt niet als vertrek geteld.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.1.2.

## Rapport

```text
AFTREKPUNTEN
  Oppervlakte van vertrekken is minder dan 8 m²                       0.00 m²    -4.00 pt
                                                                                ------
  Totaal                                                                         -4.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "berging",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "BRG",
        "naam": "Berging"
      },
      "naam": "Berging",
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
      "code": "AFT",
      "naam": "Aftrekpunten"
    }
  },
  "punten": -4.0,
  "woningwaarderingen": [
    {
      "aantal": 0.0,
      "criterium": {
        "id": "aftrekpunten__oppervlakte_van_vertrekken_minder_dan_8m2",
        "naam": "Oppervlakte van vertrekken is minder dan 8 m²",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": -4.0
    }
  ]
}
```
