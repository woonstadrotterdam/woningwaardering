# test_woz_waarde_per_m2_ruim_60_procent_onder_het_gemiddelde_van_het_corop_gebied_geeft_10_punten

Een WOZ-waarde per m² gebruiksoppervlakte die ruim 60% onder het gemiddelde van het COROP-gebied ligt, geeft 10 punten.

Bron: wettekst, Bijlage I onder B, onderdeel 11.1: "De WOZ-waarde of 85%
van de taxatiewaarde, indien er geen WOZ-waarde is vastgesteld, van het
adres waar de onzelfstandige woonruimte onderdeel van is, per m²
gebruiksoppervlakte is meer dan 10% lager dan de gemiddelde WOZ-waarde per
m² gebruiksoppervlakte van woningen in het COROP-gebied waarbinnen de
woonruimte is gelegen." en "10 punten".

Woonplaatscode 3086 is Rotterdam, in het COROP-gebied Groot-Rijnmond.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.11.2: "Het
COROP-gebied wordt bepaald op basis van de woonplaatscode van de woonplaats
waarin de eenheid zich bevindt."

De eenheid heeft WOZ-waarden met waardepeildatum 1 januari 2022, 2023 en
2024. De package rekent met de meest recente, die van 1 januari 2024.

Bron: beleidsboek onzelfstandige woonruimten, 2.11.1: "Met de laatst
vastgestelde WOZ-waarde wordt de meest recent vastgestelde WOZ-waarde op de
peildatum van de procedure bedoeld."

Het gemiddelde van het COROP-gebied staat per waardepeildatum in de
Uitvoeringsregeling huurprijzen woonruimte (bijlage IIa): voor
Groot-Rijnmond bij waardepeildatum 1 januari 2024 is dat € 3.537 per m².

Bron: wettekst, Bijlage I onder B, toelichting rubriek 11: "In de
Uitvoeringsregeling huurprijzen woonruimte zijn de COROP-gebieden
weergegeven alsmede de daarbij behorende gemiddelde WOZ-waarde per m²
gebruiksoppervlakte van woningen." en "De kolommen geven op basis van de
peildatum van de WOZ-beschikking weer met welk bedrag moet worden
gerekend."

## Rapport

```text
PUNTEN VOOR DE WOZ-WAARDE
  Percentage verschil                                               -61.98       10.00 pt
    - WOZ-waarde op waardepeildatum 01-01-2024                    78000.00 EUR
    - Gebruiksoppervlakte                                            58.00 m²
    - WOZ-waarde per m²                                            1344.83 EUR
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
    "bagGebruikersOppervlakte": 58
  },
  "wozEenheden": [
    {
      "vastgesteldeWaarde": 58000.0,
      "waardepeildatum": "2022-01-01"
    },
    {
      "vastgesteldeWaarde": 68000.0,
      "waardepeildatum": "2023-01-01"
    },
    {
      "vastgesteldeWaarde": 78000.0,
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
      "aantal": -61.9782983,
      "criterium": {
        "id": "punten_voor_de_woz_waarde__percentage_verschil",
        "naam": "Percentage verschil"
      },
      "punten": 10.0
    },
    {
      "aantal": 78000.0,
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
      "aantal": 1344.82759,
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
