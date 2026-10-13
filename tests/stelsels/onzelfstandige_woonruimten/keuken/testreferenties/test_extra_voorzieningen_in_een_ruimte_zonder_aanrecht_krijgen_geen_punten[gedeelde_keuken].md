# test_extra_voorzieningen_in_een_ruimte_zonder_aanrecht_krijgen_geen_punten[gedeelde_keuken]

Extra voorzieningen in een ruimte zonder aanrecht krijgen geen punten.

Bron: beleidsboek onzelfstandige woonruimten, 2.5.3: "Een ruimte die
beschikt over de basisvoorzieningen voor een keuken kan ook extra punten
voor voorzieningen in de keuken krijgen."

Dit geval: de keuken wordt met 2 onzelfstandige woonruimten gedeeld; de badkamer is privé.

## Rapport

```text
KEUKEN
  Gedeeld met 2 onzelfstandige woonruimten
    - Keuken
      - Lengte aanrecht                                            1000.00 mm     2.00 pt
                                                                                ------
  Totaal                                                                          2.00 pt
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
          "lengte": 1000.0
        }
      ],
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
    },
    {
      "id": "badkamer",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "BAD",
        "naam": "Badkamer"
      },
      "naam": "Badkamer",
      "oppervlakte": 10.0,
      "installaties": [
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
  "punten": 2.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "keuken__gedeeld_met_2_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 2 onzelfstandige woonruimten"
      }
    },
    {
      "criterium": {
        "id": "keuken__gedeeld_met_2_onzelfstandige_woonruimten__keuken",
        "naam": "Keuken",
        "bovenliggendeCriterium": {
          "id": "keuken__gedeeld_met_2_onzelfstandige_woonruimten"
        }
      }
    },
    {
      "aantal": 1000.0,
      "criterium": {
        "id": "keuken__gedeeld_met_2_onzelfstandige_woonruimten__keuken__lengte_aanrecht_aanrecht",
        "naam": "Lengte aanrecht",
        "bovenliggendeCriterium": {
          "id": "keuken__gedeeld_met_2_onzelfstandige_woonruimten__keuken"
        },
        "meeteenheid": {
          "code": "MIL",
          "naam": "Millimeter"
        }
      },
      "punten": 2.0
    }
  ]
}
```
