# test_gemeenschappelijk_vertrek_wordt_gedeeld_door_aantal_woonruimten_met_toegang

Een gemeenschappelijk vertrek wordt gedeeld door het aantal onzelfstandige woonruimten dat toegang en gebruiksrecht heeft tot dat vertrek.

Bron: wettekst, Bijlage I onder B, onderdeel 1: "Oppervlakte
gemeenschappelijk(e) vertrek(ken) op hetzelfde adres", "1 punt per m², te
delen door het aantal onzelfstandige woonruimten dat toegang en
gebruiksrecht heeft".

Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Wanneer op een
adres slechts een aantal onzelfstandige woonruimten gebruik mogen maken van
een gemeenschappelijk vertrek, ruimte of voorziening, en dus niet alle
aanwezige onzelfstandige woonruimten, worden de punten enkel gedeeld door
het aantal onzelfstandige woonruimten dat krachtens de huurovereenkomst
toegang en gebruiksrecht heeft tot dat vertrek, die ruimte of die
voorziening(en)."

Bron: implementatietoelichting onzelfstandige woonruimten, 2.1.1.1: "Daarom
volgen wij: per ruimte delen waar nodig, salderen, daarna éénmaal afronden
op hele m²."

## Rapport

```text
OPPERVLAKTE VAN VERTREKKEN
  Gedeeld met 6 onzelfstandige woonruimten
    - Woonkamer                                                      10.00 m²
  Gedeeld met 5 onzelfstandige woonruimten
    - Slaapkamer                                                     10.00 m²
                                                                                ------
  Totaal                                                                          4.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
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
      "oppervlakte": 10.0,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 6
    },
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
      "oppervlakte": 10.0,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 5
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
      "code": "OVZ",
      "naam": "Oppervlakte van vertrekken"
    }
  },
  "punten": 4.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "oppervlakte_van_vertrekken__gedeeld_met_6_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 6 onzelfstandige woonruimten"
      }
    },
    {
      "aantal": 10.0,
      "criterium": {
        "id": "oppervlakte_van_vertrekken__gedeeld_met_6_onzelfstandige_woonruimten__woonkamer",
        "naam": "Woonkamer",
        "bovenliggendeCriterium": {
          "id": "oppervlakte_van_vertrekken__gedeeld_met_6_onzelfstandige_woonruimten"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "criterium": {
        "id": "oppervlakte_van_vertrekken__gedeeld_met_5_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 5 onzelfstandige woonruimten"
      }
    },
    {
      "aantal": 10.0,
      "criterium": {
        "id": "oppervlakte_van_vertrekken__gedeeld_met_5_onzelfstandige_woonruimten__slaapkamer",
        "naam": "Slaapkamer",
        "bovenliggendeCriterium": {
          "id": "oppervlakte_van_vertrekken__gedeeld_met_5_onzelfstandige_woonruimten"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    }
  ]
}
```
