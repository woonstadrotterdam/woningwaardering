# test_precies_8m2_aan_vertrekken_geeft_geen_aftrek

Een totale oppervlakte van vertrekken van precies 8 m² geeft geen aftrek.

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.13
- wettekst, Bijlage I onder B, onderdeel 13

## Rapport

Geen waarderingen voor Aftrekpunten.

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "keuken",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "KEU",
        "naam": "Keuken"
      },
      "naam": "Keuken",
      "oppervlakte": 8.0
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
  "punten": 0.0,
  "woningwaarderingen": []
}
```
