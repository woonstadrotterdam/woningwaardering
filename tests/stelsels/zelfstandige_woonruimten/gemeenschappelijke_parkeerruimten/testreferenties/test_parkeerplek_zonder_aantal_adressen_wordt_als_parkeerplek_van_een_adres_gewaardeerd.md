# test_parkeerplek_zonder_aantal_adressen_wordt_als_parkeerplek_van_een_adres_gewaardeerd

Een parkeerplek zonder aantal adressen wordt gewaardeerd als een parkeerplek van één adres.

De package waarschuwt dat `gedeeld_met_aantal_adressen` ontbreekt.

Bron: implementatietoelichting zelfstandige woonruimten, 2.10.4: "Dit
attribuut dient ook op elk type parkeerplek meegegeven te worden. Ontbreekt
het, dan volgt een `UserWarning` en gaan we uit van niet gedeeld met andere
adressen."

Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
genereert de package een `UserWarning`."

De twee parkeerplekken van Type III worden ook voor één adres in deze
rubriek gewaardeerd: hun punten worden opgeteld en door 1 gedeeld.

Bron: implementatietoelichting zelfstandige woonruimten, 2.10.2:
"waarderen we altijd in deze rubriek, ook wanneer de plek aan één adres is
toegewezen."

Bron: wettekst, Bijlage I onder A, toelichting rubriek 10: "Bij meerdere
parkeerplekken worden de punten bij elkaar opgeteld." en "Indien sprake is
van een privé parkeerplek voor één adres, wordt gedeeld door 1."

Bron: wettekst, Bijlage I onder A, rubriek 10: "Type III Parkeerplek buiten
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
      "code": "ZEL",
      "naam": "Zelfstandige woonruimten"
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
