# test_gemeenschappelijke_buitenruimte_op_hetzelfde_adres_krijgt_driekwart_punt_per_m2_gedeeld_door_het_aantal_onzelfstandige_woonruimten

Een gemeenschappelijke buitenruimte op hetzelfde adres krijgt 0,75 punt per m², gedeeld door het aantal onzelfstandige woonruimten dat toegang heeft.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.8.2; wettekst,
Bijlage I onder B, onderdeel 8.

## Rapport

```text
BUITENRUIMTEN
  Gedeeld met 2 onzelfstandige woonruimten
    - Balkon                                                          6.00 m²     2.25 pt
                                                                                ------
  Totaal                                                                          2.25 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
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
      "oppervlakte": 6.0,
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
      "code": "BUI",
      "naam": "Buitenruimten"
    }
  },
  "punten": 2.25,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "buitenruimten__gedeeld_met_2_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 2 onzelfstandige woonruimten"
      }
    },
    {
      "aantal": 6.0,
      "criterium": {
        "id": "buitenruimten__gedeeld_met_2_onzelfstandige_woonruimten__balkon",
        "naam": "Balkon",
        "bovenliggendeCriterium": {
          "id": "buitenruimten__gedeeld_met_2_onzelfstandige_woonruimten"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": 2.25
    }
  ]
}
```
