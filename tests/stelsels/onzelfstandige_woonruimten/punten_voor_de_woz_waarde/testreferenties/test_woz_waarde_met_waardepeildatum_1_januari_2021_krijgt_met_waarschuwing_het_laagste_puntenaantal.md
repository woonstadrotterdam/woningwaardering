# test_woz_waarde_met_waardepeildatum_1_januari_2021_krijgt_met_waarschuwing_het_laagste_puntenaantal

Een eenheid met alleen een WOZ-waarde met waardepeildatum 1 januari 2021 krijgt met een waarschuwing het laagste puntenaantal van 10 punten.

Bron: beleidsboek onzelfstandige woonruimten, 2.11.1: "Wanneer er geen
enkele WOZ-waarde of taxatiewaarde bekend is voor het adres van de woning,
dan wordt het laagste puntenaantal voor de WOZ-waarde toegepast (10
punten)."

De package rekent bij de peildatum van de waardering, hier 1 juli 2026,
alleen met een WOZ-waarde met waardepeildatum 1 januari 2025 of 1 januari
2024. Een WOZ-waarde met een oudere waardepeildatum behandelt zij als geen
WOZ-waarde. De implementatietoelichting noemt die keuze niet; de test legt
het huidige gedrag vast.

Bron: wettekst, Bijlage I onder B, toelichting rubriek 11: "In deze
regeling zijn twee verschillende kolommen weergegeven: één voor de
gemiddelden waar nog geen nieuwe WOZ-beschikking voor is afgegeven en één
voor de gemiddelden waar wel een nieuwe WOZ-beschikking is afgegeven."

Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
genereert de package een `UserWarning`."

## Rapport

```text
PUNTEN VOOR DE WOZ-WAARDE
  Geen WOZ-waarde bekend                                                         10.00 pt
                                                                                ------
  Totaal                                                                         10.00 pt
```

## Waarschuwingen

- UserWarning: Eenheid eenheid: geen WOZ-waarde gevonden met waardepeildatum 01-01-2025 of 01-01-2024

## Input

```json
{
  "id": "eenheid",
  "adres": {
    "woonplaats": {
      "code": "3086",
      "naam": "ROTTERDAM"
    }
  },
  "adresseerbaarObjectBasisregistratie": {
    "bagGebruikersOppervlakte": 58
  },
  "wozEenheden": [
    {
      "vastgesteldeWaarde": 124000.0,
      "waardepeildatum": "2021-01-01"
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
      "code": "WOZ",
      "naam": "Punten voor de WOZ-waarde"
    }
  },
  "punten": 10.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "punten_voor_de_woz_waarde__geen_woz_waarde_bekend",
        "naam": "Geen WOZ-waarde bekend"
      },
      "punten": 10.0
    }
  ]
}
```
