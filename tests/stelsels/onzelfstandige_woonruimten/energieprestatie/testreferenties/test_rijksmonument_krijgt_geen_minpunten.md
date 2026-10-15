# test_rijksmonument_krijgt_geen_minpunten

Een rijksmonument krijgt geen minpunten voor de energieprestatie.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.6.1;
wettekst, Bijlage I onder B, onderdeel 4.2.

## Rapport

```text
ENERGIEPRESTATIE
  Bouwjaar 1921                                                       3.67 m²    -0.55 pt
  Correctie monument                                                              0.55 pt
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
      "code": "RIJ",
      "naam": "Rijksmonument"
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
      "oppervlakte": 10.0,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 5
    },
    {
      "id": "woonkamer",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "WOO",
        "naam": "Woonkamer"
      },
      "naam": "Woonkamer",
      "oppervlakte": 10.0,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 6
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
      "aantal": 3.67,
      "criterium": {
        "id": "energieprestatie__bouwjaar",
        "naam": "Bouwjaar 1921",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": -0.55
    },
    {
      "criterium": {
        "id": "energieprestatie__correctie_monument",
        "naam": "Correctie monument"
      },
      "punten": 0.55
    }
  ]
}
```
