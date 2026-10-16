# test_open_keuken_in_een_onverwarmd_vertrek_krijgt_geen_punten

Een open keuken in een vertrek zonder verwarming krijgt geen punten.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.3.2;
wettekst, Bijlage I onder A, toelichting rubriek 3 (via Bijlage I onder
B, toelichting, inleiding).

## Rapport

Geen waarderingen voor Verkoeling en verwarming.

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
      "oppervlakte": 10.0,
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
          "lengte": 2700.0
        }
      ],
      "verwarmd": false
    },
    {
      "id": "woonkamer/keuken1",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "WOK",
        "naam": "Woonkamer/keuken"
      },
      "naam": "Woonkamer/keuken1",
      "oppervlakte": 10.0,
      "verwarmd": false
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
      "oppervlakte": 10.0,
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
          "lengte": 2700.0
        }
      ],
      "verwarmd": false,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
    },
    {
      "id": "woonkamer/keuken2",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "WOK",
        "naam": "Woonkamer/keuken"
      },
      "naam": "Woonkamer/keuken2",
      "oppervlakte": 10.0,
      "verwarmd": false,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
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
      "code": "VKV",
      "naam": "Verkoeling en verwarming"
    }
  },
  "punten": 0.0,
  "woningwaarderingen": []
}
```
