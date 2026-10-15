# test_parkeerplek_zonder_oppervlakte_geeft_een_waarschuwing

Een parkeerplek zonder oppervlakte geeft een waarschuwing over incomplete input.

## Rapport

Geen waarderingen voor Gemeenschappelijke parkeerruimten.

## Waarschuwingen

- UserWarning: Ruimte 'Parkeerplek' (parkeerplek) heeft geen oppervlakte

## Input

```json
{
  "ruimten": [
    {
      "id": "parkeerplek",
      "soort": {
        "code": "GEM",
        "naam": "Gemeenschappelijke ruimten en voorzieningen"
      },
      "detailSoort": {
        "code": "PBC",
        "naam": "Parkeerplek buiten behorend bij complex"
      },
      "naam": "Parkeerplek",
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
