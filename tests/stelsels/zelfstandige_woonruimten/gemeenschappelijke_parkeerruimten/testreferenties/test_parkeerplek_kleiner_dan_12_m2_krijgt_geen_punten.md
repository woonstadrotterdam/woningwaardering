# test_parkeerplek_kleiner_dan_12_m2_krijgt_geen_punten

Een parkeerplek met een oppervlakte onder 12 m² krijgt geen punten.

Bron: implementatietoelichting zelfstandige woonruimten, 2.10.3; wettekst,
Bijlage I onder A, toelichting rubriek 10.

## Rapport

Geen waarderingen voor Gemeenschappelijke parkeerruimten.

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "parkeerplek_buiten_behorend_bij_complex",
      "soort": {
        "code": "GEM",
        "naam": "Gemeenschappelijke ruimten en voorzieningen"
      },
      "detailSoort": {
        "code": "PBC",
        "naam": "Parkeerplek buiten behorend bij complex"
      },
      "naam": "Parkeerplek buiten behorend bij complex",
      "oppervlakte": 11.0,
      "gedeeldMetAantalAdressen": 10,
      "aantal": 2
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
      "code": "GPA",
      "naam": "Gemeenschappelijke parkeerruimten"
    }
  },
  "punten": 0.0,
  "woningwaarderingen": []
}
```
