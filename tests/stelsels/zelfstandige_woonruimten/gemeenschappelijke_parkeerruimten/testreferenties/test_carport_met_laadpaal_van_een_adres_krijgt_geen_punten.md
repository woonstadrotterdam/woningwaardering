# test_carport_met_laadpaal_van_een_adres_krijgt_geen_punten

Een carport met laadpaal van één adres krijgt in deze rubriek geen punten.

De carport is een privé-buitenruimte en hoort in rubriek 8.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 10: "Een
parkeerruimte waartoe bewoners van één adres krachtens de huurovereenkomst
exclusieve toegang tot en gebruiksrecht op hebben, wordt gewaardeerd volgens
rubriek 2 (binnen, bijvoorbeeld een garagebox behorende tot de woning) of
rubriek 8 (buiten, bijvoorbeeld een oprit exclusief behorende tot de
woning)."

Bron: implementatietoelichting zelfstandige woonruimten, 2.8.3: "Een
`carport` of `parkeerplaats` is een VERA-buitenruimte: privé wordt die hier
gewaardeerd, gemeenschappelijk in rubriek 10".

De laadpaal volgt de carport en hoort dan in rubriek 12.

Bron: implementatietoelichting zelfstandige woonruimten, 2.12.3: "Krijgt die
ruimte in rubriek 10 punten, dan wordt de laadpaal daar gewaardeerd; in alle
andere gevallen hier, met dezelfde deler (aantal adressen)."

## Rapport

Geen waarderingen voor Gemeenschappelijke parkeerruimten.

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "carport",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "CAR",
        "naam": "Carport"
      },
      "naam": "Carport",
      "oppervlakte": 12.0,
      "gedeeldMetAantalAdressen": 1,
      "bouwkundigeElementen": [
        {
          "id": "laadpaal",
          "naam": "Laadpaal",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "LAA",
            "naam": "Laadpaal"
          }
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
      "code": "ZEL",
      "naam": "Zelfstandige woonruimten"
    },
    "stelselgroep": {
      "code": "GPA",
      "naam": "Gemeenschappelijke parkeerruimten"
    }
  },
  "punten": 0.0,
  "woningwaarderingen": []
}
```
