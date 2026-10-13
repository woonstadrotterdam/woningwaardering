# test_parkeerplek_zonder_aantal_adressen_wordt_als_prive_parkeerplek_gewaardeerd

Een parkeerplek zonder aantal adressen wordt gewaardeerd als een privé-parkeerplek van één adres.

De package waarschuwt dat `gedeeld_met_aantal_adressen` ontbreekt en gaat
uit van één adres. Ook het aantal onzelfstandige woonruimten is niet
aangeleverd; de package leest dat zonder waarschuwing als niet gedeeld. De
implementatietoelichting voor onzelfstandige woonruimten vraagt beide
attributen, maar noemt de waarschuwing en de aanname van één adres niet.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.10.2:
"Daarnaast zijn ook `Eenhedenruimte.gedeeld_met_aantal_adressen` en
`Eenhedenruimte.gedeeld_met_aantal_onzelfstandige_woonruimten` als
uitbreiding toegevoegd. Deze attributen dienen ook op elk type parkeerplek
meegegeven te worden wanneer het een onzelfstandige woonruimte betreft."

Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
genereert de package een `UserWarning`."

De twee parkeerplekken van Type III worden ook als privé-parkeerplek in
deze rubriek gewaardeerd: hun punten worden opgeteld en door 1 gedeeld. De
wettekst waardeert in deze rubriek alleen parkeerplekken in een
gemeenschappelijke parkeerruimte; de package volgt hier de
implementatietoelichting.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.10.2:
"waarderen we altijd in deze rubriek, ook wanneer ze privé zijn of alleen
tussen onzelfstandige woonruimten op hetzelfde adres worden gedeeld."

Bron: wettekst, Bijlage I onder A, toelichting rubriek 10: "In deze rubriek
worden alleen parkeerplekken gewaardeerd die zich in een gemeenschappelijke
parkeerruimte bevinden.", "Bij meerdere parkeerplekken worden de punten bij
elkaar opgeteld." en "Indien sprake is van een privé parkeerplek voor één
adres, wordt gedeeld door 1."

Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
overeenkomstige toepassing is."

Bron: wettekst, Bijlage I onder B, rubriek 10: "Type III Parkeerplek buiten
behorende tot het complex zonder dak 4 punten".

## Rapport

```text
GEMEENSCHAPPELIJKE PARKEERRUIMTEN
  Privé
    - Parkeerplek buiten behorend bij complex (Type III)              2.00 st     8.00 pt
                                                                                ------
  Totaal                                                                          8.00 pt
```

## Waarschuwingen

- UserWarning: Ruimte 'Parkeerplek buiten behorend bij complex' (parkeerplek_buiten_behorend_bij_complex) heeft geen 'gedeeld_met_aantal_adressen'. De waardering gaat uit van 1 (niet gedeeld). Zet 'gedeeld_met_aantal_adressen' >= 2 wanneer de ruimte gedeeld is.

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
      "aantal": 2
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
  "punten": 8.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__prive",
        "naam": "Privé"
      }
    },
    {
      "aantal": 2.0,
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__prive__parkeerplek_buiten_behorend_bij_complex_type_iii",
        "naam": "Parkeerplek buiten behorend bij complex (Type III)",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_parkeerruimten__prive"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 8.0
    }
  ]
}
```
