# test_kast_telt_mee_voor_de_minimale_oppervlakte_van_een_vertrek[samen_precies_4m2]

Een ruimte kleiner dan 4 m² is een vertrek als zij met haar kast 4 m² of groter is.

Bron: implementatietoelichting zelfstandige woonruimten, 2.2.4;
wettekst, Bijlage I onder A, toelichting rubriek 1.

Dit geval: het vertrek van 3,50 m² en de kast van 0,50 m² zijn samen precies 4,00 m², de minimale oppervlakte van een vertrek

## Rapport

```text
OPPERVLAKTE VAN VERTREKKEN
  Slaapkamer (+1 kast)                                                4.00 m²
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
      "id": "slaapkamer",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer",
      "oppervlakte": 3.5,
      "verbondenRuimten": [
        {
          "id": "kast",
          "soort": {
            "code": "OVR",
            "naam": "Overige ruimten"
          },
          "detailSoort": {
            "code": "KAS",
            "naam": "Kast"
          },
          "naam": "Kast",
          "oppervlakte": 0.5
        }
      ]
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
        "id": "oppervlakte_van_vertrekken__slaapkamer",
        "naam": "Slaapkamer (+1 kast)",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    }
  ]
}
```
