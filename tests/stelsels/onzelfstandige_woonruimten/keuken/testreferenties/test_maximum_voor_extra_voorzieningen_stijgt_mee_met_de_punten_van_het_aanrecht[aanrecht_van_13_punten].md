# test_maximum_voor_extra_voorzieningen_stijgt_mee_met_de_punten_van_het_aanrecht[aanrecht_van_13_punten]

Het maximum voor extra voorzieningen stijgt mee met de punten voor een aanrecht langer dan 3 meter.

De toelichting onder A (rubriek 5.2) kent extra punten toe "tot maximaal
zeven punten indien het aanrecht op basis van rubriek 5.1. een lengte heeft
van 2 m of meer". De package volgt de tabel onder B, waarin het aanrecht 10
of 13 punten kan krijgen en de voorzieningen tot dat aantal meetellen.

Bron: wettekst, Bijlage I onder B, onderdeel 5.2: "Voorzieningen (tot
maximaal het aantal punten extra dat voor de lengte van het aanrecht is
verkregen)".

Bron: wettekst, Bijlage I onder B, onderdeel 5.1: "3 m en meer 10 punten"
en "5 m en meer (indien er minimaal 8 onzelfstandige woonruimten toegang en
gebruiksrecht hebben tot deze keuken) 13 punten".

Bron: wettekst, Bijlage I onder B, toelichting rubriek 5: "Ook geldt dat
een aanrecht tot 3 meter gewaardeerd kan worden tot 10 punten, in afwijking
van het maximum van 7 punten (tot 2 meter) onder de bijlage I, onder A."

Dit geval: de 12 punten voor koelkasten blijven onder de 13 punten van het aanrecht; bij een maximum van 10 punten zouden er 2 punten afgaan. De keuken wordt met 8 onzelfstandige woonruimten gedeeld.

## Rapport

```text
KEUKEN
  Gedeeld met 8 onzelfstandige woonruimten
    - Keuken
      - Lengte aanrecht                                            5500.00 mm     1.63 pt
      - Extra voorzieningen
        - Inbouw koelkast                                            12.00 st     1.50 pt
  Afronding op kwartpunten                                                        0.12 pt
                                                                                ------
  Totaal                                                                          3.25 pt
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
          "lengte": 5500.0
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
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 8
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
  "punten": 3.25,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "keuken__gedeeld_met_8_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 8 onzelfstandige woonruimten"
      }
    },
    {
      "criterium": {
        "id": "keuken__gedeeld_met_8_onzelfstandige_woonruimten__keuken",
        "naam": "Keuken",
        "bovenliggendeCriterium": {
          "id": "keuken__gedeeld_met_8_onzelfstandige_woonruimten"
        }
      }
    },
    {
      "aantal": 5500.0,
      "criterium": {
        "id": "keuken__gedeeld_met_8_onzelfstandige_woonruimten__keuken__lengte_aanrecht_aanrecht",
        "naam": "Lengte aanrecht",
        "bovenliggendeCriterium": {
          "id": "keuken__gedeeld_met_8_onzelfstandige_woonruimten__keuken"
        },
        "meeteenheid": {
          "code": "MIL",
          "naam": "Millimeter"
        }
      },
      "punten": 1.63
    },
    {
      "criterium": {
        "id": "keuken__gedeeld_met_8_onzelfstandige_woonruimten__keuken__extra_voorzieningen",
        "naam": "Extra voorzieningen",
        "bovenliggendeCriterium": {
          "id": "keuken__gedeeld_met_8_onzelfstandige_woonruimten__keuken"
        }
      }
    },
    {
      "aantal": 12.0,
      "criterium": {
        "id": "keuken__gedeeld_met_8_onzelfstandige_woonruimten__keuken__extra_voorzieningen__extra_voorziening_inbouw_koelkast",
        "naam": "Inbouw koelkast",
        "bovenliggendeCriterium": {
          "id": "keuken__gedeeld_met_8_onzelfstandige_woonruimten__keuken__extra_voorzieningen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 1.5
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
