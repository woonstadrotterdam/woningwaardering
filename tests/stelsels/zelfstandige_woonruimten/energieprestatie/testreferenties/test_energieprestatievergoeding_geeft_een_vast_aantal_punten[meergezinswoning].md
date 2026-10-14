# test_energieprestatievergoeding_geeft_een_vast_aantal_punten[meergezinswoning]

Bij een energieprestatievergoeding krijgt een eengezinswoning 32 punten en een meergezinswoning 28 punten.

Bron: wettekst, Bijlage I onder A, onderdeel 4.3: "In de gevallen waarin een
energieprestatievergoeding als bedoeld in artikel 237 van boek 7 van het
Burgerlijk Wetboek is overeengekomen, wordt in afwijking van bovenstaande
tabel het volgende aantal punten toegekend: Eengezinswoning
Meergezinswoning/duplexwoning 32 28".

## Rapport

```text
ENERGIEPRESTATIE
  Energieprestatievergoeding Meergezinswoning                                    28.00 pt
                                                                                ------
  Totaal                                                                         28.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "bouwjaar": 1921,
  "energieprestaties": [
    {
      "soort": {
        "code": "EI",
        "naam": "Energie-index"
      },
      "status": {
        "code": "DEF",
        "naam": "Definitief"
      },
      "begindatum": "2017-02-23",
      "einddatum": "2027-02-23",
      "label": {
        "code": "C",
        "naam": "C"
      },
      "waarde": "1.48"
    }
  ],
  "monumenten": [],
  "panden": [
    {
      "soort": {
        "code": "MGW",
        "naam": "Meergezinswoning"
      }
    }
  ],
  "prijscomponenten": [
    {
      "detailSoort": {
        "code": "EPV",
        "naam": "Energieprestatievergoeding"
      }
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
      "code": "ENE",
      "naam": "Energieprestatie"
    }
  },
  "punten": 28.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "energieprestatie__energieprestatievergoeding",
        "naam": "Energieprestatievergoeding Meergezinswoning"
      },
      "punten": 28.0
    }
  ]
}
```
