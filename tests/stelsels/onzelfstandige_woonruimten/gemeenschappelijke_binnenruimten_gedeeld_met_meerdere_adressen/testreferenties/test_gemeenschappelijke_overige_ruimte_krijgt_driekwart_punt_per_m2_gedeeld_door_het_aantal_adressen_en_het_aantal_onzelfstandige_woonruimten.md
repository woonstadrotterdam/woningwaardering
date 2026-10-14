# test_gemeenschappelijke_overige_ruimte_krijgt_driekwart_punt_per_m2_gedeeld_door_het_aantal_adressen_en_het_aantal_onzelfstandige_woonruimten

Een gemeenschappelijke overige ruimte krijgt 0,75 punt per m², gedeeld door het aantal adressen en daarna door het aantal onzelfstandige woonruimten op het adres.

Bron: wettekst, Bijlage I onder B, rubriek 9: "Gemeenschappelijke overige
ruimte 0,75 punt per m² gedeeld door het aantal adressen dat toegang en
gebruiksrecht heeft, en daarna gedeeld door het aantal onzelfstandige
woonruimten op dat adres".

De package deelt de punten en niet de oppervlakte. De berging telt daardoor
mee, ook al is haar oppervlakte per adres kleiner dan de 2 m² die een
overige ruimte minimaal groot is.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.9.1: "Anders
dan rubriek 1 en 2 deelt rubriek 9 niet de oppervlakte, maar de punten."

Bron: wettekst, Bijlage I onder A, toelichting rubriek 9: "Bepaal of het
een vertrek of een overige ruimte is en bereken de oppervlaktepunten:" en
"Deel dit aantal punten door het aantal adressen dat toegang heeft tot de
gemeenschappelijke binnenruimten."

Bron: wettekst, Bijlage I onder A, toelichting rubriek 2: "De ruimte dient
een oppervlakte te hebben van minimaal 2 m²."

Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
overeenkomstige toepassing is."

In het totaal zit ook het punt voor de verwarming van de berging, op
dezelfde manier gedeeld; het wordt afgerond op een kwart punt.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 9: "Bepaal de punten
voor verkoeling en verwarming conform rubriek 3;"

Bron: wettekst, Bijlage I onder A, toelichting rubriek 3: "Per verwarmde
overige ruimte en verkeersruimte wordt, ongeacht de verwarmingswijze, een
waardering van één punt toegepast".

Bron: wettekst, Bijlage I onder B, toelichting rubriek 9: "De punten voor
een gemeenschappelijke binnenruimte worden na verdeling over de meerdere
adressen nog gedeeld door het aantal onzelfstandige woonruimten op dat
adres."

Bron: wettekst, Bijlage I onder A, toelichting, inleiding: "De waardering in
punten per rubriek wordt na saldering afgerond op 0,25 punt waarbij een
achtste (1/8) punt naar boven wordt afgerond."

## Rapport

```text
GEMEENSCHAPPELIJKE BINNENRUIMTEN GEDEELD MET MEERDERE ADRESSEN
  Gedeeld met 2 onzelfstandige woonruimten
    - Gedeeld met 10 adressen
      - Oppervlakte van overige ruimten                                           0.71 pt
        - Berging                                                    19.00 m²
      - Verkoeling en verwarming
        - Verwarmde overige en verkeersruimten
          - Berging                                                               0.05 pt
  Afronding op kwartpunten                                                       -0.01 pt
                                                                                ------
  Totaal                                                                          0.75 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "berging",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "BER",
        "naam": "Berging"
      },
      "naam": "Berging",
      "oppervlakte": 19.0,
      "gedeeldMetAantalAdressen": 10,
      "verwarmd": true,
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
      "code": "GBA",
      "naam": "Gemeenschappelijke binnenruimten gedeeld met meerdere adressen"
    }
  },
  "punten": 0.75,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 2 onzelfstandige woonruimten"
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_10_adressen",
        "naam": "Gedeeld met 10 adressen",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_10_adressen__oppervlakte_van_overige_ruimten",
        "naam": "Oppervlakte van overige ruimten",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_10_adressen"
        }
      },
      "punten": 0.71
    },
    {
      "aantal": 19.0,
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_10_adressen__oppervlakte_van_overige_ruimten__berging",
        "naam": "Berging",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_10_adressen__oppervlakte_van_overige_ruimten"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_10_adressen__verkoeling_en_verwarming",
        "naam": "Verkoeling en verwarming",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_10_adressen"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_10_adressen__verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten",
        "naam": "Verwarmde overige en verkeersruimten",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_10_adressen__verkoeling_en_verwarming"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_10_adressen__verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten__berging",
        "naam": "Berging",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_10_adressen__verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten"
        }
      },
      "punten": 0.05
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__afronding_op_kwartpunten",
        "naam": "Afronding op kwartpunten"
      },
      "punten": -0.01
    }
  ]
}
```
