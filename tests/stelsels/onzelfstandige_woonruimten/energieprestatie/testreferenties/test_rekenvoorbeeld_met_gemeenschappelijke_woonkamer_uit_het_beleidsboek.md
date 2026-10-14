# test_rekenvoorbeeld_met_gemeenschappelijke_woonkamer_uit_het_beleidsboek

Het rekenvoorbeeld uit het beleidsboek: een privéslaapkamer van 20 m² en een woonkamer van 40 m² die vier onzelfstandige woonruimten delen, geven bij energielabel A 19,50 punten.

Bron: beleidsboek onzelfstandige woonruimten, 2.4.4: "Huurder heeft een
privé slaapkamer van 20 m² in een pand met energielabel A. Naast de privé
slaapkamer heeft huurder toegang tot een gemeenschappelijke woonkamer van
40 m².", "Huurder deelt de woonkamer met drie andere huurders van
onzelfstandige woonruimten op het adres. Het aantal m2 gemeenschappelijk
vertrek dat aan de huurder is toe te rekenen is dus 40 m²/4 = 10 m².", "Het
puntenaantal voor de energieprestatie wordt dan als volgt berekend:" en
"(20 + 10) x 0,65 = 19,50 punten."

Bron: wettekst, Bijlage I onder B, onderdeel 4.1, tabel met de kolommen
energieprestatie, energie-index, bouwjaar en punten per m²: "A 0,8 < EI ≤
1,2 2002 en later 0,65 punt".

De privéslaapkamer heeft in de input
`gedeeld_met_aantal_onzelfstandige_woonruimten` 1 en is daarmee niet
gedeeld.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.1.4: "Indien
deze property leeg is of kleiner is dan 2, tellen we de ruimte mee als
zijnde niet gedeeld."

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
