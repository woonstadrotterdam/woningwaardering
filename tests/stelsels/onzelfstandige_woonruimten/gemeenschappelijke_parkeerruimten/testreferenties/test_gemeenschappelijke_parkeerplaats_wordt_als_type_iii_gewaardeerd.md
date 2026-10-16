# test_gemeenschappelijke_parkeerplaats_wordt_als_type_iii_gewaardeerd

Een gemeenschappelijke parkeerplaats wordt als Type III gewaardeerd.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.10.3.

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
