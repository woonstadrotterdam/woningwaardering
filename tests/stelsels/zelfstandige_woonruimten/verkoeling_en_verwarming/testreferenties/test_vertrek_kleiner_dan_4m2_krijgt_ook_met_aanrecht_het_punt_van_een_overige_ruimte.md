# test_vertrek_kleiner_dan_4m2_krijgt_ook_met_aanrecht_het_punt_van_een_overige_ruimte

Een verwarmde ruimte die als vertrek is aangeleverd maar kleiner is dan 4 m², krijgt ook met een aanrecht alleen het punt van een overige ruimte.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 3: "Alleen vertrekken
die met oppervlaktepunten als vertrek zijn gewaardeerd, worden in dit kader
meegeteld." en "Per verwarmde overige ruimte en verkeersruimte wordt,
ongeacht de verwarmingswijze, een waardering van één punt toegepast".

Bron: implementatietoelichting zelfstandige woonruimten, 2.3.2: "wij lezen
dat als de eis dat de ruimte minimaal aan de voorwaarden van een vertrek
voldoet".

## Rapport

```text
VERKOELING EN VERWARMING
  Verwarmde overige en verkeersruimten
    - Overig vertrek                                                              1.00 pt
                                                                                ------
  Totaal                                                                          1.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "overig_vertrek",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "OVT",
        "naam": "Overig vertrek"
      },
      "naam": "Overig vertrek",
      "oppervlakte": 3.0,
      "bouwkundigeElementen": [
        {
          "id": "aanrecht",
          "naam": "Aanrecht",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "AAN",
            "naam": "Aanrecht"
          },
          "lengte": 1500.0
        }
      ],
      "verwarmd": true
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
      "code": "VKV",
      "naam": "Verkoeling en verwarming"
    }
  },
  "punten": 1.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten",
        "naam": "Verwarmde overige en verkeersruimten"
      }
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten__overig_vertrek",
        "naam": "Overig vertrek",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten"
        }
      },
      "punten": 1.0
    }
  ]
}
```
