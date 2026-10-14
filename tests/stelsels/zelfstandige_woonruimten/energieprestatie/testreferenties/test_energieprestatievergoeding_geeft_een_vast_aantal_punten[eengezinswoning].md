# test_energieprestatievergoeding_geeft_een_vast_aantal_punten[eengezinswoning]

Bij een energieprestatievergoeding krijgt een eengezinswoning 32 punten en een meergezinswoning 28 punten.

Bron: wettekst, Bijlage I onder A, onderdeel 4.3: "In de gevallen waarin een
energieprestatievergoeding als bedoeld in artikel 237 van boek 7 van het
Burgerlijk Wetboek is overeengekomen, wordt in afwijking van bovenstaande
tabel het volgende aantal punten toegekend: Eengezinswoning
Meergezinswoning/duplexwoning 32 28".

## Rapport

```text
ENERGIEPRESTATIE
  Energieprestatievergoeding Eengezinswoning                                     32.00 pt
                                                                                ------
  Totaal                                                                         32.00 pt
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
        "code": "EGW",
        "naam": "Eengezinswoning"
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
  "punten": 32.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "energieprestatie__energieprestatievergoeding",
        "naam": "Energieprestatievergoeding Eengezinswoning"
      },
      "punten": 32.0
    }
  ]
}
```
