# test_gemeenschappelijke_overige_ruimte_wordt_gedeeld_door_aantal_woonruimten_met_toegang

Een gemeenschappelijke overige ruimte wordt gedeeld door het aantal onzelfstandige woonruimten dat toegang en gebruiksrecht heeft tot die ruimte.

De wettekst deelt de punten. De package deelt per ruimte de oppervlakte;
punten delen zou hier 2,75 punten geven.

Bron: wettekst, Bijlage I onder B, onderdeel 2: "Oppervlakte
gemeenschappelijke overige ruimte(n) op hetzelfde adres, niet zijnde
verkeersruimten (o.a. berging, zolder, garage)", "0,75 punt per m², te
delen door het aantal onzelfstandige woonruimten dat toegang en
gebruiksrecht heeft".

Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Wanneer op een
adres slechts een aantal onzelfstandige woonruimten gebruik mogen maken van
een gemeenschappelijk vertrek, ruimte of voorziening, en dus niet alle
aanwezige onzelfstandige woonruimten, worden de punten enkel gedeeld door
het aantal onzelfstandige woonruimten dat krachtens de huurovereenkomst
toegang en gebruiksrecht heeft tot dat vertrek, die ruimte of die
voorziening(en)."

Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.2.1: "per
ruimte delen waar nodig, salderen, daarna éénmaal afronden op hele m²,
daarna × 0,75."

## Rapport

```text
OPPERVLAKTE VAN OVERIGE RUIMTEN
  Gedeeld met 5 onzelfstandige woonruimten
    - Bijkeuken                                                      10.00 m²
  Gedeeld met 6 onzelfstandige woonruimten
    - Garage                                                         10.00 m²
                                                                                ------
  Totaal                                                                          3.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "bijkeuken",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "BIJ",
        "naam": "Bijkeuken"
      },
      "naam": "Bijkeuken",
      "oppervlakte": 10.0,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 5
    },
    {
      "id": "garage",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "GAR",
        "naam": "Garage"
      },
      "naam": "Garage",
      "oppervlakte": 10.0,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 6
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
      "code": "OOZ",
      "naam": "Oppervlakte van overige ruimten"
    }
  },
  "punten": 3.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__gedeeld_met_5_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 5 onzelfstandige woonruimten"
      }
    },
    {
      "aantal": 10.0,
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__gedeeld_met_5_onzelfstandige_woonruimten__bijkeuken",
        "naam": "Bijkeuken",
        "bovenliggendeCriterium": {
          "id": "oppervlakte_van_overige_ruimten__gedeeld_met_5_onzelfstandige_woonruimten"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__gedeeld_met_6_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 6 onzelfstandige woonruimten"
      }
    },
    {
      "aantal": 10.0,
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__gedeeld_met_6_onzelfstandige_woonruimten__garage",
        "naam": "Garage",
        "bovenliggendeCriterium": {
          "id": "oppervlakte_van_overige_ruimten__gedeeld_met_6_onzelfstandige_woonruimten"
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
