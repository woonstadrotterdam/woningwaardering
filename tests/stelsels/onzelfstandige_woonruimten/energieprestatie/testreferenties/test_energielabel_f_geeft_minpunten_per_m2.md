# test_energielabel_f_geeft_minpunten_per_m2

Een energielabel F geeft 0,10 minpunt per m² van de vertrekken.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.4; wettekst,
Bijlage I onder B, onderdeel 4.1.

## Rapport

```text
ENERGIEPRESTATIE
  F                                                                   9.00 m²    -0.90 pt
  Afronding op kwartpunten                                                       -0.10 pt
                                                                                ------
  Totaal                                                                         -1.00 pt
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
        "code": "F",
        "naam": "F"
      },
      "waarde": "160.92"
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
      "oppervlakte": 20.0,
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
      "oppervlakte": 30.0,
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
  "punten": -1.0,
  "woningwaarderingen": [
    {
      "aantal": 9.0,
      "criterium": {
        "id": "energieprestatie__label",
        "naam": "F",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": -0.9
    },
    {
      "criterium": {
        "id": "energieprestatie__afronding_op_kwartpunten",
        "naam": "Afronding op kwartpunten"
      },
      "punten": -0.1
    }
  ]
}
```
