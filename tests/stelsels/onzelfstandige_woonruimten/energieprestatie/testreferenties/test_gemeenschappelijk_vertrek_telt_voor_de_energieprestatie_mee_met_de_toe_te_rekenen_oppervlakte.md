# test_gemeenschappelijk_vertrek_telt_voor_de_energieprestatie_mee_met_de_toe_te_rekenen_oppervlakte

Een gemeenschappelijk vertrek telt voor de energieprestatie mee met de oppervlakte die aan de huurder is toe te rekenen.

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.4.4
- wettekst, Bijlage I onder B, onderdeel 4.1
- wettekst, Bijlage I onder B, onderdeel 1

## Rapport

```text
ENERGIEPRESTATIE
  A                                                                  30.00 m²    19.50 pt
                                                                                ------
  Totaal                                                                         19.50 pt
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
      },
      "waarde": "0.9"
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
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 1
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
      "oppervlakte": 40.0,
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
  "punten": 19.5,
  "woningwaarderingen": [
    {
      "aantal": 30.0,
      "criterium": {
        "id": "energieprestatie__label",
        "naam": "A",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": 19.5
    }
  ]
}
```
