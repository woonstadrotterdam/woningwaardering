# test_gebruiksoppervlakte_van_0_m2_krijgt_met_waarschuwing_geen_waardering

Een eenheid met een gebruiksoppervlakte van 0 m² krijgt met een waarschuwing geen waardering voor de WOZ-waarde.

De punten volgen uit de WOZ-waarde per m² gebruiksoppervlakte. Door een
gebruiksoppervlakte van 0 m² is de WOZ-waarde niet te delen.

Bron: beleidsboek onzelfstandige woonruimten, 2.11.2: "Deel de WOZ-waarde
door het aantal m² gebruiksoppervlakte van de woning".

Bron: implementatietoelichting onzelfstandige woonruimten, 2.11.2: "De
gebruiksoppervlakte dient gespecificeerd te worden in het attribuut
`adresseerbaar_object_basisregistratie.bag_gebruikers_oppervlakte` op de
eenheid."

De implementatietoelichting noemt niet dat de package bij een
gebruiksoppervlakte van 0 m² waarschuwt en geen waardering geeft; de test
legt het huidige gedrag vast.

Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
genereert de package een `UserWarning`."

## Rapport

Geen waarderingen voor Punten voor de WOZ-waarde.

## Waarschuwingen

- UserWarning: Eenheid eenheid: geen bruikbare gebruiksoppervlakte van het verblijfsobject gevonden. Dit dient gespecificeerd te worden in het attribuut 'adresseerbaar_object_basisregistratie.bag_gebruikers_oppervlakte' op de eenheid. Kan punten voor de WOZ-waarde niet bepalen.

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
    "bagGebruikersOppervlakte": 0
  },
  "wozEenheden": [
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
