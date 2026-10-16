# test_open_parkeergarage_niet_specifieke_plek_geeft_een_waarschuwing

Een ruimte met de detailsoort open parkeergarage, niet specifieke plek, geeft een waarschuwing dat een andere detailsoort nodig is.

Bron: implementatietoelichting datamodel-uitbreidingen,
"Parkeergelegenheden".

## Rapport

Geen waarderingen voor Gemeenschappelijke parkeerruimten.

## Waarschuwingen

- UserWarning: Ruimte 'Open parkeergarage niet specifieke plek' (open_parkeergarage_niet_specifieke_plek) heeft als ruimtedetailsoort Open parkeergarage niet specifieke plek (OPN). Gebruik Parkeerplek in inpandige afgesloten parkeergarage (PIP), Parkeerplek in uitpandige afgesloten parkeergarage (PUP), Parkeerplek buiten met dak behorend bij complex (PBD), Parkeerplek buiten behorend bij complex (PBC) of Carport (CAR) als detailsoort om in aanmerking te komen voor een waardering onder Gemeenschappelijke parkeerruimten.

## Input

```json
{
  "ruimten": [
    {
      "id": "open_parkeergarage_niet_specifieke_plek",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "OPN",
        "naam": "Open parkeergarage niet specifieke plek"
      },
      "naam": "Open parkeergarage niet specifieke plek",
      "oppervlakte": 100.0,
      "gedeeldMetAantalAdressen": 10,
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
      "code": "GPA",
      "naam": "Gemeenschappelijke parkeerruimten"
    }
  },
  "punten": 0.0,
  "woningwaarderingen": []
}
```
