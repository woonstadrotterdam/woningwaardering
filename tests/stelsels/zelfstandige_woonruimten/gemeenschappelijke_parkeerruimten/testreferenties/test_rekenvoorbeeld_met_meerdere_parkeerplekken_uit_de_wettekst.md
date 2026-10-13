# test_rekenvoorbeeld_met_meerdere_parkeerplekken_uit_de_wettekst

Het rekenvoorbeeld uit de wettekst: tien adressen die vijf Type II-parkeerplekken met laadpaal en twee Type III-parkeerplekken delen, krijgen elk 4,75 punten.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 10: "Tien adressen
delen vijf type II-parkeerplekken met laadpaal en twee type
III-parkeerplekken zonder laadpaal.", "Vijf parkeerplekken type II (zes
punten) + elke een laadpaal (twee punten) en twee parkeerplekken type III
(vier punten) = 5 x (6+2)+ 2 x 4 = 48 punten.", "48 / 10 adressen = 4,8
punten per adres." en "Afronden geschiedt op een kwart punt per adres op
4,75 punten."

De vijf Type II-parkeerplekken zijn een gemeenschappelijke carport met
`aantal` 5 en één laadpaal. De package telt die laadpaal voor elke
parkeerplek van de ruimte.

Bron: implementatietoelichting zelfstandige woonruimten, 2.10.4: "Hierdoor
is het mogelijk om aan te geven tot hoeveel van elk parkeerplektype de
eenheid toegang heeft zonder dat elk parkeervak van een parkeergarage of
parkeerterrein meegegeven dient te worden. Wanneer een laadpaal als
bouwkundig element wordt meegegeven, wordt deze bij de ruimte meegeteld voor
de berekening van de punten, waarbij het aantal wordt bepaald door
`Eenhedenruimte.aantal`."

Bron: implementatietoelichting zelfstandige woonruimten, 2.10.3: "Type II:
`Ruimtedetailsoort.parkeerplek_buiten_met_dak_behorend_bij_complex` (`PBD`)
en, wanneer die gemeenschappelijk is, `Ruimtedetailsoort.carport` (`CAR`)."

## Rapport

```text
GEMEENSCHAPPELIJKE PARKEERRUIMTEN
  Gedeeld met 10 adressen
    - Carport (Type II)                                               5.00 st     3.00 pt
    - Laadpaal                                                        5.00 st     1.00 pt
    - Parkeerplek buiten behorend bij complex (Type III)              2.00 st     0.80 pt
  Afronding op kwartpunten                                                       -0.05 pt
                                                                                ------
  Totaal                                                                          4.75 pt
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
      "oppervlakte": 12.0,
      "gedeeldMetAantalAdressen": 10,
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
      ],
      "aantal": 5
    },
    {
      "id": "parkeerplek_buiten_behorend_bij_complex",
      "soort": {
        "code": "GEM",
        "naam": "Gemeenschappelijke ruimten en voorzieningen"
      },
      "detailSoort": {
        "code": "PBC",
        "naam": "Parkeerplek buiten behorend bij complex"
      },
      "naam": "Parkeerplek buiten behorend bij complex",
      "oppervlakte": 12.0,
      "gedeeldMetAantalAdressen": 10,
      "aantal": 2
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
  "punten": 4.75,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_10_adressen",
        "naam": "Gedeeld met 10 adressen"
      }
    },
    {
      "aantal": 5.0,
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_10_adressen__carport_type_ii",
        "naam": "Carport (Type II)",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_10_adressen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 3.0
    },
    {
      "aantal": 5.0,
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_10_adressen__carport_type_ii_laadpaal",
        "naam": "Laadpaal",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_10_adressen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 1.0
    },
    {
      "aantal": 2.0,
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_10_adressen__parkeerplek_buiten_behorend_bij_complex_type_iii",
        "naam": "Parkeerplek buiten behorend bij complex (Type III)",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_10_adressen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.8
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__afronding_op_kwartpunten",
        "naam": "Afronding op kwartpunten"
      },
      "punten": -0.05
    }
  ]
}
```
