# test_woonplaatsnaam_die_afwijkt_van_het_kadaster_krijgt_met_waarschuwing_geen_waardering

Een eenheid waarvan de opgegeven woonplaatsnaam afwijkt van de woonplaats die het Kadaster bij postcode en huisnummer geeft, krijgt met een waarschuwing geen waardering voor de WOZ-waarde.

De woonplaats van de eenheid heeft een naam en geen code. De package zoekt
de woonplaats daarom op bij het Kadaster, met postcode en huisnummer.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.11.2: "Indien
dit attribuut niet gespecificeerd is, wordt op basis van postcode,
huisnummer, huisletter en huisnummertoevoeging bepaald in welke woonplaats
een eenheid zich bevindt." en "Hierbij is het van belang dat deze waarden
overeenkomen met de BAG-registratie."

Het Kadaster geeft bij postcode 1013GS en huisnummer 22 de woonplaats
Amsterdam; de eenheid noemt Rotterdam. De package rekent dan met geen van
beide woonplaatsen: zij waarschuwt voor het verschil, en daarna dat zij
geen woonplaats heeft gevonden. De implementatietoelichting noemt die keuze
niet; de test legt het huidige gedrag vast.

Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
genereert de package een `UserWarning`."

## Rapport

Geen waarderingen voor Punten voor de WOZ-waarde.

## Waarschuwingen

- UserWarning: Woonplaats Amsterdam is gevonden voor adres 1013GS 22, terwijl woonplaats ROTTERDAM is opgegeven. Kan geen woonplaats bepalen voor de waardering.
- UserWarning: Eenheid eenheid: Geen woonplaats gevonden voor adres id=None id_extern=None id_gegevensbeheerder=None id_organisatie=None id_administratie=None code=None soort=None adres=None huisletter=None huisnummer='22' huisnummer_toevoeging=None postcode='1013GS' straatnaam=None buurt=None gemeente=None geometrie=None land=None wijk=None woonplaats=EenhedenWoonplaats(id=None, id_extern=None, id_gegevensbeheerder=None, id_organisatie=None, id_administratie=None, code=None, naam='ROTTERDAM'). Kan punten voor de WOZ-waarde niet bepalen.

## Input

```json
{
  "id": "eenheid",
  "adres": {
    "huisnummer": "22",
    "postcode": "1013GS",
    "woonplaats": {
      "naam": "ROTTERDAM"
    }
  },
  "adresseerbaarObjectBasisregistratie": {
    "bagGebruikersOppervlakte": 58
  },
  "wozEenheden": [
    {
      "vastgesteldeWaarde": 178000.0,
      "waardepeildatum": "2022-01-01"
    },
    {
      "vastgesteldeWaarde": 194000.0,
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
