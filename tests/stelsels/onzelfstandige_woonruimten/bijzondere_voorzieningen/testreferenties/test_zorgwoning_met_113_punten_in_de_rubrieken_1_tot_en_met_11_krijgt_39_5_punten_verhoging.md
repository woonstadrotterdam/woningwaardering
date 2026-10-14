# test_zorgwoning_met_113_punten_in_de_rubrieken_1_tot_en_met_11_krijgt_39_5_punten_verhoging

Een zorgwoning met 113 punten in de rubrieken 1 tot en met 11 krijgt 35% daarvan als verhoging: op een kwart punt afgerond 39,5 punten.

Bron: wettekst, Bijlage I onder B, rubriek 12: "Uitsluitend bij
zorgwoningen" en "bij: 35% van de ingevolge de onderdelen 1 tot en met 11
toegekende punten."

De verhoging is het totaal van deze rubriek en wordt op een kwart punt
afgerond.

Bron: beleidsboek onzelfstandige woonruimten, 2.1.6: "Het totaal aantal
punten wordt per rubriek afgerond op 0,25 punt, waarbij vanaf een achtste
(1/8) punt naar boven wordt afgerond."

De package leest aan de doelgroep af dat de eenheid een zorgwoning is. De
implementatietoelichting voor onzelfstandige woonruimten noemt dat niet;
die voor zelfstandige woonruimten wel.

Bron: implementatietoelichting zelfstandige woonruimten, 2.12.1: "Wanneer
een eenheid de doelgroep Zorg heeft, wordt de woning automatisch als
zorgwoning gewaardeerd."

De eenheid heeft alleen de doelgroep zorg en een verwarmde woonkamer. De
test geeft geen eerder resultaat mee; de package waardeert de andere
rubrieken daarom zelf en waarschuwt voor de monumenten, de energieprestatie
en de WOZ-waarde die ontbreken. Dat de gegevens voor de andere rubrieken
daarvoor in het model moeten staan, zegt alleen de implementatietoelichting
voor zelfstandige woonruimten.

Bron: implementatietoelichting zelfstandige woonruimten, 2.12: "De extra
attributen in het model (zoals de WOZ-waarde, energielabel,
ruimtegegevens, etc.) zijn van belang omdat de 35% opslag voor zorgwoningen
wordt berekend over het totale puntenaantal van de rubrieken 1 t/m 11."

Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
genereert de package een `UserWarning`."

## Rapport

```text
BIJZONDERE VOORZIENINGEN
  Zorgwoning 35% puntenverhoging                                                 39.50 pt
                                                                                ------
  Totaal                                                                         39.50 pt
```

## Waarschuwingen

- UserWarning: Eenheid (zorgwoning): 'monumenten' is niet gespecificeerd. Indien de eenheid geen monumentstatus heeft, geef dit dan expliciet aan door een lege lijst toe te wijzen aan het 'monumenten'-attribuut.
- UserWarning: Eenheid (zorgwoning): 'energieprestaties' is None
- UserWarning: Eenheid zorgwoning: geen WOZ-waarde aangeleverd

## Input

```json
{
  "id": "zorgwoning",
  "doelgroep": {
    "code": "ZOR",
    "naam": "Zorg"
  },
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
      "oppervlakte": 98.0,
      "verwarmd": true,
      "verkoeld": false
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
      "code": "BIJ",
      "naam": "Bijzondere voorzieningen"
    }
  },
  "punten": 39.5,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "bijzondere_voorzieningen__zorgwoning_puntenverhoging",
        "naam": "Zorgwoning 35% puntenverhoging"
      },
      "punten": 39.5
    }
  ]
}
```
