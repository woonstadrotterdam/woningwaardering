# test_onderdeel_ii_rekent_met_de_oppervlakte_van_vertrekken_overige_ruimten_en_parkeerplekken_type_i

In onderdeel II telt de oppervlakte mee van de vertrekken en overige ruimten uit rubriek 1 en 2 en van de parkeerplekken type I uit rubriek 10.

Bron: wettekst, Bijlage I onder A, onderdeel 11.1: "die waarde, gedeeld
door het aantal m² van de vertrekken, de overige ruimten en parkeerplekken,
bedoeld in de rubrieken 1,2 en 10 voor zover het parkeerplek type I
betreft".

De woonkamer van 10 m² is een vertrek en de eerste toiletruimte van 10 m²
een overige ruimte. De tweede toiletruimte telt niet mee: met 1,9 m² is zij
geen overige ruimte in rubriek 2.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 2: "De ruimte dient
een oppervlakte te hebben van minimaal 2 m²."

Van een parkeerplek type I telt de oppervlakte gedeeld door het aantal
adressen. De eerste ruimte staat voor twee parkeerplekken van elk 20 m²,
gedeeld met 4 adressen, en telt voor 10 m². De tweede ruimte telt niet mee:
een parkeerplek van 10 m² valt niet onder rubriek 10.

Bron: implementatietoelichting zelfstandige woonruimten, 2.11.2: "Wij gaan
er vanuit dat de oppervlakte van de parkeerplekken ook nog gedeeld moet
worden door het aantal adressen dat toegang heeft tot de parkeerplek, omdat
er anders onredelijk veel punten kunnen worden toegewezen voor
parkeerplekken. Wij hanteren geen standaardmaat van 12m2, omdat een
parkeerplek Type I kleiner dan12m2 niet onder rubriek 10 valt."

Bron: implementatietoelichting, datamodel-uitbreidingen, "Aantal":
"Hierdoor is het mogelijk om aan te geven hoeveel van deze specifieke
ruimte er zijn."

De WOZ-waarde heeft waardepeildatum 1 januari 2024.

Bron: wettekst, Bijlage I onder A, onderdeel 11.1: "1 punt per € 15.329
voor WOZ-beschikkingen met waardepeildatum 1 januari 2024." en "€ 242 bij
WOZ-beschikkingen met waardepeildatum 1 januari 2024."

De eenheid heeft alleen een WOZ-waarde en deze ruimten. Deze rubriek rekent
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
  Onderdeel II                                                                   13.77 pt
    - Oppervlakte van vertrekken en overige ruimten                  30.00 m²
    - Factor II                                                     242.00 EUR
  Afronding op kwartpunten                                                       -0.04 pt
                                                                                ------
  Totaal                                                                         20.25 pt
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
      "id": "toiletruimte1",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "TOI",
        "naam": "Toiletruimte"
      },
      "naam": "Toiletruimte1",
      "oppervlakte": 10.0
    },
    {
      "id": "toiletruimte2",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "TOI",
        "naam": "Toiletruimte"
      },
      "naam": "Toiletruimte2",
      "oppervlakte": 1.9
    },
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
    },
    {
      "id": "parkeerplek1",
      "soort": {
        "code": "GEM",
        "naam": "Gemeenschappelijke ruimten en voorzieningen"
      },
      "detailSoort": {
        "code": "PIP",
        "naam": "Parkeerplek in inpandige afgesloten parkeergarage"
      },
      "naam": "Parkeerplek1",
      "oppervlakte": 20.0,
      "gedeeldMetAantalAdressen": 4,
      "aantal": 2
    },
    {
      "id": "parkeerplek2",
      "soort": {
        "code": "GEM",
        "naam": "Gemeenschappelijke ruimten en voorzieningen"
      },
      "detailSoort": {
        "code": "PIP",
        "naam": "Parkeerplek in inpandige afgesloten parkeergarage"
      },
      "naam": "Parkeerplek2",
      "oppervlakte": 10.0,
      "gedeeldMetAantalAdressen": 4,
      "aantal": 2
    }
  ],
  "wozEenheden": [
    {
      "vastgesteldeWaarde": 100000.0,
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
      "code": "ZEL",
      "naam": "Zelfstandige woonruimten"
    },
    "stelselgroep": {
      "code": "WOZ",
      "naam": "Punten voor de WOZ-waarde"
    }
  },
  "punten": 20.25,
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
      "punten": 13.77
    },
    {
      "aantal": 30.0,
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
      "punten": -0.04
    }
  ]
}
```
