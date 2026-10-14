# test_gemeenschappelijke_carport_wordt_als_type_ii_gewaardeerd

Een gemeenschappelijke carport wordt als Type II gewaardeerd.

De carport wordt met 3 adressen gedeeld; op het eigen adres heeft één
onzelfstandige woonruimte toegang.

Bron: beleidsboek onzelfstandige woonruimten, 2.10.3: "Type II: een
parkeerplek buiten behorende tot het complex of de woning met dak
(hieronder telt een carport)".

Bron: implementatietoelichting onzelfstandige woonruimten, 2.10.3: "Type II:
`Ruimtedetailsoort.parkeerplek_buiten_met_dak_behorend_bij_complex` (`PBD`)
en, wanneer die gemeenschappelijk is, `Ruimtedetailsoort.carport` (`CAR`)."

Bron: wettekst, Bijlage I onder B, rubriek 10: "Type II Parkeerplek buiten
behorende tot het complex met dak 6 punten gedeeld door het aantal adressen
dat toegang en gebruiksrecht heeft, en daarna gedeeld door het aantal
onzelfstandige woonruimten op dat adres".

## Rapport

```text
GEMEENSCHAPPELIJKE PARKEERRUIMTEN
  Gedeeld met 3 adressen
    - Carport (Type II)                                               1.00 st     2.00 pt
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
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 1
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
      "code": "GPA",
      "naam": "Gemeenschappelijke parkeerruimten"
    }
  },
  "punten": 2.0,
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
    }
  ]
}
```
