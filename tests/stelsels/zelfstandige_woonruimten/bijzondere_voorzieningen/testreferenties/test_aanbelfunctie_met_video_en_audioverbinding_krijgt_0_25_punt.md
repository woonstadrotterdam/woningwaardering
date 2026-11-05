# test_aanbelfunctie_met_video_en_audioverbinding_krijgt_0_25_punt

Een aanbelfunctie met video- en audioverbinding krijgt 0,25 punt.

Bron:
- implementatietoelichting zelfstandige woonruimten, 2.12.2
- wettekst, Bijlage I onder A, onderdeel 12

## Rapport

```text
BIJZONDERE VOORZIENINGEN
  Aanbelfunctie met video- en audioverbinding                                     0.25 pt
                                                                                ------
  Totaal                                                                          0.25 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "id": "aanbelfunctie",
  "ruimten": [
    {
      "id": "woonkamer",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "WOO",
        "naam": "Woonkamer"
      },
      "naam": "Woonkamer",
      "oppervlakte": 10.0,
      "installaties": [
        {
          "code": "ABF",
          "naam": "Aanbelfunctie met video- en audioverbinding"
        }
      ]
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
      "code": "BIJ",
      "naam": "Bijzondere voorzieningen"
    }
  },
  "punten": 0.25,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "bijzondere_voorzieningen__aanbelfunctie_met_video_en_audioverbinding",
        "naam": "Aanbelfunctie met video- en audioverbinding"
      },
      "punten": 0.25
    }
  ]
}
```
