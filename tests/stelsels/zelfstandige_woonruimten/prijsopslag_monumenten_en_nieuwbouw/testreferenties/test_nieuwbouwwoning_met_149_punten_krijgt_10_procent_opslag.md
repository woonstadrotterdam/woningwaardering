# test_nieuwbouwwoning_met_149_punten_krijgt_10_procent_opslag

Een woning met 149 punten die na 1 juli 2024 voor het eerst in gebruik is genomen en waarvan de bouw voor 1 januari 2028 is gestart, krijgt 10 procent opslag.

Bron: wettekst, artikel 8a, vierde lid: "wordt met 10% vermeerderd indien
die woonruimte na 1 juli 2024 voor het eerst in gebruik wordt genomen als
woonruimte en de bouw van deze woonruimte, of de verbouw van een ruimte met
een andere gebruiksfunctie dan een woonfunctie naar een woonruimte met een
woonfunctie, voor 1 januari 2028 is gestart."

De opslag geldt voor een woning in de middensector. De woning haalt zonder
opslag 149 punten en valt daarmee in de middensector.

Bron: implementatietoelichting zelfstandige woonruimten, 1.3.1: "Hoger dan
€ 932,93 maar maximaal € 1.228,07 of 144 t/m 186 punten"

De keuken heeft geen aanrecht en de woning heeft geen bouwjaar. Daarvoor
waarschuwen de rubrieken keuken en punten voor de WOZ-waarde, die de
package voor het puntentotaal meewaardeert.

Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
genereert de package een `UserWarning`."

## Rapport

```text
PRIJSOPSLAG MONUMENTEN EN NIEUWBOUW
  Nieuwbouw                                                                                    10%
                                                                                ------
  Totaal                                                                          0.00 pt      10%
```

## Waarschuwingen

- UserWarning: Ruimte 'Keuken' (keuken) is een keuken, maar heeft geen aanrecht (of geen aanrecht met een lengte >=1000mm) en mag daardoor niet gewaardeerd worden voor Keuken.
- UserWarning: Eenheid (meergezinswoning_van_79_m2) kan niet gewaardeerd worden voor stelselgroep Keuken omdat er geen keuken is gevonden.
- UserWarning: Eenheid (meergezinswoning_van_79_m2): geen bouwjaar gevonden. Kan niet bepalen of woning onder nieuwbouw valt.

## Input

```json
{
  "id": "meergezinswoning_van_79_m2",
  "beginBouwdatum": "2023-01-01",
  "inExploitatiedatum": "2024-08-01",
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
  ],
  "wozEenheden": [
    {
      "vastgesteldeWaarde": 313000.0,
      "waardepeildatum": "2024-01-01"
    },
    {
      "vastgesteldeWaarde": 307000.0,
      "waardepeildatum": "2023-01-01"
    },
    {
      "vastgesteldeWaarde": 341000.0,
      "waardepeildatum": "2022-01-01"
    },
    {
      "vastgesteldeWaarde": 283000.0,
      "waardepeildatum": "2021-01-01"
    },
    {
      "vastgesteldeWaarde": 273000.0,
      "waardepeildatum": "2020-01-01"
    },
    {
      "vastgesteldeWaarde": 237000.0,
      "waardepeildatum": "2019-01-01"
    },
    {
      "vastgesteldeWaarde": 201000.0,
      "waardepeildatum": "2018-01-01"
    },
    {
      "vastgesteldeWaarde": 163000.0,
      "waardepeildatum": "2017-01-01"
    },
    {
      "vastgesteldeWaarde": 142000.0,
      "waardepeildatum": "2016-01-01"
    },
    {
      "vastgesteldeWaarde": 135000.0,
      "waardepeildatum": "2015-01-01"
    },
    {
      "vastgesteldeWaarde": 125000.0,
      "waardepeildatum": "2014-01-01"
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
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "prijsopslag_monumenten_en_nieuwbouw__nieuwbouw",
        "naam": "Nieuwbouw"
      },
      "opslagpercentage": 0.1
    }
  ],
  "opslagpercentage": 0.1
}
```
