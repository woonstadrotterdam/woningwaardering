# test_rijksmonument_met_pluspunten_krijgt_geen_correctie

Een rijksmonument met een positief aantal punten voor de energieprestatie houdt die punten.

Bron: wettekst, Bijlage I onder A, onderdeel 4.2: "Indien de woonruimte
bestaat uit of deel uitmaakt van een rijksmonument, een provinciaal monument
of een gemeentelijke monument als bedoeld in artikel 8a worden voor deze
rubriek geen minpunten toegekend."

De punten komen hier uit de energieprestatievergoeding van een
eengezinswoning.

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
  "monumenten": [
    {
      "code": "RIJ",
      "naam": "Rijksmonument"
    }
  ],
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
