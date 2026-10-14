# test_schuur_aangeleverd_als_vertrek_is_een_vertrek

Een schuur die als vertrek is aangeleverd, wordt als vertrek gewaardeerd.

Bron: implementatietoelichting zelfstandige woonruimten, 2.2.1.2: "De
gespecificeerde ruimtesoort is leidend bij de waardering van een ruimte,
voor de `Ruimtedetailsoorten` die tot rubriek 1 of 2 kunnen horen."

## Rapport

```text
OPPERVLAKTE VAN VERTREKKEN
  Schuur                                                              6.00 m²
                                                                    ------      ------
  Totaal                                                              6.00 m²     6.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "schuur",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SCH",
        "naam": "Schuur"
      },
      "naam": "Schuur",
      "oppervlakte": 6.0
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
      "code": "OVZ",
      "naam": "Oppervlakte van vertrekken"
    }
  },
  "punten": 6.0,
  "woningwaarderingen": [
    {
      "aantal": 6.0,
      "criterium": {
        "id": "oppervlakte_van_vertrekken__schuur",
        "naam": "Schuur",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    }
  ]
}
```
