# test_rekenvoorbeeld_uit_het_beleidsboek_geeft_36_25_punten

Een WOZ-waarde van € 300.000 met waardepeildatum 1 januari 2025 geeft bij 60 m² aan vertrekken 36,25 punten, zoals in het rekenvoorbeeld van het beleidsboek.

Bron: beleidsboek zelfstandige woonruimten, 2.11.2: "De WOZ-waarde van een
woning is op 1 januari 2026 vastgesteld op € 300.000, met de
waardepeildatum 1 januari 2025. De oppervlakte van de vertrekken en overige
ruimten van de woning is 60 m².", "Onderdeel I: € 300.000 / € 16.954 =
17,6949392474 punten", "Onderdeel II: € 300.000 / 60 (m²) / € 268 =
18,6567164179 punten" en "Totaal = 36,3516556653. Dit is afgerond 36,25
punten."

In de output staan de punten van onderdeel I en II op twee decimalen. De
waardering 'Afronding op kwartpunten' is het verschil tussen de som van die
twee rijen en het totaal.

Bron: docs/voor-ontwikkelaars/criteriumstrategie, Structuur van de output:
"Bij het vastleggen in de output krijgen de rijen wel twee decimalen.
Afronding op kwartpunten sluit het verschil tussen de som van die getoonde
rijen en het stelselgroeptotaal".

De eenheid heeft alleen een bouwjaar, een WOZ-waarde en een woonkamer. Deze
rubriek rekent met de uitkomst van de andere rubrieken: de oppervlakte uit
rubriek 1 en 2, en de punten waaraan het minimum van 40 punten en de cap op
de WOZ worden getoetst. De package waardeert die rubrieken daarom mee en
waarschuwt voor de energieprestatie, de monumenten, de pandsoort en de
keuken die ontbreken.

Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
genereert de package een `UserWarning`."

## Rapport

```text
PUNTEN VOOR DE WOZ-WAARDE
  WOZ-waarde op waardepeildatum 01-01-2025                       300000.00 EUR
  Onderdeel I                                                                    17.69 pt
    - Factor I                                                    16954.00 EUR
  Onderdeel II                                                                   18.66 pt
    - Oppervlakte van vertrekken en overige ruimten                  60.00 m²
    - Factor II                                                     268.00 EUR
  Afronding op kwartpunten                                                       -0.10 pt
                                                                                ------
  Totaal                                                                         36.25 pt
```

## Waarschuwingen

- UserWarning: Eenheid (None): 'energieprestaties' is None
- UserWarning: Eenheid (None): 'monumenten' is niet gespecificeerd. Indien de eenheid geen monumentstatus heeft, geef dit dan expliciet aan door een lege lijst toe te wijzen aan het 'monumenten'-attribuut.
- UserWarning: Eenheid (None) heeft geen pandsoort Eengezinswoning of Meergezinswoning en komt daarom niet in aanmerking voor waardering onder stelselgroep Energieprestatie.
- UserWarning: Eenheid (None) kan niet gewaardeerd worden voor stelselgroep Keuken omdat er geen keuken is gevonden.

## Input

```json
{
  "bouwjaar": 1990,
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
      "oppervlakte": 60.0,
      "verwarmd": true
    }
  ],
  "wozEenheden": [
    {
      "vastgesteldeWaarde": 300000.0,
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
  "punten": 36.25,
  "woningwaarderingen": [
    {
      "aantal": 300000.0,
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
      "punten": 17.69
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
      "punten": 18.66
    },
    {
      "aantal": 60.0,
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
      "punten": -0.1
    }
  ]
}
```
