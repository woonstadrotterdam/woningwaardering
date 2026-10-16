# test_monument_krijgt_geen_minpunten[gemeentelijk_monument]

Een rijks-, provinciaal of gemeentelijk monument krijgt geen minpunten voor de energieprestatie.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.6.1;
wettekst, Bijlage I onder B, onderdeel 4.2.

## Rapport

```text
ENERGIEPRESTATIE
  Bouwjaar 1921                                                      10.00 m²    -1.50 pt
  Correctie monument                                                              1.50 pt
                                                                                ------
  Totaal                                                                          0.00 pt
```

## Waarschuwingen

- UserWarning: Eenheid (eenheid): 'energieprestaties' is None

## Input

```json
{
  "id": "eenheid",
  "bouwjaar": 1921,
  "energieprestaties": [],
  "monumenten": [
    {
      "code": "GEM",
      "naam": "Gemeentelijk monument"
    }
  ],
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
  "punten": 0.0,
  "woningwaarderingen": [
    {
      "aantal": 10.0,
      "criterium": {
        "id": "energieprestatie__bouwjaar",
        "naam": "Bouwjaar 1921",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": -1.5
    },
    {
      "criterium": {
        "id": "energieprestatie__correctie_monument",
        "naam": "Correctie monument"
      },
      "punten": 1.5
    }
  ]
}
```
