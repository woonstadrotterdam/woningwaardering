# test_overige_ruimte_met_aanrecht_telt_als_keuken

Een overige ruimte met een aanrecht telt voor de keuken mee.

Bron: implementatietoelichting zelfstandige woonruimten, 2.5.1.

## Rapport

```text
KEUKEN
  Bijkeuken
    - Lengte aanrecht                                              2200.00 mm     7.00 pt
  Garage
    - Lengte aanrecht                                              1500.00 mm     4.00 pt
                                                                                ------
  Totaal                                                                         11.00 pt
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
          "lengte": 2200.0
        }
      ]
    },
    {
      "id": "garage",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "GAR",
        "naam": "Garage"
      },
      "naam": "Garage",
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
          "lengte": 1500.0
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
      "code": "KEU",
      "naam": "Keuken"
    }
  },
  "punten": 11.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "keuken__bijkeuken",
        "naam": "Bijkeuken"
      }
    },
    {
      "aantal": 2200.0,
      "criterium": {
        "id": "keuken__bijkeuken__lengte_aanrecht_aanrecht",
        "naam": "Lengte aanrecht",
        "bovenliggendeCriterium": {
          "id": "keuken__bijkeuken"
        },
        "meeteenheid": {
          "code": "MIL",
          "naam": "Millimeter"
        }
      },
      "punten": 7.0
    },
    {
      "criterium": {
        "id": "keuken__garage",
        "naam": "Garage"
      }
    },
    {
      "aantal": 1500.0,
      "criterium": {
        "id": "keuken__garage__lengte_aanrecht_aanrecht",
        "naam": "Lengte aanrecht",
        "bovenliggendeCriterium": {
          "id": "keuken__garage"
        },
        "meeteenheid": {
          "code": "MIL",
          "naam": "Millimeter"
        }
      },
      "punten": 4.0
    }
  ]
}
```
