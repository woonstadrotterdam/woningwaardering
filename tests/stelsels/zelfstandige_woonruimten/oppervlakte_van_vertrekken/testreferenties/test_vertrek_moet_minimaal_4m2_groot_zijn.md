# test_vertrek_moet_minimaal_4m2_groot_zijn

Een ruimte kleiner dan 4 m² wordt niet als vertrek gewaardeerd.

Bron: implementatietoelichting zelfstandige woonruimten, 2.2.1.2;
wettekst, Bijlage I onder A, toelichting rubriek 1.

## Rapport

```text
OPPERVLAKTE VAN VERTREKKEN
  Slaapkamer2                                                         4.00 m²
                                                                    ------      ------
  Totaal                                                              4.00 m²     4.00 pt
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
      "code": "ZEL",
      "naam": "Zelfstandige woonruimten"
    },
    "stelselgroep": {
      "code": "OVZ",
      "naam": "Oppervlakte van vertrekken"
    }
  },
  "punten": 4.0,
  "woningwaarderingen": [
    {
      "aantal": 4.0,
      "criterium": {
        "id": "oppervlakte_van_vertrekken__slaapkamer2",
        "naam": "Slaapkamer2",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    }
  ]
}
```
