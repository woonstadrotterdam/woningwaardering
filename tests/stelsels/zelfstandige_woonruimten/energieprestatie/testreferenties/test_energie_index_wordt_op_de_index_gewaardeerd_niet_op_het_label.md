# test_energie_index_wordt_op_de_index_gewaardeerd_niet_op_het_label

Een energie-index uit 2020 wordt gewaardeerd op de index, niet op het label dat erbij is meegegeven.

Bron: beleidsboek zelfstandige woonruimten, 2.4.4: "Bij een energie-index
wordt het puntenaantal bepaald door het relevante cijfer."

Een energie-index van 1,48 geeft een eengezinswoning 22 punten; het
meegegeven label A zou 41 punten geven.

Bron: wettekst, Bijlage I onder A, onderdeel 4.1, tabel met de kolommen
energielabel, energie-index, bouwjaar, eengezinswoning en meergezinswoning:
"C 1,4 < EI ≤ 1,8 1992 t/m 1999 22 15", "A 0,8 < EI ≤ 1,2 2002 en later 41
37".

## Rapport

```text
ENERGIEPRESTATIE
  A -> C (Energie-index)                                                         22.00 pt
                                                                                ------
  Totaal                                                                         22.00 pt
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
      "label": {
        "code": "A",
        "naam": "A"
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
  "punten": 22.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "energieprestatie__label",
        "naam": "A -> C (Energie-index)"
      },
      "punten": 22.0
    }
  ]
}
```
