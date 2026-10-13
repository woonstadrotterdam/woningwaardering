# test_buitenruimte_gedeeld_met_meerdere_adressen_zonder_aantal_onzelfstandige_woonruimten_wordt_alleen_door_het_aantal_adressen_gedeeld

Een buitenruimte die met meerdere adressen wordt gedeeld en zonder aantal onzelfstandige woonruimten is aangeleverd, wordt alleen door het aantal adressen gedeeld.

De package leest een ontbrekend aantal onzelfstandige woonruimten als één
woonruimte met toegang; die lezing staat in geen bron. Tuin1 wordt met 2
adressen gedeeld en Tuin2 met 3 adressen.

Bron: wettekst, Bijlage I onder B, rubriek 8: "Gemeenschappelijke
buitenruimten gedeeld met meerdere adressen", "0,75 punt per m², gedeeld
door het aantal adressen dat toegang en gebruiksrecht heeft, en daarna
gedeeld door het aantal onzelfstandige woonruimten op dat adres".

Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Wanneer op een
adres slechts een aantal onzelfstandige woonruimten gebruik mogen maken van
een gemeenschappelijk vertrek, ruimte of voorziening, en dus niet alle
aanwezige onzelfstandige woonruimten, worden de punten enkel gedeeld door
het aantal onzelfstandige woonruimten dat krachtens de huurovereenkomst
toegang en gebruiksrecht heeft tot dat vertrek, die ruimte of die
voorziening(en)."

## Rapport

```text
BUITENRUIMTEN
  Gedeeld met 2 adressen
    - Tuin1                                                           6.00 m²     2.25 pt
  Gedeeld met 3 adressen
    - Tuin2                                                           6.00 m²     1.50 pt
                                                                                ------
  Totaal                                                                          3.75 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "tuin1",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "TUI",
        "naam": "Tuin"
      },
      "naam": "Tuin1",
      "oppervlakte": 6.0,
      "gedeeldMetAantalAdressen": 2
    },
    {
      "id": "tuin2",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "TUI",
        "naam": "Tuin"
      },
      "naam": "Tuin2",
      "oppervlakte": 6.0,
      "gedeeldMetAantalAdressen": 3
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
  "punten": 3.75,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "buitenruimten__gedeeld_met_2_adressen",
        "naam": "Gedeeld met 2 adressen"
      }
    },
    {
      "aantal": 6.0,
      "criterium": {
        "id": "buitenruimten__gedeeld_met_2_adressen__tuin1",
        "naam": "Tuin1",
        "bovenliggendeCriterium": {
          "id": "buitenruimten__gedeeld_met_2_adressen"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": 2.25
    },
    {
      "criterium": {
        "id": "buitenruimten__gedeeld_met_3_adressen",
        "naam": "Gedeeld met 3 adressen"
      }
    },
    {
      "aantal": 6.0,
      "criterium": {
        "id": "buitenruimten__gedeeld_met_3_adressen__tuin2",
        "naam": "Tuin2",
        "bovenliggendeCriterium": {
          "id": "buitenruimten__gedeeld_met_3_adressen"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": 1.5
    }
  ]
}
```
