# test_woz_waarde_per_m2_binnen_10_procent_van_het_gemiddelde_van_het_corop_gebied_geeft_12_punten

Een WOZ-waarde per m² gebruiksoppervlakte die maximaal 10% hoger of lager is dan het gemiddelde van het COROP-gebied, geeft 12 punten.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.11.2; wettekst,
Bijlage I onder B, onderdeel 11.1.

De package rekent met de meest recent vastgestelde WOZ-waarde.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.11.1.

## Rapport

```text
PUNTEN VOOR DE WOZ-WAARDE
  Percentage verschil                                                -0.07       12.00 pt
    - WOZ-waarde op waardepeildatum 01-01-2024                   205000.00 EUR
    - Gebruiksoppervlakte                                            58.00 m²
    - WOZ-waarde per m²                                            3534.48 EUR
    - Gemiddelde WOZ-waarde per m² voor Groot-Rijnmond             3537.00 EUR
                                                                                ------
  Totaal                                                                         12.00 pt
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
    "bagGebruikersOppervlakte": 58
  },
  "wozEenheden": [
    {
      "vastgesteldeWaarde": 178000.0,
      "waardepeildatum": "2022-01-01"
    },
    {
      "vastgesteldeWaarde": 194000.0,
      "waardepeildatum": "2023-01-01"
    },
    {
      "vastgesteldeWaarde": 205000.0,
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
  "punten": 12.0,
  "woningwaarderingen": [
    {
      "aantal": -0.0711688,
      "criterium": {
        "id": "punten_voor_de_woz_waarde__percentage_verschil",
        "naam": "Percentage verschil"
      },
      "punten": 12.0
    },
    {
      "aantal": 205000.0,
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
      "aantal": 58.0,
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
      "aantal": 3534.48276,
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
