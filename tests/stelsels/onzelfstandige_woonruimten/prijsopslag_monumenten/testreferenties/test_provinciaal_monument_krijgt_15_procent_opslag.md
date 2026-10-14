# test_provinciaal_monument_krijgt_15_procent_opslag

Een provinciaal monument krijgt 15% opslag op de maximale huurprijs.

Bron: wettekst, artikel 8a, derde lid: "De maximale huurprijsgrens wordt
met 15% vermeerderd indien de woonruimte bestaat uit of deel uitmaakt van
een door het college van burgemeester en wethouders aangewezen gemeentelijk
monument of een door gedeputeerde staten aangewezen provinciaal monument."

## Rapport

```text
PRIJSOPSLAG MONUMENTEN
  Gemeentelijk of provinciaal monument                                                         15%
                                                                                ------
  Totaal                                                                          0.00 pt      15%
```

## Waarschuwingen

Geen.

## Input

```json
{
  "monumenten": [
    {
      "code": "PRO",
      "naam": "Provinciaal monument"
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
      "code": "PMO",
      "naam": "Prijsopslag monumenten"
    }
  },
  "punten": 0.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "prijsopslag_monumenten__gemeentelijk_of_provinciaal_monument",
        "naam": "Gemeentelijk of provinciaal monument"
      },
      "opslagpercentage": 0.15
    }
  ],
  "opslagpercentage": 0.15
}
```
