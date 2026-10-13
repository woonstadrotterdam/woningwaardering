# test_aanbelfunctie_met_video_en_audioverbinding_krijgt_0_25_punt

Een aanbelfunctie met video- en audioverbinding krijgt 0,25 punt.

Bron: wettekst, Bijlage I onder B, rubriek 12: "Aanbelfunctie met video- en
audioverbinding waarbij de voordeur automatisch kan worden geopend vanuit
de woning" en "0,25 punt".

De aanbelfunctie is een installatie van een ruimte, hier de woonkamer.

Bron: implementatietoelichting, datamodel-uitbreidingen, "Installaties":
"Op dit moment gebruiken wij `installaties` als attribuut op ruimte met als
type `Optional[list[Installatiesoort]]`."

Of de voordeur vanuit de woonruimte kan worden geopend, controleert de
package niet. De implementatietoelichting voor onzelfstandige woonruimten
neemt die voorwaarde ongewijzigd over en zegt niet dat ze niet wordt
gecontroleerd. De test legt het huidige gedrag vast.

Bron: beleidsboek onzelfstandige woonruimten, 2.12.2: "Daarbij dient er ook
sprake te zijn van de mogelijkheid tot het openen van de
(gemeenschappelijke) voordeur vanuit de woonruimte (op afstand) die toegang
geeft tot het complex waarvan de woning onderdeel uitmaakt."

## Rapport

```text
BIJZONDERE VOORZIENINGEN
  Aanbelfunctie met video- en audioverbinding                                     0.25 pt
                                                                                ------
  Totaal                                                                          0.25 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "id": "aanbelfunctie",
  "ruimten": [
    {
      "id": "woonkamer",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "WOO",
        "naam": "Woonkamer"
      },
      "naam": "Woonkamer",
      "oppervlakte": 19.1488,
      "verwarmd": true,
      "verkoeld": false,
      "installaties": [
        {
          "code": "ABF",
          "naam": "Aanbelfunctie met video- en audioverbinding"
        }
      ]
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
      "code": "BIJ",
      "naam": "Bijzondere voorzieningen"
    }
  },
  "punten": 0.25,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "bijzondere_voorzieningen__aanbelfunctie_met_video_en_audioverbinding",
        "naam": "Aanbelfunctie met video- en audioverbinding"
      },
      "punten": 0.25
    }
  ]
}
```
