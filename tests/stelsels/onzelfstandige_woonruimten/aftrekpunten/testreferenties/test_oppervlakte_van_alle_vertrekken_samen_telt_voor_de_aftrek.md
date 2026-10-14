# test_oppervlakte_van_alle_vertrekken_samen_telt_voor_de_aftrek

Voor de aftrek telt de oppervlakte van alle vertrekken samen, zodat twee vertrekken van 4 m² geen aftrek geven.

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
      "id": "slaapkamer1",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer1",
      "oppervlakte": 4.0
    },
    {
      "id": "slaapkamer2",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer2",
      "oppervlakte": 4.0
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
