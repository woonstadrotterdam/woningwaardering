# test_eenheid_zonder_adres_krijgt_met_waarschuwing_geen_waardering

Een eenheid zonder adres krijgt met een waarschuwing geen waardering voor de WOZ-waarde.

De package bepaalt het COROP-gebied met de woonplaatscode, of zoekt de
woonplaats op met postcode en huisnummer. Zonder adres heeft zij geen van
beide.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.11.2: "Het
COROP-gebied wordt bepaald op basis van de woonplaatscode van de woonplaats
waarin de eenheid zich bevindt." en "Indien dit attribuut niet
gespecificeerd is, wordt op basis van postcode, huisnummer, huisletter en
huisnummertoevoeging bepaald in welke woonplaats een eenheid zich bevindt."

De implementatietoelichting noemt niet dat de package bij een ontbrekend
adres waarschuwt en geen waardering geeft; de test legt het huidige gedrag
vast.

Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
genereert de package een `UserWarning`."

## Rapport

Geen waarderingen voor Punten voor de WOZ-waarde.

## Waarschuwingen

- UserWarning: Eenheid eenheid: adres met woonplaatscode of postcode en huisnummer ontbreekt, COROP-gebied kan niet bepaald worden voor gemiddelde WOZ waarde

## Input

```json
{
  "id": "eenheid",
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
