# test_gemeenschappelijke_carport_of_parkeerplaats_wordt_niet_als_buitenruimte_gewaardeerd

Een gemeenschappelijke carport of parkeerplaats wordt niet als buitenruimte gewaardeerd.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.8.3; wettekst,
Bijlage I onder A, toelichting rubriek 8 (via Bijlage I onder B,
toelichting, inleiding).

## Rapport

Geen waarderingen voor Buitenruimten.

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "carport",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "CAR",
        "naam": "Carport"
      },
      "naam": "Carport",
      "oppervlakte": 12.0,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 3
    },
    {
      "id": "parkeerplaats",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "PAR",
        "naam": "Parkeerplaats"
      },
      "naam": "Parkeerplaats",
      "oppervlakte": 12.0,
      "gedeeldMetAantalAdressen": 2
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
      "code": "BUI",
      "naam": "Buitenruimten"
    }
  },
  "punten": 0.0,
  "woningwaarderingen": []
}
```
