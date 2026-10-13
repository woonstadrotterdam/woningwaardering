# test_rijksmonument_zonder_datum_van_de_huurovereenkomst_krijgt_met_waarschuwing_35_procent_opslag

Een rijksmonument zonder datum van afsluiten van de huurovereenkomst krijgt met een waarschuwing 35% opslag op de maximale huurprijs.

De waardering van een rijksmonument hangt af van de datum waarop de
huurovereenkomst is afgesloten; de package vraagt die datum daarom op.

Bron: implementatietoelichting zelfstandige woonruimten, 2.13.4: "De datum
van afsluiten van de huurovereenkomst dient gespecificeerd te worden voor
rijksmonumenten."

Bron: implementatietoelichting, datamodel-uitbreidingen, "Datum afsluiten
huurovereenkomst": "Voor een correcte waardering van rijksmonumenten dient
de afsluitings datum van de huurovereenkomst opgegeven te worden."

Ontbreekt de datum, dan rekent de package met de peildatum van de
waardering, hier 1 juli 2026. De implementatietoelichting noemt die keuze
niet; de test legt het huidige gedrag vast.

Bron: wettekst, artikel 8a, eerste lid: "De maximale huurprijsgrens wordt
met 35% vermeerderd indien de woonruimte bestaat uit of deel uitmaakt van
een rijksmonument als bedoeld in artikel 1.1 van de Erfgoedwet en de
huurovereenkomst betreffende die woonruimte is afgesloten na het tijdstip
van inwerkingtreding van de Wet betaalbare huur."

## Rapport

```text
PRIJSOPSLAG MONUMENTEN EN NIEUWBOUW
  Rijksmonument                                                                                35%
                                                                                ------
  Totaal                                                                          0.00 pt      35%
```

## Waarschuwingen

- UserWarning: Eenheid (eenheid): 'datum_afsluiten_huurovereenkomst' is niet gespecificeerd voor dit rijksmonument.

## Input

```json
{
  "id": "eenheid",
  "monumenten": [
    {
      "code": "RIJ",
      "naam": "Rijksmonument"
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
      "code": "PMN",
      "naam": "Prijsopslag monumenten en nieuwbouw"
    }
  },
  "punten": 0.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "prijsopslag_monumenten_en_nieuwbouw__rijksmonument",
        "naam": "Rijksmonument"
      },
      "opslagpercentage": 0.35
    }
  ],
  "opslagpercentage": 0.35
}
```
