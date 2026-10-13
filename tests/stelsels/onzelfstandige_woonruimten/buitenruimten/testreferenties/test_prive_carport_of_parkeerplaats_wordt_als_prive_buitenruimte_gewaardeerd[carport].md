# test_prive_carport_of_parkeerplaats_wordt_als_prive_buitenruimte_gewaardeerd[carport]

Een privé-carport of privé-parkeerplaats wordt als privé-buitenruimte gewaardeerd.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 8: "Wanneer zich
binnen de privé-buitenruimte een parkeerplek bevindt, geldt de parkeerplek
en de weg daar naartoe als privé-buitenruimte."

Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
overeenkomstige toepassing is."

Bron: implementatietoelichting onzelfstandige woonruimten, 2.8.3: "Een
`carport` of `parkeerplaats` is een VERA-buitenruimte: privé wordt die hier
gewaardeerd, gemeenschappelijk in rubriek 10".

Bron: wettekst, Bijlage I onder B, rubriek 8: "Privé buitenruimte(n)", "2
punten + 0,35 punt per m²".

## Rapport

```text
BUITENRUIMTEN
  Privé
    - Carport                                                        12.00 m²     4.20 pt
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
        "id": "buitenruimten__prive__carport",
        "naam": "Carport",
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
