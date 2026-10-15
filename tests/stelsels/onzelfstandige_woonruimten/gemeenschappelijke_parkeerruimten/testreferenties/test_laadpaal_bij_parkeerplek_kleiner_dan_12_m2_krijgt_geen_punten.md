# test_laadpaal_bij_parkeerplek_kleiner_dan_12_m2_krijgt_geen_punten

Een laadpaal bij een parkeerplek met een oppervlakte onder 12 m² krijgt in deze rubriek geen punten.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.10.5;
implementatietoelichting onzelfstandige woonruimten, 2.10.3; wettekst,
Bijlage I onder A, toelichting rubriek 10 (via Bijlage I onder B,
toelichting, inleiding).

## Rapport

Geen waarderingen voor Gemeenschappelijke parkeerruimten.

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
      "oppervlakte": 10.0,
      "gedeeldMetAantalAdressen": 3,
      "bouwkundigeElementen": [
        {
          "id": "laadpaal",
          "naam": "Laadpaal",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "LAA",
            "naam": "Laadpaal"
          }
        }
      ],
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 1
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
      "code": "GPA",
      "naam": "Gemeenschappelijke parkeerruimten"
    }
  },
  "punten": 0.0,
  "woningwaarderingen": []
}
```
