# test_gemeenschappelijke_carport_wordt_als_type_ii_gewaardeerd

Een gemeenschappelijke carport wordt als Type II gewaardeerd.

Bron: implementatietoelichting zelfstandige woonruimten, 2.10.3; wettekst,
Bijlage I onder A, onderdeel 10.

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
