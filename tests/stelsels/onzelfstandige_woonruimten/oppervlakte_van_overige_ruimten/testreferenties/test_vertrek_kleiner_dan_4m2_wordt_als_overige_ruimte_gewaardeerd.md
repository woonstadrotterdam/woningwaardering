# test_vertrek_kleiner_dan_4m2_wordt_als_overige_ruimte_gewaardeerd

Een ruimte die als vertrek is aangeleverd maar kleiner is dan 4 m², wordt als overige ruimte gewaardeerd.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 2: een overige ruimte
is een ruimte waarvoor geldt "De ruimte voldoet niet aan de eisen voor een
vertrek (zie vaste toelichting onder 1) of een verkeersruimte".

Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
overeenkomstige toepassing is."

Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.2.2: "Een
ruimte met `Ruimtesoort` `vertrek` komt in aanmerking voor waardering in de
rubriek 'Oppervlakte van overige ruimten' als de oppervlakte minder dan 4 m²
en minimaal 2 m² is."

## Rapport

```text
OPPERVLAKTE VAN OVERIGE RUIMTEN
  Privé
    - Slaapkamer1                                                     3.99 m²
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
      "id": "slaapkamer1",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer1",
      "oppervlakte": 3.99
    },
    {
      "id": "slaapkamer2",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer2",
      "oppervlakte": 4.0
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
  "punten": 3.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__prive",
        "naam": "Privé"
      }
    },
    {
      "aantal": 3.99,
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__prive__slaapkamer1",
        "naam": "Slaapkamer1",
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
