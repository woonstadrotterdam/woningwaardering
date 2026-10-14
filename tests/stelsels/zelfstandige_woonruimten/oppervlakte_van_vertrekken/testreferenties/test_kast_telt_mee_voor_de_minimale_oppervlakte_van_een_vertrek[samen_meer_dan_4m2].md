# test_kast_telt_mee_voor_de_minimale_oppervlakte_van_een_vertrek[samen_meer_dan_4m2]

Een ruimte kleiner dan 4 m² is een vertrek als zij met haar kast 4 m² of groter is.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 1: "Meting van de
oppervlakte van vertrekken vindt plaats van muur tot muur, op een hoogte van
1,50 meter boven de vloer, inclusief de oppervlakte van alle tot de woning
behorende losse en vaste kasten."

Bron: implementatietoelichting zelfstandige woonruimten, 2.2.4: "De
kastoppervlakte telt ook mee bij de drempeltoets in `classificeer_ruimte`
(4,00 m² voor vertrek, 2,00 m² voor overige ruimte)".

## Rapport

```text
OPPERVLAKTE VAN VERTREKKEN
  Slaapkamer (+1 kast)                                                4.20 m²
                                                                    ------      ------
  Totaal                                                              4.20 m²     4.00 pt
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
      "oppervlakte": 3.7,
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
      "aantal": 4.2,
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
