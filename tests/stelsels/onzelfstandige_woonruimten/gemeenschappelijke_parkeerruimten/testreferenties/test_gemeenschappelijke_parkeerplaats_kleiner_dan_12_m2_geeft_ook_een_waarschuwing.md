# test_gemeenschappelijke_parkeerplaats_kleiner_dan_12_m2_geeft_ook_een_waarschuwing

Een gemeenschappelijke parkeerplaats geeft de waarschuwing over haar detailsoort ook wanneer zij met een oppervlakte onder 12 m² geen punten krijgt.

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.10.3
- wettekst, Bijlage I onder A, toelichting rubriek 10 (via Bijlage I onder B, toelichting, inleiding)

## Rapport

Geen waarderingen voor Gemeenschappelijke parkeerruimten.

## Waarschuwingen

- UserWarning: Ruimte 'Parkeerplaats' (parkeerplaats) is een gemeenschappelijke Parkeerplaats (PAR). Gebruik Type I, II of III (Parkeerplek in inpandige afgesloten parkeergarage (PIP), Parkeerplek in uitpandige afgesloten parkeergarage (PUP), Parkeerplek buiten met dak behorend bij complex (PBD) of Parkeerplek buiten behorend bij complex (PBC)) voor een gemeenschappelijke parkeerplek: deze wordt nu gewaardeerd als Type III.

## Input

```json
{
  "ruimten": [
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
      "oppervlakte": 11.99,
      "gedeeldMetAantalAdressen": 3,
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
