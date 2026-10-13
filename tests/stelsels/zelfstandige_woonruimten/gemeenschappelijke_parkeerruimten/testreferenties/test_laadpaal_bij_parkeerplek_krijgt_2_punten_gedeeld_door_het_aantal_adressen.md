# test_laadpaal_bij_parkeerplek_krijgt_2_punten_gedeeld_door_het_aantal_adressen

Een laadpaal bij een parkeerplek krijgt 2 punten extra, gedeeld door het aantal adressen dat toegang en gebruiksrecht heeft.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 10: "Indien er sprake
is van een laadpaal voor exclusief gebruik door de bewoners, geldt twee
punten extra per parkeerplek met laadpaal." en "Daarna wordt dit
puntentotaal gedeeld door het aantal adressen dat gebruik kan maken van de
parkeerplek(ken)."

Bron: beleidsboek zelfstandige woonruimten, 2.10.5: "Als de parkeerplek
beschikt over een laadpaal voor elektrisch rijden, die exclusief is voor
gebruik door bewoners, dan worden 2 extra punten toegekend, gedeeld door het
aantal adressen dat toegang en gebruiksrecht heeft."

## Rapport

```text
GEMEENSCHAPPELIJKE PARKEERRUIMTEN
  Gedeeld met 3 adressen
    - Carport (Type II)                                               1.00 st     2.00 pt
    - Laadpaal                                                        1.00 st     0.67 pt
  Afronding op kwartpunten                                                        0.08 pt
                                                                                ------
  Totaal                                                                          2.75 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "carport",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "CAR",
        "naam": "Carport"
      },
      "naam": "Carport",
      "oppervlakte": 15.0,
      "gedeeldMetAantalAdressen": 3,
      "bouwkundigeElementen": [
        {
          "id": "laadpaal",
          "naam": "Laadpaal",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "LAA",
            "naam": "Laadpaal"
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
      "code": "GPA",
      "naam": "Gemeenschappelijke parkeerruimten"
    }
  },
  "punten": 2.75,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_3_adressen",
        "naam": "Gedeeld met 3 adressen"
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_3_adressen__carport_type_ii",
        "naam": "Carport (Type II)",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_3_adressen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 2.0
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_3_adressen__carport_type_ii_laadpaal",
        "naam": "Laadpaal",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_3_adressen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.67
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__afronding_op_kwartpunten",
        "naam": "Afronding op kwartpunten"
      },
      "punten": 0.08
    }
  ]
}
```
