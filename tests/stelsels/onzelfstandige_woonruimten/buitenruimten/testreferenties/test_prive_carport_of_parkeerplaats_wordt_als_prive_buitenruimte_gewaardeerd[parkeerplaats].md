# test_prive_carport_of_parkeerplaats_wordt_als_prive_buitenruimte_gewaardeerd[parkeerplaats]

Een privé-carport of privé-parkeerplaats wordt als privé-buitenruimte gewaardeerd.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.8.1;
implementatietoelichting onzelfstandige woonruimten, 2.8.3; wettekst,
Bijlage I onder A, toelichting rubriek 8 (via Bijlage I onder B,
toelichting, inleiding).

## Rapport

```text
BUITENRUIMTEN
  Privé
    - Parkeerplaats                                                  12.00 m²     4.20 pt
    - Privé buitenruimten aanwezig                                                2.00 pt
  Afronding op kwartpunten                                                        0.05 pt
                                                                                ------
  Totaal                                                                          6.25 pt
```

## Waarschuwingen

Geen.

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
      "oppervlakte": 12.0
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
      "code": "BUI",
      "naam": "Buitenruimten"
    }
  },
  "punten": 6.25,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "buitenruimten__prive",
        "naam": "Privé"
      }
    },
    {
      "aantal": 12.0,
      "criterium": {
        "id": "buitenruimten__prive__parkeerplaats",
        "naam": "Parkeerplaats",
        "bovenliggendeCriterium": {
          "id": "buitenruimten__prive"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": 4.2
    },
    {
      "criterium": {
        "id": "buitenruimten__prive__prive_buitenruimten_aanwezig",
        "naam": "Privé buitenruimten aanwezig",
        "bovenliggendeCriterium": {
          "id": "buitenruimten__prive"
        }
      },
      "punten": 2.0
    },
    {
      "criterium": {
        "id": "buitenruimten__afronding_op_kwartpunten",
        "naam": "Afronding op kwartpunten"
      },
      "punten": 0.05
    }
  ]
}
```
