# test_carport_gedeeld_met_onzelfstandige_woonruimten_op_hetzelfde_adres_wordt_als_type_ii_gewaardeerd

Een carport die alleen door onzelfstandige woonruimten op hetzelfde adres wordt gedeeld, wordt in deze rubriek als Type II gewaardeerd.

De carport hoort bij één adres en wordt daar met 2 onzelfstandige
woonruimten gedeeld. De package leest een parkeerplek die binnen het eigen
adres wordt gedeeld als gemeenschappelijk; de test legt die keuze uit de
implementatietoelichting vast.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.10.2: "Voor
een onzelfstandige woonruimte telt daarnaast
`Eenhedenruimte.gedeeld_met_aantal_onzelfstandige_woonruimten` groter dan 1
als gemeenschappelijk: de plek wordt dan binnen het eigen adres gedeeld."

De wettekst noemt een parkeerruimte pas gemeenschappelijk bij ten minste
twee adressen en verwijst een parkeerruimte van één adres naar rubriek 2 of
8; de keuze van de package wijkt daarvan af.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 10: "Een
gemeenschappelijke parkeerruimte is een ruimte die toegankelijk is voor
bewoners van tenminste twee adressen die daar exclusief gebruiksrecht op
hebben, waarin zich tenminste één parkeerplek bevindt" en "Een parkeerruimte
waartoe bewoners van één adres krachtens de huurovereenkomst exclusieve
toegang tot en gebruiksrecht op hebben, wordt gewaardeerd volgens rubriek 2
(binnen, bijvoorbeeld een garagebox behorende tot de woning) of rubriek 8
(buiten, bijvoorbeeld een oprit exclusief behorende tot de woning)."

Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
overeenkomstige toepassing is."

De 6 punten van Type II worden door de 2 onzelfstandige woonruimten
gedeeld.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.10.3: "Type II:
`Ruimtedetailsoort.parkeerplek_buiten_met_dak_behorend_bij_complex` (`PBD`)
en, wanneer die gemeenschappelijk is, `Ruimtedetailsoort.carport` (`CAR`)."

Bron: wettekst, Bijlage I onder B, rubriek 10: "Type II Parkeerplek buiten
behorende tot het complex met dak 6 punten".

Bron: wettekst, Bijlage I onder B, toelichting rubriek 10: "De punten voor
een parkeerplaats worden na eventuele verdeling over de meerdere adressen
nog gedeeld door het aantal onzelfstandige woonruimten op dat adres."

## Rapport

```text
GEMEENSCHAPPELIJKE PARKEERRUIMTEN
  Gedeeld met 2 onzelfstandige woonruimten
    - Carport (Type II)                                               1.00 st     3.00 pt
                                                                                ------
  Totaal                                                                          3.00 pt
```

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
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
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
  "punten": 3.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_2_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 2 onzelfstandige woonruimten"
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_2_onzelfstandige_woonruimten__carport_type_ii",
        "naam": "Carport (Type II)",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_2_onzelfstandige_woonruimten"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 3.0
    }
  ]
}
```
