# test_punten_per_m2_voor_een_energielabel_hangen_af_van_de_labelklasse[label_a3plus]

De punten per m² van de vertrekken voor een energielabel hangen af van de labelklasse.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.4; wettekst,
Bijlage I onder B, onderdeel 4.1.

## Rapport

```text
ENERGIEPRESTATIE
  A+++                                                               10.00 m²     9.50 pt
                                                                                ------
  Totaal                                                                          9.50 pt
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
      "begindatum": "2021-03-27",
      "einddatum": "2031-03-27",
      "label": {
        "code": "AP3",
        "naam": "A+++"
      }
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
  "punten": 9.5,
  "woningwaarderingen": [
    {
      "aantal": 10.0,
      "criterium": {
        "id": "energieprestatie__label",
        "naam": "A+++",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": 9.5
    }
  ]
}
```
