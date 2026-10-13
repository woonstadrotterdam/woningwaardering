# test_twee_laadpalen_bij_een_garage_krijgen_samen_4_punten

Twee laadpalen bij een privégarage krijgen elk 2 punten: samen 4 punten.

Bron: wettekst, Bijlage I onder B, rubriek 12: "Laadpaal t.b.v. elektrisch
opladen" en "2 punten gedeeld door het aantal adressen dat toegang en
gebruiksrecht heeft."

De laadpalen zijn bouwkundige elementen van de garage. De garage wordt niet
met andere adressen en niet met andere onzelfstandige woonruimten gedeeld;
de punten worden daarom niet gedeeld. Een garage van één adres krijgt in
rubriek 10 geen punten; de laadpalen worden daarom in deze rubriek
gewaardeerd.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 10: "Een
parkeerruimte waartoe bewoners van één adres krachtens de huurovereenkomst
exclusieve toegang tot en gebruiksrecht op hebben, wordt gewaardeerd volgens
rubriek 2 (binnen, bijvoorbeeld een garagebox behorende tot de woning) of
rubriek 8 (buiten, bijvoorbeeld een oprit exclusief behorende tot de
woning)."

Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
overeenkomstige toepassing is."

Bron: implementatietoelichting onzelfstandige woonruimten, 2.12.3: "Krijgt
die ruimte in rubriek 10 punten, dan wordt de laadpaal daar gewaardeerd; in
alle andere gevallen hier, met dezelfde deler (aantal adressen × aantal
onzelfstandige woonruimten)."

## Rapport

```text
BIJZONDERE VOORZIENINGEN
  Privé
    - Laadpalen                                                       2.00 st     4.00 pt
                                                                                ------
  Totaal                                                                          4.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "id": "2 laadpalen",
  "ruimten": [
    {
      "id": "garage",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "GAR",
        "naam": "Garage"
      },
      "naam": "Garage",
      "oppervlakte": 19.1488,
      "bouwkundigeElementen": [
        {
          "id": "element_1",
          "naam": "Laadpaal",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "LAA",
            "naam": "Laadpaal"
          }
        },
        {
          "id": "element_2",
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
      ],
      "verwarmd": true,
      "verkoeld": false
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
  "punten": 4.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "bijzondere_voorzieningen__prive",
        "naam": "Privé"
      }
    },
    {
      "aantal": 2.0,
      "criterium": {
        "id": "bijzondere_voorzieningen__prive__laadpalen",
        "naam": "Laadpalen",
        "bovenliggendeCriterium": {
          "id": "bijzondere_voorzieningen__prive"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 4.0
    }
  ]
}
```
