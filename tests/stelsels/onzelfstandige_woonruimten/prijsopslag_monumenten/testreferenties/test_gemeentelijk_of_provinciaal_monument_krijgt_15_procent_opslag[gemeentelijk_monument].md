# test_gemeentelijk_of_provinciaal_monument_krijgt_15_procent_opslag[gemeentelijk_monument]

Een gemeentelijk of provinciaal monument krijgt 15% opslag op de maximale huurprijs.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.14.5; wettekst,
artikel 8a, derde lid.

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
      "code": "GEM",
      "naam": "Gemeentelijk monument"
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
