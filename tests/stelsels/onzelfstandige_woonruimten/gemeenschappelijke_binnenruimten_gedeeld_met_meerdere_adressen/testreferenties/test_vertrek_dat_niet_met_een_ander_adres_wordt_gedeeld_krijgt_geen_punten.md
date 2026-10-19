# test_vertrek_dat_niet_met_een_ander_adres_wordt_gedeeld_krijgt_geen_punten

Een gemeenschappelijk vertrek dat niet met een ander adres wordt gedeeld, krijgt in deze rubriek geen punten.

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.9.1
- wettekst, Bijlage I onder A, toelichting rubriek 9 (via Bijlage I onder B, toelichting, inleiding)

## Rapport

Geen waarderingen voor Gemeenschappelijke binnenruimten gedeeld met meerdere adressen.

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
      "oppervlakte": 10.0,
      "verwarmd": true,
      "verkoeld": true,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
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
      "oppervlakte": 10.0,
      "gedeeldMetAantalAdressen": 1,
      "verwarmd": true,
      "verkoeld": true,
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
      "code": "GBA",
      "naam": "Gemeenschappelijke binnenruimten gedeeld met meerdere adressen"
    }
  },
  "punten": 0.0,
  "woningwaarderingen": []
}
```
