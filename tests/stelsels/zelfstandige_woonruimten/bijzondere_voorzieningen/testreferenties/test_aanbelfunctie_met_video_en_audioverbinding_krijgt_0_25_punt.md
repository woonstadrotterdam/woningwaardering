# test_aanbelfunctie_met_video_en_audioverbinding_krijgt_0_25_punt

Een aanbelfunctie met video- en audioverbinding krijgt 0,25 punt.

Bron: wettekst, Bijlage I onder A, rubriek 12: "Aanbelfunctie met video- en
audioverbinding waarbij de voordeur automatisch kan worden geopend vanuit
de woning." en "0,25 punt".

De aanbelfunctie is een installatie van een ruimte, hier de woonkamer. Of
de voordeur vanuit de woning kan worden geopend, controleert de package
niet: de implementatietoelichting haalt die voorwaarde door en houdt de
waardering over. De test legt het huidige gedrag vast.

Bron: implementatietoelichting zelfstandige woonruimten, 2.12.2: "wordt de
aanbelfunctie gewaardeerd met 0,25 punt."

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
      "oppervlakte": 19.1488,
      "verwarmd": true,
      "verkoeld": false,
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
