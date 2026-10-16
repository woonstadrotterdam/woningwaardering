# test_woz_waarde_die_niet_door_de_gebruiksoppervlakte_te_delen_is_krijgt_met_waarschuwing_geen_waardering

Een eenheid waarvan de WOZ-waarde niet door de gebruiksoppervlakte te delen is, krijgt met een waarschuwing geen waardering voor de WOZ-waarde.

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
