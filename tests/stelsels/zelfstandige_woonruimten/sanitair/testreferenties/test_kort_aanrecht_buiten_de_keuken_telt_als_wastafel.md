# test_kort_aanrecht_buiten_de_keuken_telt_als_wastafel

Een aanrecht korter dan 1 meter buiten de keuken telt als wastafel.

Bron: implementatietoelichting zelfstandige woonruimten, 2.5.2.

## Rapport

```text
SANITAIR
  Bijkeuken
    - Wastafel (spoelbak in aanrecht < 1m)                            1.00 st     1.00 pt
                                                                                ------
  Totaal                                                                          1.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "bijkeuken",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "BIJ",
        "naam": "Bijkeuken"
      },
      "naam": "Bijkeuken",
      "oppervlakte": 10.0,
      "bouwkundigeElementen": [
        {
          "id": "aanrecht",
          "naam": "Aanrecht",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "AAN",
            "naam": "Aanrecht"
          },
          "lengte": 800.0
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
      "code": "SAN",
      "naam": "Sanitair"
    }
  },
  "punten": 1.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "sanitair__bijkeuken",
        "naam": "Bijkeuken"
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__bijkeuken__spoelbak_in_aanrecht",
        "naam": "Wastafel (spoelbak in aanrecht < 1m)",
        "bovenliggendeCriterium": {
          "id": "sanitair__bijkeuken"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 1.0
    }
  ]
}
```
