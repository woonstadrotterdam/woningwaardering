# test_energieprestatie_zonder_soort_telt_niet_mee

Een energieprestatie zonder soort telt niet mee: het bouwjaar bepaalt de punten per m².

Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.3;
implementatietoelichting onzelfstandige woonruimten, 2.4.5; wettekst,
Bijlage I onder B, onderdeel 4.1.

## Rapport

```text
ENERGIEPRESTATIE
  Bouwjaar 1921                                                       3.67 m²    -0.55 pt
  Afronding op kwartpunten                                                        0.05 pt
                                                                                ------
  Totaal                                                                         -0.50 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "bouwjaar": 1921,
  "energieprestaties": [
    {
      "status": {
        "code": "DEF",
        "naam": "Definitief"
      },
      "begindatum": "2017-02-23",
      "einddatum": "2027-02-23",
      "label": {
        "naam": "C"
      },
      "waarde": "1.48"
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
  "punten": -0.5,
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
        "id": "energieprestatie__afronding_op_kwartpunten",
        "naam": "Afronding op kwartpunten"
      },
      "punten": 0.05
    }
  ]
}
```
