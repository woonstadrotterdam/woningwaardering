# test_prive_carport_krijgt_geen_punten

Een privé-carport krijgt in deze rubriek geen punten.

De carport hoort bij één adres en het aantal onzelfstandige woonruimten is
niet aangeleverd. Ze is daarmee niet gemeenschappelijk, maar een
privé-buitenruimte die in rubriek 8 hoort.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.10.2: "Voor
een onzelfstandige woonruimte telt daarnaast
`Eenhedenruimte.gedeeld_met_aantal_onzelfstandige_woonruimten` groter dan 1
als gemeenschappelijk: de plek wordt dan binnen het eigen adres gedeeld."

Bron: implementatietoelichting onzelfstandige woonruimten, 2.8.3: "Een
`carport` of `parkeerplaats` is een VERA-buitenruimte: privé wordt die hier
gewaardeerd, gemeenschappelijk in rubriek 10".

Bron: wettekst, Bijlage I onder A, toelichting rubriek 10: "Een
parkeerruimte waartoe bewoners van één adres krachtens de huurovereenkomst
exclusieve toegang tot en gebruiksrecht op hebben, wordt gewaardeerd volgens
rubriek 2 (binnen, bijvoorbeeld een garagebox behorende tot de woning) of
rubriek 8 (buiten, bijvoorbeeld een oprit exclusief behorende tot de
woning)."

Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
overeenkomstige toepassing is."

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
      "gedeeldMetAantalAdressen": 1
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
      "code": "GPA",
      "naam": "Gemeenschappelijke parkeerruimten"
    }
  },
  "punten": 0.0,
  "woningwaarderingen": []
}
```
