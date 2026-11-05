# test_eenheid_zonder_recente_woz_waarde_krijgt_met_waarschuwing_het_laagste_puntenaantal

Een eenheid zonder recente WOZ-waarde krijgt met een waarschuwing het laagste puntenaantal van 10 punten.

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.11.1

De package beschouwt alleen een WOZ-waarde met waardepeildatum 1 januari van
een van de twee jaren vóór de peildatum van de procedure als relevant.

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.11.1
- wettekst, Bijlage I onder B, toelichting rubriek 11

## Rapport

```text
PUNTEN VOOR DE WOZ-WAARDE
  Geen WOZ-waarde bekend                                                         10.00 pt
                                                                                ------
  Totaal                                                                         10.00 pt
```

## Waarschuwingen

- UserWarning: Eenheid eenheid: geen WOZ-waarde gevonden met waardepeildatum 01-01-2025 of 01-01-2024

## Input

```json
{
  "id": "eenheid",
  "adres": {
    "woonplaats": {
      "code": "3086",
      "naam": "ROTTERDAM"
    }
  },
  "adresseerbaarObjectBasisregistratie": {
    "bagGebruikersOppervlakte": 58
  },
  "wozEenheden": [
    {
      "vastgesteldeWaarde": 124000.0,
      "waardepeildatum": "2023-01-01"
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
      "code": "WOZ",
      "naam": "Punten voor de WOZ-waarde"
    }
  },
  "punten": 10.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "punten_voor_de_woz_waarde__geen_woz_waarde_bekend",
        "naam": "Geen WOZ-waarde bekend"
      },
      "punten": 10.0
    }
  ]
}
```
