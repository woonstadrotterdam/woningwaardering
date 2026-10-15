# test_toe_te_rekenen_oppervlakte_telt_onafgerond_mee_voor_de_energieprestatie

De oppervlakte die aan de huurder is toe te rekenen, telt voor de energieprestatie onafgerond mee.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.4; wettekst,
Bijlage I onder B, onderdeel 4.1.

## Rapport

```text
ENERGIEPRESTATIE
  A                                                                  20.50 m²    13.33 pt
  Afronding op kwartpunten                                                       -0.08 pt
                                                                                ------
  Totaal                                                                         13.25 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "bouwjaar": 1990,
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
      "begindatum": "2021-01-01",
      "einddatum": "2031-01-01",
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
      "oppervlakte": 10.4
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
      "oppervlakte": 40.4,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 4
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
  "punten": 13.25,
  "woningwaarderingen": [
    {
      "aantal": 20.5,
      "criterium": {
        "id": "energieprestatie__label",
        "naam": "A",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": 13.33
    },
    {
      "criterium": {
        "id": "energieprestatie__afronding_op_kwartpunten",
        "naam": "Afronding op kwartpunten"
      },
      "punten": -0.08
    }
  ]
}
```
