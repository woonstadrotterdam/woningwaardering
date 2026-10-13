# test_woonplaatscode_zonder_corop_gebied_krijgt_met_waarschuwing_geen_waardering

Een eenheid met een woonplaatscode waarbij de package geen COROP-gebied kent, krijgt met een waarschuwing geen waardering voor de WOZ-waarde.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.11.2: "Het
COROP-gebied wordt bepaald op basis van de woonplaatscode van de woonplaats
waarin de eenheid zich bevindt."

De package zoekt het COROP-gebied bij de woonplaatscode op in een extract
van CBS-data. Woonplaatscode 0100 staat daar niet in.

Bron: docs/voor-ontwikkelaars/data, Woonplaatsen en COROP-gebieden: "daarom
hebben we een script gemaakt dat een extract van deze data als resource in
de package opslaat in `woningwaardering/data/corop/corop.generated.csv`".

De implementatietoelichting noemt niet dat de package bij een onbekende
woonplaatscode waarschuwt en geen waardering geeft; de test legt het
huidige gedrag vast.

Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
genereert de package een `UserWarning`."

## Rapport

Geen waarderingen voor Punten voor de WOZ-waarde.

## Waarschuwingen

- UserWarning: Eenheid eenheid: Geen COROP-gebied gevonden voor woonplaats Rotjeknor met woonplaatscode 0100. Kan punten voor de WOZ-waarde niet bepalen.

## Input

```json
{
  "id": "eenheid",
  "adres": {
    "woonplaats": {
      "code": "0100",
      "naam": "Rotjeknor"
    }
  },
  "adresseerbaarObjectBasisregistratie": {
    "bagGebruikersOppervlakte": 58
  },
  "wozEenheden": [
    {
      "vastgesteldeWaarde": 148000.0,
      "waardepeildatum": "2022-01-01"
    },
    {
      "vastgesteldeWaarde": 184000.0,
      "waardepeildatum": "2023-01-01"
    },
    {
      "vastgesteldeWaarde": 205000.0,
      "waardepeildatum": "2024-01-01"
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
  "woningwaarderingen": []
}
```
