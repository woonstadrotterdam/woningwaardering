# test_carport_gedeeld_met_onzelfstandige_woonruimten_op_hetzelfde_adres_wordt_als_type_ii_gewaardeerd

Een carport die alleen door onzelfstandige woonruimten op hetzelfde adres wordt gedeeld, wordt in deze rubriek als Type II gewaardeerd.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.10.2; wettekst,
Bijlage I onder A, toelichting rubriek 10 (via Bijlage I onder B,
toelichting, inleiding).

De punten van een parkeerplek worden na de verdeling over de adressen
gedeeld door het aantal onzelfstandige woonruimten op het adres.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.10.4; wettekst,
Bijlage I onder B, toelichting rubriek 10.

## Rapport

```text
GEMEENSCHAPPELIJKE PARKEERRUIMTEN
  Gedeeld met 2 onzelfstandige woonruimten
    - Carport (Type II)                                               1.00 st     3.00 pt
                                                                                ------
  Totaal                                                                          3.00 pt
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
      "gedeeldMetAantalAdressen": 1,
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
      "code": "GPA",
      "naam": "Gemeenschappelijke parkeerruimten"
    }
  },
  "punten": 3.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_2_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 2 onzelfstandige woonruimten"
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_2_onzelfstandige_woonruimten__carport_type_ii",
        "naam": "Carport (Type II)",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_2_onzelfstandige_woonruimten"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 3.0
    }
  ]
}
```
