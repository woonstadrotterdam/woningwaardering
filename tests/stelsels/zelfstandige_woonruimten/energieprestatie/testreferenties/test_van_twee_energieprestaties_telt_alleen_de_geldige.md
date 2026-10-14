# test_van_twee_energieprestaties_telt_alleen_de_geldige

Van twee energieprestaties bepaalt alleen de geldige de punten.

Bron: beleidsboek zelfstandige woonruimten, 2.4.2: "De woonruimte krijgt
punten voor de energieprestatie als de woning een geldend energielabel of
energie-index heeft."

Het eerste energielabel is op twee gronden niet geldig: het is op de
peildatum vervallen en het is afgegeven in 2019.

Bron: beleidsboek zelfstandige woonruimten, 2.4.3: "Aan een vervallen
energielabel of energie-index wordt geen waardering toegekend.", "Een
energielabel dat is afgegeven in de periode van 1 januari 2015 tot 1 januari
2021 krijgt geen punten in het woningwaarderingsstelsel."

Bron: implementatietoelichting zelfstandige woonruimten, 2.4.3: "De
peildatum moet vallen tussen begindatum en einddatum."

Het geldige energielabel A geeft een meergezinswoning 37 punten.

Bron: wettekst, Bijlage I onder A, onderdeel 4.1, tabel met de kolommen
energielabel, energie-index, bouwjaar, eengezinswoning en meergezinswoning:
"A 0,8 < EI ≤ 1,2 2002 en later 41 37".

## Rapport

```text
ENERGIEPRESTATIE
  A                                                                              37.00 pt
                                                                                ------
  Totaal                                                                         37.00 pt
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
      "begindatum": "2019-03-27",
      "einddatum": "2021-03-27",
      "label": {
        "code": "F",
        "naam": "F"
      },
      "waarde": "160"
    },
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
        "code": "A",
        "naam": "A"
      },
      "waarde": "170"
    }
  ],
  "monumenten": [],
  "panden": [
    {
      "soort": {
        "code": "MGW",
        "naam": "Meergezinswoning"
      }
    }
  ]
}
```

## Output

```json
{
  "criteriumGroep": {
    "stelsel": {
      "code": "ZEL",
      "naam": "Zelfstandige woonruimten"
    },
    "stelselgroep": {
      "code": "ENE",
      "naam": "Energieprestatie"
    }
  },
  "punten": 37.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "energieprestatie__label",
        "naam": "A"
      },
      "punten": 37.0
    }
  ]
}
```
