# test_rijksmonument_in_rijksbeschermd_stadsgezicht_krijgt_geen_opslag_voor_het_stadsgezicht

Een rijksmonument in een rijksbeschermd stadsgezicht krijgt de opslag van 5% voor het stadsgezicht niet.

Bron: wettekst, artikel 8a, vijfde lid: "De maximale huurprijsgrens wordt
met 5% vermeerderd indien:" en "c. de woonruimte niet bestaat of deel
uitmaakt van een rijksmonument als bedoeld in artikel 1.1 van de Erfgoedwet
of van een door het college van burgemeester en wethouders aangewezen
gemeentelijk monument of een door gedeputeerde staten aangewezen
provinciaal monument."

Bron: beleidsboek onzelfstandige woonruimten, 2.14.1: "Zo kunnen de
monumentenopslag (zowel de Rijksmonumenten als provinciale en gemeentelijke
monumenten) en de opslag voor een beschermd stads- of dorpsgezicht niet
tegelijkertijd voor dezelfde woonruimte worden toegekend".

De woning is uit 1964 en voldoet daarmee aan de voorwaarde voor het
bouwjaar; alleen de status van rijksmonument sluit de opslag voor het
stadsgezicht uit.

Bron: wettekst, artikel 8a, vijfde lid: "b. de woonruimte behoort tot een
woning die is gebouwd voor 1965; en".

De eenheid heeft geen datum van afsluiten van de huurovereenkomst. De
package waarschuwt daarvoor en rekent met de peildatum van de waardering,
hier 1 juli 2026; het rijksmonument krijgt daarmee 35% opslag. De
implementatietoelichting noemt de keuze voor de peildatum niet; de test
legt het huidige gedrag vast.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.14.4: "De datum
van afsluiten van de huurovereenkomst dient gespecificeerd te worden voor
Rijksmonumenten."

Bron: wettekst, artikel 8a, eerste lid: "De maximale huurprijsgrens wordt
met 35% vermeerderd indien de woonruimte bestaat uit of deel uitmaakt van
een rijksmonument als bedoeld in artikel 1.1 van de Erfgoedwet en de
huurovereenkomst betreffende die woonruimte is afgesloten na het tijdstip
van inwerkingtreding van de Wet betaalbare huur."

## Rapport

```text
PRIJSOPSLAG MONUMENTEN
  Rijksmonument                                                                                35%
                                                                                ------
  Totaal                                                                          0.00 pt      35%
```

## Waarschuwingen

- UserWarning: Eenheid (None): 'datum_afsluiten_huurovereenkomst' is niet gespecificeerd voor dit rijksmonument.

## Input

```json
{
  "bouwjaar": 1964,
  "monumenten": [
    {
      "code": "RIJ",
      "naam": "Rijksmonument"
    },
    {
      "code": "SGR",
      "naam": "Rijksbeschermd stadsgezicht"
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
      "code": "PMO",
      "naam": "Prijsopslag monumenten"
    }
  },
  "punten": 0.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "prijsopslag_monumenten__rijksmonument",
        "naam": "Rijksmonument"
      },
      "opslagpercentage": 0.35
    }
  ],
  "opslagpercentage": 0.35
}
```
