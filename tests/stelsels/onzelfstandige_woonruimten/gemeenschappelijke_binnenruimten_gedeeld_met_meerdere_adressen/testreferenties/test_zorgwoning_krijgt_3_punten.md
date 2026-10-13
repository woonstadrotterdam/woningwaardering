# test_zorgwoning_krijgt_3_punten

Een zorgwoning krijgt 3 punten voor de gemeenschappelijke ruimten en voorzieningen.

Bron: beleidsboek onzelfstandige woonruimten, 2.9.4: "Om arbeidsintensief
meetwerk te voorkomen kent de Huurcommissie in dat geval een waardering van
3 punten per woning toe."

De eenheid heeft de doelgroep zorg en alleen een eigen woonkamer. De
gemeenschappelijke ruimten zijn niet meegegeven; het scenario toont
daardoor niet dat de 3 punten in de plaats komen van hun waardering.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.6.1: "Bij een
zorgwoning tellen ruimten gedeeld met meerdere adressen niet mee, omdat die
stelselgroep daar door een vaste waardering wordt vervangen."

De package leest een zorgwoning af aan de doelgroep van de eenheid. De
implementatietoelichting voor onzelfstandige woonruimten noemt dat niet;
die voor zelfstandige woonruimten wel.

Bron: implementatietoelichting zelfstandige woonruimten, 2.12.1: "Wanneer
een eenheid de doelgroep Zorg heeft, wordt de woning automatisch als
zorgwoning gewaardeerd."

## Rapport

```text
GEMEENSCHAPPELIJKE BINNENRUIMTEN GEDEELD MET MEERDERE ADRESSEN
  Zorgwoning                                                                      3.00 pt
                                                                                ------
  Totaal                                                                          3.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
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
      "oppervlakte": 10.0
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
      "code": "GBA",
      "naam": "Gemeenschappelijke binnenruimten gedeeld met meerdere adressen"
    }
  },
  "punten": 3.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__zorgwoning",
        "naam": "Zorgwoning"
      },
      "punten": 3.0
    }
  ]
}
```
