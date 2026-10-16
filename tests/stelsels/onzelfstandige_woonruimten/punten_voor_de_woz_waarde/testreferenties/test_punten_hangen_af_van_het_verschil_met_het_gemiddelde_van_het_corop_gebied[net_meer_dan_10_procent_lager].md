# test_punten_hangen_af_van_het_verschil_met_het_gemiddelde_van_het_corop_gebied[net_meer_dan_10_procent_lager]

De punten voor de WOZ-waarde hangen af van hoeveel de WOZ-waarde per m² afwijkt van het gemiddelde van het COROP-gebied.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.11.2; wettekst,
Bijlage I onder B, onderdeel 11.1.

Dit geval: het verschil is -10,0003%; het rapport rondt af op -10,00

## Rapport

```text
PUNTEN VOOR DE WOZ-WAARDE
  Percentage verschil                                               -10.00       10.00 pt
    - WOZ-waarde op waardepeildatum 01-01-2024                   318329.00 EUR
    - Gebruiksoppervlakte                                           100.00 m²
    - WOZ-waarde per m²                                            3183.29 EUR
    - Gemiddelde WOZ-waarde per m² voor Groot-Rijnmond             3537.00 EUR
                                                                                ------
  Totaal                                                                         10.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "adres": {
    "woonplaats": {
      "code": "3086",
      "naam": "ROTTERDAM"
    }
  },
  "adresseerbaarObjectBasisregistratie": {
    "bagGebruikersOppervlakte": 100
  },
  "wozEenheden": [
    {
      "vastgesteldeWaarde": 318329.0,
      "waardepeildatum": "2024-01-01"
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
      "code": "WOZ",
      "naam": "Punten voor de WOZ-waarde"
    }
  },
  "punten": 10.0,
  "woningwaarderingen": [
    {
      "aantal": -10.0002827,
      "criterium": {
        "id": "punten_voor_de_woz_waarde__percentage_verschil",
        "naam": "Percentage verschil"
      },
      "punten": 10.0
    },
    {
      "aantal": 318329.0,
      "criterium": {
        "id": "punten_voor_de_woz_waarde__percentage_verschil__woz_waarde",
        "naam": "WOZ-waarde op waardepeildatum 01-01-2024",
        "bovenliggendeCriterium": {
          "id": "punten_voor_de_woz_waarde__percentage_verschil"
        },
        "meeteenheid": {
          "code": "EUR",
          "naam": "Euro"
        }
      }
    },
    {
      "aantal": 100.0,
      "criterium": {
        "id": "punten_voor_de_woz_waarde__percentage_verschil__gebruiksoppervlakte",
        "naam": "Gebruiksoppervlakte",
        "bovenliggendeCriterium": {
          "id": "punten_voor_de_woz_waarde__percentage_verschil"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "aantal": 3183.29,
      "criterium": {
        "id": "punten_voor_de_woz_waarde__percentage_verschil__woz_waarde_per_m2",
        "naam": "WOZ-waarde per m²",
        "bovenliggendeCriterium": {
          "id": "punten_voor_de_woz_waarde__percentage_verschil"
        },
        "meeteenheid": {
          "code": "EUR",
          "naam": "Euro"
        }
      }
    },
    {
      "aantal": 3537.0,
      "criterium": {
        "id": "punten_voor_de_woz_waarde__percentage_verschil__gemiddelde_woz_waarde_per_m2",
        "naam": "Gemiddelde WOZ-waarde per m² voor Groot-Rijnmond",
        "bovenliggendeCriterium": {
          "id": "punten_voor_de_woz_waarde__percentage_verschil"
        },
        "meeteenheid": {
          "code": "EUR",
          "naam": "Euro"
        }
      }
    }
  ]
}
```
