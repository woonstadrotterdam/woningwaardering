# test_overige_ruimte_moet_minimaal_2m2_groot_zijn

Een ruimte kleiner dan 2 m² wordt niet als overige ruimte gewaardeerd.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.2.2;
wettekst, Bijlage I onder A, toelichting rubriek 2 (via Bijlage I onder B,
toelichting, inleiding).

## Rapport

```text
OPPERVLAKTE VAN OVERIGE RUIMTEN
  Privé
    - Bijkeuken                                                       2.00 m²
                                                                                ------
  Totaal                                                                          1.50 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "toiletruimte",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "TOI",
        "naam": "Toiletruimte"
      },
      "naam": "Toiletruimte",
      "oppervlakte": 1.0
    },
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
      "oppervlakte": 2.0
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
  "punten": 1.5,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__prive",
        "naam": "Privé"
      }
    },
    {
      "aantal": 2.0,
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
