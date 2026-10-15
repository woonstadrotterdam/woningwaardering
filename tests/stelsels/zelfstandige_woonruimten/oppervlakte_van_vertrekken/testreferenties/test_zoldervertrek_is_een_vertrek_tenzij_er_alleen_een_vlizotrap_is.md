# test_zoldervertrek_is_een_vertrek_tenzij_er_alleen_een_vlizotrap_is

Een zoldervertrek is een vertrek, tenzij het alleen via een vlizotrap bereikbaar is.

Bron: implementatietoelichting zelfstandige woonruimten, 2.2.1.3;
implementatietoelichting zelfstandige woonruimten, 2.2.2.3; wettekst,
Bijlage I onder A, toelichting rubriek 1.

## Rapport

```text
OPPERVLAKTE VAN VERTREKKEN
  Zoldervertrek1                                                     10.00 m²
  Zoldervertrek2                                                     10.00 m²
                                                                    ------      ------
  Totaal                                                             20.00 m²    20.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "zoldervertrek1",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "ZVT",
        "naam": "Zoldervertrek"
      },
      "naam": "Zoldervertrek1",
      "oppervlakte": 10.0,
      "bouwkundigeElementen": [
        {
          "id": "trap",
          "naam": "Trap",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "TRA",
            "naam": "Trap"
          }
        }
      ]
    },
    {
      "id": "zoldervertrek2",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "ZVT",
        "naam": "Zoldervertrek"
      },
      "naam": "Zoldervertrek2",
      "oppervlakte": 10.0
    },
    {
      "id": "zoldervertrek3",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "ZVT",
        "naam": "Zoldervertrek"
      },
      "naam": "Zoldervertrek3",
      "oppervlakte": 10.0,
      "bouwkundigeElementen": [
        {
          "id": "vlizotrap",
          "naam": "Vlizotrap",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "VTR",
            "naam": "Vlizotrap"
          }
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
      "code": "OVZ",
      "naam": "Oppervlakte van vertrekken"
    }
  },
  "punten": 20.0,
  "woningwaarderingen": [
    {
      "aantal": 10.0,
      "criterium": {
        "id": "oppervlakte_van_vertrekken__zoldervertrek1",
        "naam": "Zoldervertrek1",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "aantal": 10.0,
      "criterium": {
        "id": "oppervlakte_van_vertrekken__zoldervertrek2",
        "naam": "Zoldervertrek2",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    }
  ]
}
```
