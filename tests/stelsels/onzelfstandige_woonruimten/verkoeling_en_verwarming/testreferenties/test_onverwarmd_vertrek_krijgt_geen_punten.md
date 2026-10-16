# test_onverwarmd_vertrek_krijgt_geen_punten

Een vertrek zonder verwarming krijgt geen punten.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.3;
wettekst, Bijlage I onder B, onderdeel 3.

## Rapport

Geen waarderingen voor Verkoeling en verwarming.

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "keuken1",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "KEU",
        "naam": "Keuken"
      },
      "naam": "Keuken1",
      "oppervlakte": 10.0,
      "verwarmd": false
    },
    {
      "id": "keuken2",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "KEU",
        "naam": "Keuken"
      },
      "naam": "Keuken2",
      "oppervlakte": 10.0,
      "verwarmd": false,
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
      "code": "VKV",
      "naam": "Verkoeling en verwarming"
    }
  },
  "punten": 0.0,
  "woningwaarderingen": []
}
```
