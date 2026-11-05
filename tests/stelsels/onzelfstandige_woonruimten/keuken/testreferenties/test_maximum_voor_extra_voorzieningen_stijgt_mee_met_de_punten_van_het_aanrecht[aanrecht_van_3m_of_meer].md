# test_maximum_voor_extra_voorzieningen_stijgt_mee_met_de_punten_van_het_aanrecht[aanrecht_van_3m_of_meer]

Het maximum voor extra voorzieningen stijgt mee met de punten voor een aanrecht van 3 meter of meer.

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.5.3
- wettekst, Bijlage I onder B, onderdeel 5.2

Een aanrecht van 3 meter of meer krijgt 10 punten, en vanaf 5 meter bij minimaal 8
onzelfstandige woonruimten 13 punten, gedeeld door het aantal woonruimten.

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.5.2
- wettekst, Bijlage I onder B, onderdeel 5.1

Dit geval: de 8 punten voor koelkasten blijven onder de 10 punten van het aanrecht; bij een maximum van 7 punten zou er 1 punt afgaan.

## Rapport

```text
KEUKEN
  Privé
    - Keuken
      - Lengte aanrecht                                            3500.00 mm    10.00 pt
      - Extra voorzieningen
        - Inbouw koelkast                                             8.00 st     8.00 pt
                                                                                ------
  Totaal                                                                         18.00 pt
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
          "lengte": 3500.0
        }
      ],
      "installaties": [
        {
          "code": "IKO",
          "naam": "Inbouw koelkast"
        },
        {
          "code": "IKO",
          "naam": "Inbouw koelkast"
        },
        {
          "code": "IKO",
          "naam": "Inbouw koelkast"
        },
        {
          "code": "IKO",
          "naam": "Inbouw koelkast"
        },
        {
          "code": "IKO",
          "naam": "Inbouw koelkast"
        },
        {
          "code": "IKO",
          "naam": "Inbouw koelkast"
        },
        {
          "code": "IKO",
          "naam": "Inbouw koelkast"
        },
        {
          "code": "IKO",
          "naam": "Inbouw koelkast"
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
      "code": "ONZ",
      "naam": "Onzelfstandige woonruimten"
    },
    "stelselgroep": {
      "code": "KEU",
      "naam": "Keuken"
    }
  },
  "punten": 18.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "keuken__prive",
        "naam": "Privé"
      }
    },
    {
      "criterium": {
        "id": "keuken__prive__keuken",
        "naam": "Keuken",
        "bovenliggendeCriterium": {
          "id": "keuken__prive"
        }
      }
    },
    {
      "aantal": 3500.0,
      "criterium": {
        "id": "keuken__prive__keuken__lengte_aanrecht_aanrecht",
        "naam": "Lengte aanrecht",
        "bovenliggendeCriterium": {
          "id": "keuken__prive__keuken"
        },
        "meeteenheid": {
          "code": "MIL",
          "naam": "Millimeter"
        }
      },
      "punten": 10.0
    },
    {
      "criterium": {
        "id": "keuken__prive__keuken__extra_voorzieningen",
        "naam": "Extra voorzieningen",
        "bovenliggendeCriterium": {
          "id": "keuken__prive__keuken"
        }
      }
    },
    {
      "aantal": 8.0,
      "criterium": {
        "id": "keuken__prive__keuken__extra_voorzieningen__extra_voorziening_inbouw_koelkast",
        "naam": "Inbouw koelkast",
        "bovenliggendeCriterium": {
          "id": "keuken__prive__keuken__extra_voorzieningen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 8.0
    }
  ]
}
```
