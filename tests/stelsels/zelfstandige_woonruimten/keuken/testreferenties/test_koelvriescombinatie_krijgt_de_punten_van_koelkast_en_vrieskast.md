# test_koelvriescombinatie_krijgt_de_punten_van_koelkast_en_vrieskast

Een inbouw koelvriescombinatie krijgt de punten van een koelkast en een vrieskast samen.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 5: "Wanneer een
object twee voorzieningen heeft, bijvoorbeeld een ingebouwde combi
magnetron/oven of een gecombineerde koel- en vrieskast, worden beide
voorzieningen in dit object gewaardeerd conform de rubriek."

Bron: wettekst, Bijlage I onder A, onderdeel 5.2: "Inbouw koelkast 1 punt"
en "Inbouw vrieskast 0,75 punt".

## Rapport

```text
KEUKEN
  Keuken
    - Lengte aanrecht                                              2500.00 mm     7.00 pt
    - Extra voorzieningen
      - Inbouw koelvriescombinatie                                    1.00 st     1.75 pt
                                                                                ------
  Totaal                                                                          8.75 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "keuken",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "KEU",
        "naam": "Keuken"
      },
      "naam": "Keuken",
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
          "lengte": 2500.0
        }
      ],
      "installaties": [
        {
          "code": "IKV",
          "naam": "Inbouw koelvriescombinatie"
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
  "punten": 8.75,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "keuken__keuken",
        "naam": "Keuken"
      }
    },
    {
      "aantal": 2500.0,
      "criterium": {
        "id": "keuken__keuken__lengte_aanrecht_aanrecht",
        "naam": "Lengte aanrecht",
        "bovenliggendeCriterium": {
          "id": "keuken__keuken"
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
        "id": "keuken__keuken__extra_voorzieningen",
        "naam": "Extra voorzieningen",
        "bovenliggendeCriterium": {
          "id": "keuken__keuken"
        }
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "keuken__keuken__extra_voorzieningen__extra_voorziening_inbouw_koelvriescombinatie",
        "naam": "Inbouw koelvriescombinatie",
        "bovenliggendeCriterium": {
          "id": "keuken__keuken__extra_voorzieningen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 1.75
    }
  ]
}
```
