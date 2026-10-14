# test_punten_voor_een_energie_index_hangen_af_van_de_klasse[index_2_71]

De punten voor een energie-index hangen af van de klasse waarin de index valt.

Elke index ligt op de bovengrens van zijn klasse, behalve 2,71. De
energieprestaties hebben geen label, zodat alleen de index de punten
bepaalt. De grenzen bij A++ en E staan er niet in: daar verschillen de
bronnen.

Bron: wettekst, Bijlage I onder A, onderdeel 4.1, tabel met de kolommen
energielabel, energie-index, bouwjaar, eengezinswoning en meergezinswoning:
"A+ 0,6 < EI ≤ 0,8 n.v.t. 47 43", "A 0,8 < EI ≤ 1,2 2002 en later 41 37",
"B 1,2 < EI ≤ 1,4 2000 t/m 2001 34 30", "C 1,4 < EI ≤ 1,8 1992 t/m 1999 22
15", "D 1,8 < EI ≤ 2,1 1984 t/m 1991 14 11", "F 2,4 < EI ≤ 2,7 1977 t/m
1978 –9 –9" en "G EI > 2,7 1976 of ouder –15 –15".

## Rapport

```text
ENERGIEPRESTATIE
  Energie-index                                                                 -15.00 pt
                                                                                ------
  Totaal                                                                        -15.00 pt
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
      "begindatum": "2020-08-01",
      "einddatum": "2030-08-01",
      "waarde": "2.71"
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
  "punten": -15.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "energieprestatie__label",
        "naam": "Energie-index"
      },
      "punten": -15.0
    }
  ]
}
```
