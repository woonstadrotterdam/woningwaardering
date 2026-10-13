# test_woz_eenheid_zonder_vastgestelde_waarde_wordt_overgeslagen

Een WOZ-eenheid zonder vastgestelde waarde slaat de package over: zij rekent met de meest recente WOZ-waarde die wel is vastgesteld.

De WOZ-eenheid met waardepeildatum 1 januari 2025 heeft geen vastgestelde
waarde. De package rekent met de WOZ-waarde van 1 januari 2024 en met de
kengetallen die bij die waardepeildatum horen. De implementatietoelichting
noemt die keuze niet; de test legt het huidige gedrag vast.

Bron: beleidsboek zelfstandige woonruimten, 2.11.1: "Met de laatst
vastgestelde WOZ-waarde wordt de meest recent vastgestelde WOZ-waarde op de
peildatum van de procedure bedoeld."

Bron: wettekst, Bijlage I onder A, onderdeel 11.1: "1 punt per € 15.329
voor WOZ-beschikkingen met waardepeildatum 1 januari 2024." en "€ 242 bij
WOZ-beschikkingen met waardepeildatum 1 januari 2024."

De eenheid heeft alleen WOZ-eenheden en een woonkamer. Deze rubriek rekent
met de uitkomst van de andere rubrieken: de oppervlakte uit rubriek 1 en 2,
en de punten waaraan het minimum van 40 punten en de cap op de WOZ worden
getoetst. De package waardeert die rubrieken daarom mee en waarschuwt voor
de energieprestatie, de monumenten, de pandsoort, de keuken en het bouwjaar
die ontbreken.

Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
genereert de package een `UserWarning`."

## Rapport

```text
PUNTEN VOOR DE WOZ-WAARDE
  WOZ-waarde op waardepeildatum 01-01-2024                       100000.00 EUR
  Onderdeel I                                                                     6.52 pt
    - Factor I                                                    15329.00 EUR
  Onderdeel II                                                                   41.32 pt
    - Oppervlakte van vertrekken en overige ruimten                  10.00 m²
    - Factor II                                                     242.00 EUR
  Afronding op kwartpunten                                                       -0.09 pt
                                                                                ------
  Totaal                                                                         47.75 pt
```

## Waarschuwingen

- UserWarning: Eenheid (eenheid): 'energieprestaties' is None
- UserWarning: Eenheid (eenheid): 'monumenten' is niet gespecificeerd. Indien de eenheid geen monumentstatus heeft, geef dit dan expliciet aan door een lege lijst toe te wijzen aan het 'monumenten'-attribuut.
- UserWarning: Eenheid (eenheid) heeft geen pandsoort Eengezinswoning of Meergezinswoning en komt daarom niet in aanmerking voor waardering onder stelselgroep Energieprestatie.
- UserWarning: Eenheid (eenheid) kan niet gewaardeerd worden voor stelselgroep Keuken omdat er geen keuken is gevonden.
- UserWarning: Eenheid (eenheid): geen bouwjaar gevonden. Kan niet bepalen of woning onder nieuwbouw valt.

## Input

```json
{
  "id": "eenheid",
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
      "oppervlakte": 10.0
    }
  ],
  "wozEenheden": [
    {
      "vastgesteldeWaarde": 100000.0,
      "waardepeildatum": "2022-01-01"
    },
    {
      "vastgesteldeWaarde": 100000.0,
      "waardepeildatum": "2023-01-01"
    },
    {
      "vastgesteldeWaarde": 100000.0,
      "waardepeildatum": "2024-01-01"
    },
    {
      "waardepeildatum": "2025-01-01"
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
      "code": "WOZ",
      "naam": "Punten voor de WOZ-waarde"
    }
  },
  "punten": 47.75,
  "woningwaarderingen": [
    {
      "aantal": 100000.0,
      "criterium": {
        "id": "punten_voor_de_woz_waarde__woz_waarde",
        "naam": "WOZ-waarde op waardepeildatum 01-01-2024",
        "meeteenheid": {
          "code": "EUR",
          "naam": "Euro"
        }
      }
    },
    {
      "criterium": {
        "id": "punten_voor_de_woz_waarde__onderdeel_I",
        "naam": "Onderdeel I"
      },
      "punten": 6.52
    },
    {
      "aantal": 15329.0,
      "criterium": {
        "id": "punten_voor_de_woz_waarde__onderdeel_I__factor_I",
        "naam": "Factor I",
        "bovenliggendeCriterium": {
          "id": "punten_voor_de_woz_waarde__onderdeel_I"
        },
        "meeteenheid": {
          "code": "EUR",
          "naam": "Euro"
        }
      }
    },
    {
      "criterium": {
        "id": "punten_voor_de_woz_waarde__onderdeel_II",
        "naam": "Onderdeel II"
      },
      "punten": 41.32
    },
    {
      "aantal": 10.0,
      "criterium": {
        "id": "punten_voor_de_woz_waarde__onderdeel_II__oppervlakte_vertrekken_en_overige_ruimten",
        "naam": "Oppervlakte van vertrekken en overige ruimten",
        "bovenliggendeCriterium": {
          "id": "punten_voor_de_woz_waarde__onderdeel_II"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "aantal": 242.0,
      "criterium": {
        "id": "punten_voor_de_woz_waarde__onderdeel_II__factor_II",
        "naam": "Factor II",
        "bovenliggendeCriterium": {
          "id": "punten_voor_de_woz_waarde__onderdeel_II"
        },
        "meeteenheid": {
          "code": "EUR",
          "naam": "Euro"
        }
      }
    },
    {
      "criterium": {
        "id": "punten_voor_de_woz_waarde__afronding_op_kwartpunten",
        "naam": "Afronding op kwartpunten"
      },
      "punten": -0.09
    }
  ]
}
```
