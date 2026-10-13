# test_vertrek_gedeeld_met_meerdere_adressen_telt_niet_mee

Een vertrek dat met meerdere adressen wordt gedeeld, telt niet mee in de m² voor de energieprestatie.

Bron: wettekst, Bijlage I onder B, onderdeel 4.1: "Punten per m² die
volgens rubriek 1 zijn toe te rekenen aan de huurder".

Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.4:
"Gemeenschappelijke vertrekken die met meerdere adressen worden gedeeld
(`gedeeldMetAantalAdressen` ≥ 2) tellen niet mee voor de oppervlakte in
§2.4.4." en "Rubriek 1 dekt alleen privévertrekken en gemeenschappelijke
vertrekken op hetzelfde adres; ruimten gedeeld met meerdere adressen
vallen onder rubriek 9".

De privéslaapkamer heeft in de input
`gedeeld_met_aantal_onzelfstandige_woonruimten` 1 en is daarmee niet
gedeeld.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.1.4: "Indien
deze property leeg is of kleiner is dan 2, tellen we de ruimte mee als
zijnde niet gedeeld."

Alleen de privéslaapkamer van 20 m² telt mee. Label A geeft 0,65 punt per
m².

Bron: wettekst, Bijlage I onder B, onderdeel 4.1, tabel met de kolommen
energieprestatie, energie-index, bouwjaar en punten per m²: "A 0,8 < EI ≤
1,2 2002 en later 0,65 punt".

## Rapport

```text
ENERGIEPRESTATIE
  A                                                                  20.00 m²    13.00 pt
                                                                                ------
  Totaal                                                                         13.00 pt
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
      "gedeeldMetAantalAdressen": 2,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
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
  "punten": 13.0,
  "woningwaarderingen": [
    {
      "aantal": 20.0,
      "criterium": {
        "id": "energieprestatie__label",
        "naam": "A",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": 13.0
    }
  ]
}
```
