# test_parkeerplek_in_een_uitpandige_afgesloten_parkeergarage_telt_mee_in_onderdeel_ii

In onderdeel II telt ook de oppervlakte mee van een parkeerplek in een uitpandige afgesloten parkeergarage.

Bron:
- implementatietoelichting zelfstandige woonruimten, 2.11.2
- wettekst, Bijlage I onder A, onderdeel 11.1

Een parkeerplek in een afgesloten parkeergarage is type I, of de garage nu
in- of uitpandig is.

Bron:
- implementatietoelichting zelfstandige woonruimten, 2.10.3
- wettekst, Bijlage I onder A, onderdeel 10

## Rapport

```text
PUNTEN VOOR DE WOZ-WAARDE
  WOZ-waarde op waardepeildatum 01-01-2025                       300000.00 EUR
  Onderdeel I                                                                    17.69 pt
    - Factor I                                                    16954.00 EUR
  Onderdeel II                                                                   48.67 pt
    - Oppervlakte van vertrekken en overige ruimten                  23.00 m²
    - Factor II                                                     268.00 EUR
  Afronding op kwartpunten                                                       -0.11 pt
                                                                                ------
  Totaal                                                                         66.25 pt
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
      "oppervlakte": 20.0
    },
    {
      "id": "parkeerplek_in_uitpandige_afgesloten_parkeergarage",
      "soort": {
        "code": "GEM",
        "naam": "Gemeenschappelijke ruimten en voorzieningen"
      },
      "detailSoort": {
        "code": "PUP",
        "naam": "Parkeerplek in uitpandige afgesloten parkeergarage"
      },
      "naam": "Parkeerplek in uitpandige afgesloten parkeergarage",
      "oppervlakte": 12.5,
      "gedeeldMetAantalAdressen": 4
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
  "punten": 66.25,
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
      "punten": 48.67
    },
    {
      "aantal": 23.0,
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
      "punten": -0.11
    }
  ]
}
```
