# test_rekenvoorbeeld_met_vijf_parkeerplekken_uit_de_wettekst

Het rekenvoorbeeld uit de wettekst: vijf Type III-parkeerplekken die tien adressen delen, geven een van de vier onzelfstandige woonruimten op een adres 0,50 punt.

Bron: wettekst, Bijlage I onder B, toelichting rubriek 10: "in een
woongebouw bevinden zich tien adressen. Op één van deze adressen zijn vier
onzelfstandige woonruimten.", "Bij het woongebouw horen vijf type-III
parkeerplaatsen. De vijf parkeerplaatsen leveren 5 x 4 = 20 punten op. De
parkeerplaatsen worden gedeeld door tien adressen, dus 20/10 = 2 punten per
adres. Op het adres van A zijn vier onzelfstandige woonruimten, dus voor A
resulteert dit in 2/4 = 0,50 punt in de rubriek parkeerruimte."

De vijf parkeerplekken zijn één ruimte met `aantal` 5.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.10.2: "Daartoe
is het attribuut `Eenhedenruimte.aantal` als uitbreiding op het VERA-model
toegevoegd. Hierdoor is het mogelijk om aan te geven tot hoeveel van de
parkeerruimten de eenheid toegang heeft zonder dat elk parkeervak van een
parkeergarage of parkeerterrein meegegeven dient te worden."

Bron: implementatietoelichting onzelfstandige woonruimten, 2.10.3: "Type
III: `Ruimtedetailsoort.parkeerplek_buiten_behorend_bij_complex` (`PBC`)".

## Rapport

```text
GEMEENSCHAPPELIJKE PARKEERRUIMTEN
  Gedeeld met 4 onzelfstandige woonruimten
    - Gedeeld met 10 adressen
      - Parkeerplek buiten behorend bij complex (Type III)            5.00 st     0.50 pt
                                                                                ------
  Totaal                                                                          0.50 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "parkeerplek_buiten_behorend_bij_complex",
      "soort": {
        "code": "GEM",
        "naam": "Gemeenschappelijke ruimten en voorzieningen"
      },
      "detailSoort": {
        "code": "PBC",
        "naam": "Parkeerplek buiten behorend bij complex"
      },
      "naam": "Parkeerplek buiten behorend bij complex",
      "oppervlakte": 12.0,
      "gedeeldMetAantalAdressen": 10,
      "aantal": 5,
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
      "code": "GPA",
      "naam": "Gemeenschappelijke parkeerruimten"
    }
  },
  "punten": 0.5,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_4_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 4 onzelfstandige woonruimten"
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_10_adressen",
        "naam": "Gedeeld met 10 adressen",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_4_onzelfstandige_woonruimten"
        }
      }
    },
    {
      "aantal": 5.0,
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_10_adressen__parkeerplek_buiten_behorend_bij_complex_type_iii",
        "naam": "Parkeerplek buiten behorend bij complex (Type III)",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_10_adressen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.5
    }
  ]
}
```
