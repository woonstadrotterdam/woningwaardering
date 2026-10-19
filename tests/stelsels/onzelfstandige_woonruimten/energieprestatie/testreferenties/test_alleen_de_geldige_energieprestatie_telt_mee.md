# test_alleen_de_geldige_energieprestatie_telt_mee

Alleen een geldige energieprestatie bepaalt de punten per m² van de vertrekken.

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.4.3
- wettekst, Bijlage I onder B, onderdeel 4.1

## Rapport

```text
ENERGIEPRESTATIE
  A                                                                  10.00 m²     6.50 pt
                                                                                ------
  Totaal                                                                          6.50 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "bouwjaar": 1993,
  "energieprestaties": [
    {
      "soort": {
        "code": "NTA",
        "naam": "Energielabel conform NTA8800"
      },
      "status": {
        "code": "DEF",
        "naam": "Definitief"
      },
      "begindatum": "2014-03-27",
      "einddatum": "2024-03-27",
      "label": {
        "code": "F",
        "naam": "F"
      },
      "waarde": "160"
    },
    {
      "soort": {
        "code": "NTA",
        "naam": "Energielabel conform NTA8800"
      },
      "status": {
        "code": "DEF",
        "naam": "Definitief"
      },
      "begindatum": "2021-03-27",
      "einddatum": "2031-03-27",
      "label": {
        "code": "A",
        "naam": "A"
      },
      "waarde": "170"
    }
  ],
  "monumenten": [],
  "ruimten": [
    {
      "id": "slaapkamer",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer",
      "oppervlakte": 10.0
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
      "code": "ENE",
      "naam": "Energieprestatie"
    }
  },
  "punten": 6.5,
  "woningwaarderingen": [
    {
      "aantal": 10.0,
      "criterium": {
        "id": "energieprestatie__label",
        "naam": "A",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": 6.5
    }
  ]
}
```
