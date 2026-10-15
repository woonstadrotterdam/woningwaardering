# test_energielabel_afgegeven_van_2015_tot_2021_telt_niet_mee

Een energielabel dat is afgegeven van 1 januari 2015 tot 1 januari 2021 telt niet mee: het bouwjaar bepaalt de punten per m².

Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.3;
implementatietoelichting onzelfstandige woonruimten, 2.4.5; wettekst,
Bijlage I onder B, onderdeel 4.1.

## Rapport

```text
ENERGIEPRESTATIE
  Bouwjaar 1970                                                       3.67 m²    -0.55 pt
  Afronding op kwartpunten                                                        0.05 pt
                                                                                ------
  Totaal                                                                         -0.50 pt
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
      "begindatum": "2018-06-01",
      "einddatum": "2028-06-01",
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
        "naam": "Bouwjaar 1970",
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
