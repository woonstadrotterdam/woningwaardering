# test_zorgwoning_met_41_punten_in_de_rubrieken_1_tot_en_met_11_1_krijgt_14_25_punten_verhoging

Een zorgwoning met 41 punten in de rubrieken 1 tot en met 11.1 krijgt 35% daarvan als verhoging: op een kwart punt afgerond 14,25 punten.

Bron: wettekst, Bijlage I onder A, rubriek 12: "Uitsluitend bij
zorgwoningen" en "bij: 35% van de ingevolge de onderdelen 1 tot en met 11.1
toegekende punten."

De verhoging is het totaal van deze rubriek en wordt op een kwart punt
afgerond.

Bron: beleidsboek zelfstandige woonruimten, 2.1.4: "Het totaal aantal
punten wordt per rubriek afgerond op 0,25 punt, waarbij vanaf een achtste
(1/8) punt naar boven wordt afgerond."

De package leest aan de doelgroep af dat de eenheid een zorgwoning is.

Bron: implementatietoelichting zelfstandige woonruimten, 2.12.1: "Wanneer
een eenheid de doelgroep Zorg heeft, wordt de woning automatisch als
zorgwoning gewaardeerd."

De eenheid heeft alleen de doelgroep zorg en een verwarmde woonkamer. De
test geeft geen eerder resultaat mee; de package waardeert de andere
rubrieken daarom zelf en waarschuwt voor de energieprestatie, de
monumenten, de pandsoort, de keuken, de WOZ-waarde en het bouwjaar die
ontbreken.

Bron: implementatietoelichting zelfstandige woonruimten, 2.12: "De extra
attributen in het model (zoals de WOZ-waarde, energielabel,
ruimtegegevens, etc.) zijn van belang omdat de 35% opslag voor zorgwoningen
wordt berekend over het totale puntenaantal van de rubrieken 1 t/m 11."

Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
genereert de package een `UserWarning`."

## Rapport

```text
BIJZONDERE VOORZIENINGEN
  Zorgwoning 35% puntenverhoging                                                 14.25 pt
                                                                                ------
  Totaal                                                                         14.25 pt
```

## Waarschuwingen

- UserWarning: Eenheid (zorgwoning): 'energieprestaties' is None
- UserWarning: Eenheid (zorgwoning): 'monumenten' is niet gespecificeerd. Indien de eenheid geen monumentstatus heeft, geef dit dan expliciet aan door een lege lijst toe te wijzen aan het 'monumenten'-attribuut.
- UserWarning: Eenheid (zorgwoning) heeft geen pandsoort Eengezinswoning of Meergezinswoning en komt daarom niet in aanmerking voor waardering onder stelselgroep Energieprestatie.
- UserWarning: Eenheid (zorgwoning) kan niet gewaardeerd worden voor stelselgroep Keuken omdat er geen keuken is gevonden.
- UserWarning: Eenheid (zorgwoning): geen WOZ-waarde aangeleverd
- UserWarning: Eenheid (zorgwoning): geen bouwjaar gevonden. Kan niet bepalen of woning onder nieuwbouw valt.

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
      "oppervlakte": 19.1488,
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
      "code": "ZEL",
      "naam": "Zelfstandige woonruimten"
    },
    "stelselgroep": {
      "code": "BIJ",
      "naam": "Bijzondere voorzieningen"
    }
  },
  "punten": 14.25,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "bijzondere_voorzieningen__zorgwoning_puntenverhoging",
        "naam": "Zorgwoning 35% puntenverhoging"
      },
      "punten": 14.25
    }
  ]
}
```
