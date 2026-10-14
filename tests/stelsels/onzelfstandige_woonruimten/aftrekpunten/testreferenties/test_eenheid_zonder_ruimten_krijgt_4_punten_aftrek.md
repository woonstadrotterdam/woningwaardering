# test_eenheid_zonder_ruimten_krijgt_4_punten_aftrek

Een eenheid zonder ruimten krijgt 4 punten aftrek.

Naar de letter van de wettekst is 0 m² minder dan 8 m², maar een eenheid
zonder ruimten is onvolledige input. De package geeft daar geen
waarschuwing voor. De test legt dat huidige gedrag vast.

Bron: wettekst, Bijlage I onder B, onderdeel 13: "Wanneer de totale
oppervlakte van vertrekken onder rubriek 1 minder is dan 8 m²", "– 4
punten".

Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
genereert de package een `UserWarning`."

## Rapport

```text
AFTREKPUNTEN
  Oppervlakte van vertrekken is minder dan 8 m²                       0.00 m²    -4.00 pt
                                                                                ------
  Totaal                                                                         -4.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{}
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
      "code": "AFT",
      "naam": "Aftrekpunten"
    }
  },
  "punten": -4.0,
  "woningwaarderingen": [
    {
      "aantal": 0.0,
      "criterium": {
        "id": "aftrekpunten__oppervlakte_van_vertrekken_minder_dan_8m2",
        "naam": "Oppervlakte van vertrekken is minder dan 8 m²",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": -4.0
    }
  ]
}
```
