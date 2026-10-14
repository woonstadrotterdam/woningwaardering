# test_kast_telt_mee_in_de_oppervlakte_van_een_gemeenschappelijke_overige_ruimte[berging_van_8m2]

De oppervlakte van een kast telt mee in de oppervlakte van een gemeenschappelijke overige ruimte.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 9: "Met vertrekken en
overige ruimten wordt onder deze rubriek aangesloten bij definities en de
meetmethoden als gegeven onder rubriek 1 en 2."

Bron: wettekst, Bijlage I onder A, toelichting rubriek 2: "Meting van de
oppervlakte vindt plaats van muur tot muur, op een hoogte van 1,50 meter
boven de vloer, inclusief de oppervlakte van alle losse en vaste tot de
woning behorende kasten".

Bron: implementatietoelichting zelfstandige woonruimten, 2.2.4: "De
kastoppervlakte telt ook mee bij de drempeltoets in `classificeer_ruimte`
(4,00 m² voor vertrek, 2,00 m² voor overige ruimte) en bij totalen voor
onder meer energieprestatie, gemeenschappelijke ruimten en
zoldercorrecties."

Bron: wettekst, Bijlage I onder A, rubriek 9: "Gemeenschappelijke overige
ruimte 0,75 punt per m² gedeeld door het aantal adressen dat toegang en
gebruiksrecht heeft."

Het totaal van de rubriek wordt afgerond op een kwart punt.

Bron: wettekst, Bijlage I onder A, toelichting, inleiding: "De waardering in
punten per rubriek wordt na saldering afgerond op 0,25 punt waarbij een
achtste (1/8) punt naar boven wordt afgerond."

## Rapport

```text
GEMEENSCHAPPELIJKE VERTREKKEN, OVERIGE RUIMTEN EN VOORZIENINGEN
  Gedeeld met 2 adressen
    - Oppervlakte van overige ruimten                                             3.75 pt
      - Berging (+1 kast)                                            10.00 m²
                                                                                ------
  Totaal                                                                          3.75 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "berging",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "BER",
        "naam": "Berging"
      },
      "naam": "Berging",
      "oppervlakte": 8.0,
      "gedeeldMetAantalAdressen": 2,
      "verbondenRuimten": [
        {
          "id": "kast",
          "soort": {
            "code": "OVR",
            "naam": "Overige ruimten"
          },
          "detailSoort": {
            "code": "KAS",
            "naam": "Kast"
          },
          "naam": "Kast",
          "oppervlakte": 2.0
        }
      ]
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
      "code": "GVR",
      "naam": "Gemeenschappelijke vertrekken, overige ruimten en voorzieningen"
    }
  },
  "punten": 3.75,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen",
        "naam": "Gedeeld met 2 adressen"
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__oppervlakte_van_overige_ruimten",
        "naam": "Oppervlakte van overige ruimten",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen"
        }
      },
      "punten": 3.75
    },
    {
      "aantal": 10.0,
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__oppervlakte_van_overige_ruimten__berging",
        "naam": "Berging (+1 kast)",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__oppervlakte_van_overige_ruimten"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    }
  ]
}
```
