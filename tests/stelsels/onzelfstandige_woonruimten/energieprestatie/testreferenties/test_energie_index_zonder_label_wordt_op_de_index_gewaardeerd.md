# test_energie_index_zonder_label_wordt_op_de_index_gewaardeerd

Een energie-index zonder label bepaalt de punten per m².

Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.2;
implementatietoelichting onzelfstandige woonruimten, 2.4.4; wettekst,
Bijlage I onder B, onderdeel 4.1.

## Rapport

```text
ENERGIEPRESTATIE
  Energie-index                                                       3.67 m²     2.38 pt
  Afronding op kwartpunten                                                        0.12 pt
                                                                                ------
  Totaal                                                                          2.50 pt
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
        "code": "EI",
        "naam": "Energie-index"
      },
      "status": {
        "code": "DEF",
        "naam": "Definitief"
      },
      "begindatum": "2018-06-01",
      "einddatum": "2028-06-01",
      "waarde": "1.0"
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
  "punten": 2.5,
  "woningwaarderingen": [
    {
      "aantal": 3.67,
      "criterium": {
        "id": "energieprestatie__label",
        "naam": "Energie-index",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": 2.38
    },
    {
      "criterium": {
        "id": "energieprestatie__afronding_op_kwartpunten",
        "naam": "Afronding op kwartpunten"
      },
      "punten": 0.12
    }
  ]
}
```
