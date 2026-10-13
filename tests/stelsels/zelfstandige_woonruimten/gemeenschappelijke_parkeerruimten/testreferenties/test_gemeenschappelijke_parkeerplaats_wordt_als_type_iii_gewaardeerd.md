# test_gemeenschappelijke_parkeerplaats_wordt_als_type_iii_gewaardeerd

Een gemeenschappelijke parkeerplaats wordt als Type III gewaardeerd.

De package waarschuwt dat bij een gemeenschappelijke parkeerplek een
Type-detailsoort hoort.

Bron: implementatietoelichting zelfstandige woonruimten, 2.10.3: "Type III:
`Ruimtedetailsoort.parkeerplek_buiten_behorend_bij_complex` (`PBC`) en,
wanneer die gemeenschappelijk is, `Ruimtedetailsoort.parkeerplaats` (`PAR`).
Bij die laatste volgt een `UserWarning` dat een Type-detailsoort meer op
zijn plaats is: `PAR` legt het type niet vast."

Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
genereert de package een `UserWarning`."

Bron: wettekst, Bijlage I onder A, rubriek 10: "Type III Parkeerplek buiten
behorende tot het complex zonder dak 4 punten gedeeld door het aantal
adressen dat toegang en gebruiksrecht heeft."

## Rapport

```text
GEMEENSCHAPPELIJKE PARKEERRUIMTEN
  Gedeeld met 3 adressen
    - Parkeerplaats (Type III)                                        1.00 st     1.33 pt
  Afronding op kwartpunten                                                       -0.08 pt
                                                                                ------
  Totaal                                                                          1.25 pt
```

## Waarschuwingen

- UserWarning: Ruimte 'Parkeerplaats' (parkeerplaats) is een gemeenschappelijke Parkeerplaats (PAR). Gebruik Type I, II of III (Parkeerplek in inpandige afgesloten parkeergarage (PIP), Parkeerplek in uitpandige afgesloten parkeergarage (PUP), Parkeerplek buiten met dak behorend bij complex (PBD) of Parkeerplek buiten behorend bij complex (PBC)) voor een gemeenschappelijke parkeerplek: deze wordt nu gewaardeerd als Type III.

## Input

```json
{
  "ruimten": [
    {
      "id": "parkeerplaats",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "PAR",
        "naam": "Parkeerplaats"
      },
      "naam": "Parkeerplaats",
      "oppervlakte": 15.0,
      "gedeeldMetAantalAdressen": 3
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
  "punten": 1.25,
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
        "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_3_adressen__parkeerplaats_type_iii",
        "naam": "Parkeerplaats (Type III)",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_3_adressen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 1.33
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__afronding_op_kwartpunten",
        "naam": "Afronding op kwartpunten"
      },
      "punten": -0.08
    }
  ]
}
```
