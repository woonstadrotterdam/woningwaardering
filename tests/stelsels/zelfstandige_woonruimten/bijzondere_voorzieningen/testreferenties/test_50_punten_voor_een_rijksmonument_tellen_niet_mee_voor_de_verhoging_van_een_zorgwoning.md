# test_50_punten_voor_een_rijksmonument_tellen_niet_mee_voor_de_verhoging_van_een_zorgwoning

De 50 punten voor een rijksmonument met een huurovereenkomst van 1 januari 2024 tellen niet mee in de punten waarover een zorgwoning 35% verhoging krijgt.

De 50 punten komen op grond van artikel 8a bij de waardering. De verhoging
voor een zorgwoning is een percentage van de punten van de onderdelen 1 tot
en met 11.1.

Bron: wettekst, artikel 8a, tweede lid: "Indien de woonruimte bestaat uit
of deel uitmaakt van een rijksmonument als bedoeld in artikel 1.1 van de
Erfgoedwet en de huurovereenkomst betreffende die woonruimte is afgesloten
voor het tijdstip van inwerkingtreding van de Wet betaalbare huur, wordt de
waardering voor een zelfstandige woonruimte in bijlage I, onder A, met 50
punten vermeerderd en de waardering voor een onzelfstandige woonruimte in
bijlage I, onder B, met 10 punten vermeerderd."

Bron: wettekst, Bijlage I onder A, rubriek 12: "bij: 35% van de ingevolge
de onderdelen 1 tot en met 11.1 toegekende punten."

De eenheid heeft de doelgroep zorg, de monumentstatus, de datum van de
huurovereenkomst, een bouwjaar en een verwarmde woonkamer. De test geeft
geen eerder resultaat mee; de package waardeert de andere rubrieken daarom
zelf en waarschuwt voor de energieprestatie, de pandsoort, de keuken en de
WOZ-waarde die ontbreken.

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
- UserWarning: Eenheid (zorgwoning) heeft geen pandsoort Eengezinswoning of Meergezinswoning en komt daarom niet in aanmerking voor waardering onder stelselgroep Energieprestatie.
- UserWarning: Eenheid (zorgwoning) kan niet gewaardeerd worden voor stelselgroep Keuken omdat er geen keuken is gevonden.
- UserWarning: Eenheid (zorgwoning): geen WOZ-waarde aangeleverd

## Input

```json
{
  "id": "zorgwoning",
  "bouwjaar": 1960,
  "doelgroep": {
    "code": "ZOR",
    "naam": "Zorg"
  },
  "monumenten": [
    {
      "code": "RIJ",
      "naam": "Rijksmonument"
    }
  ],
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
  ],
  "datumAfsluitenHuurovereenkomst": "2024-01-01"
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
