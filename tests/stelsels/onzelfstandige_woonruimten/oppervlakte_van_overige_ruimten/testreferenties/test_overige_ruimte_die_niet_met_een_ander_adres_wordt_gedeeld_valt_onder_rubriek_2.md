# test_overige_ruimte_die_niet_met_een_ander_adres_wordt_gedeeld_valt_onder_rubriek_2

Een overige ruimte die niet met een ander adres wordt gedeeld, wordt in rubriek 2 gewaardeerd.

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.9.1
- wettekst, Bijlage I onder A, toelichting rubriek 9 (via Bijlage I onder B, toelichting, inleiding)

## Rapport

```text
OPPERVLAKTE VAN OVERIGE RUIMTEN
  Privé
    - Bijkeuken                                                       8.00 m²
                                                                                ------
  Totaal                                                                          6.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "bijkeuken",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "BIJ",
        "naam": "Bijkeuken"
      },
      "naam": "Bijkeuken",
      "oppervlakte": 8.0,
      "gedeeldMetAantalAdressen": 1
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
  "punten": 6.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__prive",
        "naam": "Privé"
      }
    },
    {
      "aantal": 8.0,
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__prive__bijkeuken",
        "naam": "Bijkeuken",
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
