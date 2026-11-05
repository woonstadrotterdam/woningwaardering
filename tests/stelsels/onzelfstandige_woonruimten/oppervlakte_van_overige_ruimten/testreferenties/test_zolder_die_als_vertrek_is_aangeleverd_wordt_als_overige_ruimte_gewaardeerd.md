# test_zolder_die_als_vertrek_is_aangeleverd_wordt_als_overige_ruimte_gewaardeerd

Een zolder die als vertrek is aangeleverd, wordt als overige ruimte gewaardeerd.

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.2.2.3
- wettekst, Bijlage I onder A, toelichting rubriek 2 (via Bijlage I onder B, toelichting, inleiding)

## Rapport

```text
OPPERVLAKTE VAN OVERIGE RUIMTEN
  Privé
    - Zolder                                                         10.00 m²
                                                                                ------
  Totaal                                                                          7.50 pt
```

## Waarschuwingen

- UserWarning: Ruimte 'Zolder' (zolder) is aangeleverd als Vertrek maar wordt gewaardeerd als Overige ruimten.
- UserWarning: Ruimte 'Zolder' (zolder) is aangeleverd als Vertrek maar wordt gewaardeerd als Overige ruimten.

## Input

```json
{
  "ruimten": [
    {
      "id": "zolder",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "ZOL",
        "naam": "Zolder"
      },
      "naam": "Zolder",
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
      "code": "OOZ",
      "naam": "Oppervlakte van overige ruimten"
    }
  },
  "punten": 7.5,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__prive",
        "naam": "Privé"
      }
    },
    {
      "aantal": 10.0,
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__prive__zolder",
        "naam": "Zolder",
        "bovenliggendeCriterium": {
          "id": "oppervlakte_van_overige_ruimten__prive"
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
