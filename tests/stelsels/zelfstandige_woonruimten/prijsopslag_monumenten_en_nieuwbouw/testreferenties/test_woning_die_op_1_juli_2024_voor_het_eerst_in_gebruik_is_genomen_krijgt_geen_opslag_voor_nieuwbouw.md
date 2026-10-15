# test_woning_die_op_1_juli_2024_voor_het_eerst_in_gebruik_is_genomen_krijgt_geen_opslag_voor_nieuwbouw

Een woning die op 1 juli 2024 voor het eerst in gebruik is genomen, krijgt geen opslag voor nieuwbouw.

Bron: implementatietoelichting zelfstandige woonruimten, 2.13.7.1; wettekst,
artikel 8a, vierde lid.

## Rapport

Geen waarderingen voor Prijsopslag monumenten en nieuwbouw.

## Waarschuwingen

Geen.

## Input

```json
{
  "id": "meergezinswoning_van_79_m2",
  "beginBouwdatum": "2023-01-01",
  "inExploitatiedatum": "2024-07-01",
  "energieprestaties": [
    {
      "soort": {
        "code": "EI",
        "naam": "Energie-index"
      },
      "status": {
        "code": "DEF",
        "naam": "Definitief"
      },
      "begindatum": "2019-07-03",
      "einddatum": "2029-07-03",
      "label": {
        "code": "B",
        "naam": "B"
      },
      "waarde": "1.24"
    }
  ],
  "gebruiksoppervlakte": 79,
  "monumenten": [],
  "panden": [
    {
      "soort": {
        "code": "MGW",
        "naam": "Meergezinswoning"
      }
    }
  ],
  "ruimten": [
    {
      "id": "balkon",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "BAL",
        "naam": "Balkon"
      },
      "naam": "Balkon",
      "breedte": 3080.0,
      "hoogte": 2440.0,
      "lengte": 1680.0,
      "oppervlakte": 4.61588
    },
    {
      "id": "meterruimte",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "MET",
        "naam": "Meterruimte"
      },
      "naam": "Meterruimte",
      "oppervlakte": 0.27125
    },
    {
      "id": "woonkamer",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "WOO",
        "naam": "Woonkamer"
      },
      "naam": "Woonkamer",
      "oppervlakte": 30.1218,
      "verwarmd": true
    },
    {
      "id": "entree",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "ENT",
        "naam": "Entree"
      },
      "naam": "Entree",
      "oppervlakte": 7.14345,
      "verwarmd": true
    },
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
      "oppervlakte": 11.718,
      "verwarmd": true
    },
    {
      "id": "berging1",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "BER",
        "naam": "Berging"
      },
      "naam": "Berging1",
      "oppervlakte": 5.09507
    },
    {
      "id": "badkamer",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "BAD",
        "naam": "Badkamer"
      },
      "naam": "Badkamer",
      "oppervlakte": 4.644,
      "verwarmd": true
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
      "oppervlakte": 9.2092,
      "verwarmd": true
    },
    {
      "id": "keuken",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "KEU",
        "naam": "Keuken"
      },
      "naam": "Keuken",
      "oppervlakte": 5.76,
      "verwarmd": true
    },
    {
      "id": "berging2",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "BER",
        "naam": "Berging"
      },
      "naam": "Berging2",
      "oppervlakte": 1.8836
    },
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
      "oppervlakte": 1.28113
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
      "code": "PMN",
      "naam": "Prijsopslag monumenten en nieuwbouw"
    }
  },
  "punten": 0.0,
  "woningwaarderingen": [],
  "opslagpercentage": 0.0
}
```
