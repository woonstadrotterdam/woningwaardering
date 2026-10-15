# test_koelvriescombinatie_krijgt_de_punten_van_koelkast_en_vrieskast

Een inbouw koelvriescombinatie krijgt de punten van een koelkast en een vrieskast samen.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.5.4; wettekst,
Bijlage I onder A, toelichting rubriek 5 (via Bijlage I onder B,
toelichting, inleiding); wettekst, Bijlage I onder B, onderdeel 5.2.

## Rapport

```text
KEUKEN
  Gedeeld met 2 onzelfstandige woonruimten
    - Keuken
      - Lengte aanrecht                                            2500.00 mm     3.50 pt
      - Extra voorzieningen
        - Inbouw koelvriescombinatie                                  1.00 st     0.88 pt
  Afronding op kwartpunten                                                        0.12 pt
                                                                                ------
  Totaal                                                                          4.50 pt
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
      ],
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
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
  "punten": 4.5,
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
      "aantal": 2500.0,
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
      "punten": 3.5
    },
    {
      "criterium": {
        "id": "keuken__gedeeld_met_2_onzelfstandige_woonruimten__keuken__extra_voorzieningen",
        "naam": "Extra voorzieningen",
        "bovenliggendeCriterium": {
          "id": "keuken__gedeeld_met_2_onzelfstandige_woonruimten__keuken"
        }
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "keuken__gedeeld_met_2_onzelfstandige_woonruimten__keuken__extra_voorzieningen__extra_voorziening_inbouw_koelvriescombinatie",
        "naam": "Inbouw koelvriescombinatie",
        "bovenliggendeCriterium": {
          "id": "keuken__gedeeld_met_2_onzelfstandige_woonruimten__keuken__extra_voorzieningen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.88
    },
    {
      "criterium": {
        "id": "keuken__afronding_op_kwartpunten",
        "naam": "Afronding op kwartpunten"
      },
      "punten": 0.12
    }
  ]
}
```
