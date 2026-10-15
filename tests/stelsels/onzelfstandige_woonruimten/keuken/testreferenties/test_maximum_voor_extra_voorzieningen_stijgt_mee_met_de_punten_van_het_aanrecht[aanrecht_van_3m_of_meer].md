# test_maximum_voor_extra_voorzieningen_stijgt_mee_met_de_punten_van_het_aanrecht[aanrecht_van_3m_of_meer]

Het maximum voor extra voorzieningen stijgt mee met de punten voor een aanrecht van 3 meter of meer.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.5.3; wettekst,
Bijlage I onder B, onderdeel 5.2; wettekst, Bijlage I onder B, toelichting
rubriek 5.

Een aanrecht van 3 meter of meer krijgt 10 punten, en een aanrecht van 5
meter of meer 13 punten als minimaal 8 onzelfstandige woonruimten toegang en
gebruiksrecht hebben tot de keuken.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.5.2; wettekst,
Bijlage I onder B, onderdeel 5.1.

De punten worden gedeeld door het aantal onzelfstandige woonruimten met
toegang en gebruiksrecht.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.5.2;
implementatietoelichting onzelfstandige woonruimten, 2.5.3; wettekst,
Bijlage I onder B, onderdeel 5.1; wettekst, Bijlage I onder B, onderdeel
5.2.

Dit geval: de 8 punten voor koelkasten blijven onder de 10 punten van het aanrecht; bij een maximum van 7 punten zou er 1 punt afgaan. De keuken wordt met 2 onzelfstandige woonruimten gedeeld.

## Rapport

```text
KEUKEN
  Gedeeld met 2 onzelfstandige woonruimten
    - Keuken
      - Lengte aanrecht                                            3500.00 mm     5.00 pt
      - Extra voorzieningen
        - Inbouw koelkast                                             8.00 st     4.00 pt
                                                                                ------
  Totaal                                                                          9.00 pt
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
  "punten": 9.0,
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
      "aantal": 3500.0,
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
      "punten": 5.0
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
      "aantal": 8.0,
      "criterium": {
        "id": "keuken__gedeeld_met_2_onzelfstandige_woonruimten__keuken__extra_voorzieningen__extra_voorziening_inbouw_koelkast",
        "naam": "Inbouw koelkast",
        "bovenliggendeCriterium": {
          "id": "keuken__gedeeld_met_2_onzelfstandige_woonruimten__keuken__extra_voorzieningen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 4.0
    }
  ]
}
```
