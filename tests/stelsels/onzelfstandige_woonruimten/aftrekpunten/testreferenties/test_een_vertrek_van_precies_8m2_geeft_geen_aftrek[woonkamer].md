# test_een_vertrek_van_precies_8m2_geeft_geen_aftrek[woonkamer]

Een woonruimte met één privévertrek van precies 8 m² krijgt geen aftrek.

Bron: wettekst, Bijlage I onder B, onderdeel 13: "Wanneer de totale
oppervlakte van vertrekken onder rubriek 1 minder is dan 8 m²", "– 4
punten".

## Rapport

Geen waarderingen voor Aftrekpunten.

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
