# test_keuken_aangeleverd_als_gemeenschappelijke_ruimte_wordt_als_vertrek_gewaardeerd

Een keuken die als gemeenschappelijke ruimte is aangeleverd, wordt als vertrek gewaardeerd.

De package waarschuwt dat de aangeleverde ruimtesoort afwijkt van de
ruimtesoort waarmee de keuken is gewaardeerd.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 1: "In afwijking van
bovenstaande eisen is een ruimte die uitsluitend als keuken dient en een
badkamer of doucheruimte altijd een vertrek."

Bron: implementatietoelichting zelfstandige woonruimten, 2.2.1.2:
"Uitzonderingen: keuken, badkamer en doucheruimte zijn volgens het
beleidsboek altijd een vertrek, en zo waarderen wij die ook, los van het
meegegeven `Ruimtesoort`."

Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
genereert de package een `UserWarning`."

Als vertrek krijgt de keuken 1 punt per m² en 2 punten voor verwarming, elk
gedeeld door het aantal adressen.

Bron: wettekst, Bijlage I onder A, rubriek 9: "Gemeenschappelijke vertrek 1
punt per m² gedeeld door het aantal adressen dat toegang en gebruiksrecht
heeft."

Bron: wettekst, Bijlage I onder A, rubriek 3: "Verwarming per vertrek 2
punten".

Bron: wettekst, Bijlage I onder A, toelichting rubriek 9: "Deel dit aantal
punten door het aantal adressen dat toegang heeft tot de gemeenschappelijke
binnenruimten."

Het aanrecht van 2 meter telt ook in een ruimte met deze ruimtesoort mee
voor de keuken.

Bron: implementatietoelichting zelfstandige woonruimten, 2.5.1: "Rubriek 5
stelt eisen aan de keuken zelf, niet aan de ruimte waarin die ligt. Een
aanrecht telt daarom in elke ruimte mee."

Bron: wettekst, Bijlage I onder A, onderdeel 5.1: "2 m en meer 7 punten".

## Rapport

```text
GEMEENSCHAPPELIJKE VERTREKKEN, OVERIGE RUIMTEN EN VOORZIENINGEN
  Gedeeld met 4 adressen
    - Oppervlakte van vertrekken                                                  2.50 pt
      - Keuken                                                       10.00 m²
    - Verkoeling en verwarming
      - Verwarmde vertrekken
        - Keuken                                                                  0.50 pt
    - Keuken
      - Keuken
        - Lengte aanrecht                                          2000.00 mm     1.75 pt
                                                                                ------
  Totaal                                                                          4.75 pt
```

## Waarschuwingen

- UserWarning: Ruimte 'Keuken' (keuken) is aangeleverd als Gemeenschappelijke ruimten en voorzieningen maar wordt gewaardeerd als Vertrek.
- UserWarning: Ruimte 'Keuken' (keuken) is aangeleverd als Gemeenschappelijke ruimten en voorzieningen maar wordt gewaardeerd als Vertrek.
- UserWarning: Ruimte 'Keuken' (keuken) is aangeleverd als Gemeenschappelijke ruimten en voorzieningen maar wordt gewaardeerd als Vertrek.
- UserWarning: Ruimte 'Keuken' (keuken) is aangeleverd als Gemeenschappelijke ruimten en voorzieningen maar wordt gewaardeerd als Vertrek.

## Input

```json
{
  "ruimten": [
    {
      "id": "keuken",
      "soort": {
        "code": "GEM",
        "naam": "Gemeenschappelijke ruimten en voorzieningen"
      },
      "detailSoort": {
        "code": "KEU",
        "naam": "Keuken"
      },
      "naam": "Keuken",
      "oppervlakte": 10.0,
      "gedeeldMetAantalAdressen": 4,
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
          "lengte": 2000.0
        }
      ],
      "verwarmd": true
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
      "code": "GVR",
      "naam": "Gemeenschappelijke vertrekken, overige ruimten en voorzieningen"
    }
  },
  "punten": 4.75,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_4_adressen",
        "naam": "Gedeeld met 4 adressen"
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_4_adressen__oppervlakte_van_vertrekken",
        "naam": "Oppervlakte van vertrekken",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_4_adressen"
        }
      },
      "punten": 2.5
    },
    {
      "aantal": 10.0,
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_4_adressen__oppervlakte_van_vertrekken__keuken",
        "naam": "Keuken",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_4_adressen__oppervlakte_van_vertrekken"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_4_adressen__verkoeling_en_verwarming",
        "naam": "Verkoeling en verwarming",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_4_adressen"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_4_adressen__verkoeling_en_verwarming__verwarmde_vertrekken",
        "naam": "Verwarmde vertrekken",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_4_adressen__verkoeling_en_verwarming"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_4_adressen__verkoeling_en_verwarming__verwarmde_vertrekken__keuken",
        "naam": "Keuken",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_4_adressen__verkoeling_en_verwarming__verwarmde_vertrekken"
        }
      },
      "punten": 0.5
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_4_adressen__keuken",
        "naam": "Keuken",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_4_adressen"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_4_adressen__keuken__keuken",
        "naam": "Keuken",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_4_adressen__keuken"
        }
      }
    },
    {
      "aantal": 2000.0,
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_4_adressen__keuken__keuken__lengte_aanrecht_aanrecht",
        "naam": "Lengte aanrecht",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_4_adressen__keuken__keuken"
        },
        "meeteenheid": {
          "code": "MIL",
          "naam": "Millimeter"
        }
      },
      "punten": 1.75
    }
  ]
}
```
