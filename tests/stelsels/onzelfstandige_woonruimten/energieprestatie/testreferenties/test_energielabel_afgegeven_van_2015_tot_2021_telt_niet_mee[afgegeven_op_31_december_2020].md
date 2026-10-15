# test_energielabel_afgegeven_van_2015_tot_2021_telt_niet_mee[afgegeven_op_31_december_2020]

Een energielabel dat is afgegeven van 1 januari 2015 tot 1 januari 2021, telt niet mee.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.3.

Zonder geldige energieprestatie bepaalt het bouwjaar de punten per m².

Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.5; wettekst,
Bijlage I onder B, onderdeel 4.1.

## Rapport

```text
ENERGIEPRESTATIE
  Bouwjaar 1970                                                      10.00 m²    -1.50 pt
                                                                                ------
  Totaal                                                                         -1.50 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "bouwjaar": 1970,
  "energieprestaties": [
    {
      "soort": {
        "code": "VEL",
        "naam": "Voorlopig energielabel"
      },
      "status": {
        "code": "DEF",
        "naam": "Definitief"
      },
      "begindatum": "2020-12-31",
      "einddatum": "2030-12-31",
      "label": {
        "code": "A",
        "naam": "A"
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
  "punten": -1.5,
  "woningwaarderingen": [
    {
      "aantal": 10.0,
      "criterium": {
        "id": "energieprestatie__bouwjaar",
        "naam": "Bouwjaar 1970",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": -1.5
    }
  ]
}
```
