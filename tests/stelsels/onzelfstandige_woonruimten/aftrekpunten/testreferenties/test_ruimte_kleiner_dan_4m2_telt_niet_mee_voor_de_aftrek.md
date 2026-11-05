# test_ruimte_kleiner_dan_4m2_telt_niet_mee_voor_de_aftrek

Een ruimte kleiner dan 4 m² is geen vertrek en telt niet mee voor de aftrek.

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.2.1.2
- wettekst, Bijlage I onder A, toelichting rubriek 1 (via Bijlage I onder B, toelichting, inleiding)

Minder dan 8 m² aan vertrekken geeft 4 punten aftrek.

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.13
- wettekst, Bijlage I onder B, onderdeel 13

## Rapport

```text
AFTREKPUNTEN
  Oppervlakte van vertrekken is minder dan 8 m²                       5.00 m²    -4.00 pt
                                                                                ------
  Totaal                                                                         -4.00 pt
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
      "oppervlakte": 5.0
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
      "oppervlakte": 3.99
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
      "code": "AFT",
      "naam": "Aftrekpunten"
    }
  },
  "punten": -4.0,
  "woningwaarderingen": [
    {
      "aantal": 5.0,
      "criterium": {
        "id": "aftrekpunten__oppervlakte_van_vertrekken_minder_dan_8m2",
        "naam": "Oppervlakte van vertrekken is minder dan 8 m²",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": -4.0
    }
  ]
}
```
