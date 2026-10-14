# test_onderdeel_i_en_ii_worden_niet_afgerond_voordat_ze_worden_opgeteld

De punten van onderdeel I en onderdeel II worden niet afgerond voordat ze bij elkaar worden opgeteld.

Bron: beleidsboek zelfstandige woonruimten, 2.11.2: "1 punt voor iedere
€ 16.954 van de laatstelijk vastgestelde WOZ-waarde met waardepeildatum 1
januari 2025 , 85% van de taxatiewaarde of de minimum WOZ-waarde. Rond dit
puntenaantal niet af.", "Deel de WOZ-waarde door het aantal berekende m² en
vervolgens door € 268 (bij een WOZ-waarde met waardepeildatum 1 januari
2025 , 85% van de taxatiewaarde of minimum WOZ-waarde). Dit geeft het
puntenaantal voor onderdeel II. Rond dit puntenaantal niet af." en "Tel de
punten van de twee onderdelen bij elkaar op en rond volgens de instructie
van paragraaf 2.1.4 af op een kwart punt."

In de output staan de punten van onderdeel I en II wel op twee decimalen.
De waardering 'Afronding op kwartpunten' is het verschil tussen de som van
die twee rijen en het totaal.

Bron: docs/voor-ontwikkelaars/criteriumstrategie, Structuur van de output:
"Punten van een waardering worden in de berekening niet tussentijds op twee
decimalen afgerond; alleen het rubriektotaal wordt op een kwart punt
afgerond. Bij het vastleggen in de output krijgen de rijen wel twee
decimalen. Afronding op kwartpunten sluit het verschil tussen de som van
die getoonde rijen en het stelselgroeptotaal".

De eenheid heeft alleen een bouwjaar, een WOZ-waarde en een slaapkamer.
Deze rubriek rekent met de uitkomst van de andere rubrieken: de oppervlakte
uit rubriek 1 en 2, en de punten waaraan het minimum van 40 punten en de
cap op de WOZ worden getoetst. De package waardeert die rubrieken daarom
mee en waarschuwt voor de energieprestatie, de monumenten, de pandsoort en
de keuken die ontbreken.

Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
genereert de package een `UserWarning`."

## Rapport

```text
PUNTEN VOOR DE WOZ-WAARDE
  WOZ-waarde op waardepeildatum 01-01-2025                        50000.00 EUR
  Onderdeel I                                                                     2.95 pt
    - Factor I                                                    16954.00 EUR
  Onderdeel II                                                                    7.18 pt
    - Oppervlakte van vertrekken en overige ruimten                  26.00 m²
    - Factor II                                                     268.00 EUR
  Afronding op kwartpunten                                                       -0.13 pt
                                                                                ------
  Totaal                                                                         10.00 pt
```

## Waarschuwingen

- UserWarning: Eenheid (eenheid): 'energieprestaties' is None
- UserWarning: Eenheid (eenheid): 'monumenten' is niet gespecificeerd. Indien de eenheid geen monumentstatus heeft, geef dit dan expliciet aan door een lege lijst toe te wijzen aan het 'monumenten'-attribuut.
- UserWarning: Eenheid (eenheid) heeft geen pandsoort Eengezinswoning of Meergezinswoning en komt daarom niet in aanmerking voor waardering onder stelselgroep Energieprestatie.
- UserWarning: Eenheid (eenheid) kan niet gewaardeerd worden voor stelselgroep Keuken omdat er geen keuken is gevonden.

## Input

```json
{
  "id": "eenheid",
  "bouwjaar": 1980,
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
      "oppervlakte": 26.0,
      "verwarmd": true
    }
  ],
  "wozEenheden": [
    {
      "vastgesteldeWaarde": 50000.0,
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
  "punten": 10.0,
  "woningwaarderingen": [
    {
      "aantal": 50000.0,
      "criterium": {
        "id": "punten_voor_de_woz_waarde__woz_waarde",
        "naam": "WOZ-waarde op waardepeildatum 01-01-2025",
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
      "punten": 2.95
    },
    {
      "aantal": 16954.0,
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
      "punten": 7.18
    },
    {
      "aantal": 26.0,
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
      "aantal": 268.0,
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
      "punten": -0.13
    }
  ]
}
```
