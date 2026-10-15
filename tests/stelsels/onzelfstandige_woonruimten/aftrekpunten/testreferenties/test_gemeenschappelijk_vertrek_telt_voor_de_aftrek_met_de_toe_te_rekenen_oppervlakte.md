# test_gemeenschappelijk_vertrek_telt_voor_de_aftrek_met_de_toe_te_rekenen_oppervlakte

Een gemeenschappelijk vertrek telt voor de aftrek mee met de oppervlakte die aan de huurder is toe te rekenen.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.1; wettekst,
Bijlage I onder B, toelichting rubriek 1.

Minder dan 8 m² aan vertrekken geeft 4 punten aftrek.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.13; wettekst,
Bijlage I onder B, onderdeel 13.

## Rapport

```text
AFTREKPUNTEN
  Oppervlakte van vertrekken is minder dan 8 m²                       6.00 m²    -4.00 pt
                                                                                ------
  Totaal                                                                         -4.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
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
      "oppervlakte": 12.0,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
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
      "code": "AFT",
      "naam": "Aftrekpunten"
    }
  },
  "punten": -4.0,
  "woningwaarderingen": [
    {
      "aantal": 6.0,
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
