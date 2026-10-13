# test_laadpaal_bij_parkeerplek_op_hetzelfde_adres_krijgt_2_punten_gedeeld_door_het_aantal_onzelfstandige_woonruimten

Een laadpaal bij een parkeerplek die alleen door onzelfstandige woonruimten op hetzelfde adres wordt gedeeld, krijgt 2 punten extra, gedeeld door het aantal onzelfstandige woonruimten.

De carport hoort bij één adres en wordt daar met 2 onzelfstandige
woonruimten gedeeld.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 10: "Indien er sprake
is van een laadpaal voor exclusief gebruik door de bewoners, geldt twee
punten extra per parkeerplek met laadpaal."

Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
overeenkomstige toepassing is."

Bron: wettekst, Bijlage I onder B, toelichting rubriek 10: "De punten voor
een parkeerplaats worden na eventuele verdeling over de meerdere adressen
nog gedeeld door het aantal onzelfstandige woonruimten op dat adres."

Het beleidsboek noemt bij de laadpaal alleen de deling door het aantal
adressen. De package deelt de laadpaal door dezelfde deler als de
parkeerplek waar hij bij hoort.

Bron: beleidsboek onzelfstandige woonruimten, 2.10.5: "dan worden 2 extra
punten toegekend, gedeeld door het aantal adressen dat toegang en
gebruiksrecht heeft."

Bron: implementatietoelichting onzelfstandige woonruimten, 2.12.3: "de
laadpaal deelt de rubriek én de deler van de parkeerruimte waar hij bij
hoort. Krijgt die ruimte in rubriek 10 punten, dan wordt de laadpaal daar
gewaardeerd; in alle andere gevallen hier, met dezelfde deler (aantal
adressen × aantal onzelfstandige woonruimten)."

## Rapport

```text
GEMEENSCHAPPELIJKE PARKEERRUIMTEN
  Gedeeld met 2 onzelfstandige woonruimten
    - Carport (Type II)                                               1.00 st     3.00 pt
    - Laadpaal                                                        1.00 st     1.00 pt
                                                                                ------
  Totaal                                                                          4.00 pt
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
      ],
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
  "punten": 4.0,
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
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_2_onzelfstandige_woonruimten__carport_type_ii_laadpaal",
        "naam": "Laadpaal",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_2_onzelfstandige_woonruimten"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 1.0
    }
  ]
}
```
