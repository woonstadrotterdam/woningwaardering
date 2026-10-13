# test_gemeenschappelijke_parkeerplaats_kleiner_dan_12_m2_geeft_ook_een_waarschuwing

Een gemeenschappelijke parkeerplaats geeft de waarschuwing over haar detailsoort ook wanneer zij met een oppervlakte onder 12 m² geen punten krijgt.

Dat de waarschuwing ook onder 12 m² volgt, is een keuze van de package die
in geen bron staat.

Bron: implementatietoelichting zelfstandige woonruimten, 2.10.3: "Bij die
laatste volgt een `UserWarning` dat een Type-detailsoort meer op zijn plaats
is: `PAR` legt het type niet vast."

Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
genereert de package een `UserWarning`."

Bron: wettekst, Bijlage I onder A, toelichting rubriek 10: "Een parkeerplek
is een afgebakend vak en heeft een oppervlakte van minimaal 12 m² waar een
gangbare personenauto in zijn geheel op past."

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
      ]
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
