# test_keuken_aangeleverd_als_overige_ruimte_is_een_vertrek

Een keuken die als overige ruimte is aangeleverd, wordt als vertrek gewaardeerd.

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.2.1.2
- wettekst, Bijlage I onder A, toelichting rubriek 1 (via Bijlage I onder B, toelichting, inleiding)

## Rapport

```text
OPPERVLAKTE VAN VERTREKKEN
  Privé
    - Keuken                                                         10.00 m²
                                                                                ------
  Totaal                                                                         10.00 pt
```

## Waarschuwingen

- UserWarning: Ruimte 'Keuken' (keuken) is aangeleverd als Overige ruimten maar wordt gewaardeerd als Vertrek.

## Input

```json
{
  "ruimten": [
    {
      "id": "keuken",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "KEU",
        "naam": "Keuken"
      },
      "naam": "Keuken",
      "oppervlakte": 10.0
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
      "code": "OVZ",
      "naam": "Oppervlakte van vertrekken"
    }
  },
  "punten": 10.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "oppervlakte_van_vertrekken__prive",
        "naam": "Privé"
      }
    },
    {
      "aantal": 10.0,
      "criterium": {
        "id": "oppervlakte_van_vertrekken__prive__keuken",
        "naam": "Keuken",
        "bovenliggendeCriterium": {
          "id": "oppervlakte_van_vertrekken__prive"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    }
  ]
}
```
