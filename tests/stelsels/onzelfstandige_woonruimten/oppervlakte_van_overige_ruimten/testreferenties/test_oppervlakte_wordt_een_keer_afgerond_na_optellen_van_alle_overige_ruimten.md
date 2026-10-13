# test_oppervlakte_wordt_een_keer_afgerond_na_optellen_van_alle_overige_ruimten

De oppervlakte wordt één keer afgerond op hele vierkante meters, nadat de toe te rekenen oppervlakte van alle overige ruimten is opgeteld.

Het beleidsboek rondt privé en gemeenschappelijke overige ruimten
afzonderlijk af; dat geeft hier 20 m² in plaats van 21 m². De package volgt
de keuze uit de implementatietoelichting. De zolder heeft een vlizotrap:
daardoor staat het subtotaal in de uitkomst en komt de aftrek voor die
zolder daarop in mindering.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 2: "De afronding van
de oppervlakte van alle overige ruimte samen vindt plaats op hele
vierkante meters na saldering van de oppervlakte van de afzonderlijke
overige ruimten; bij 0,5 m² of meer wordt naar boven afgerond, bij minder
dan 0,5 m² naar beneden."

Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
overeenkomstige toepassing is."

Bron: beleidsboek onzelfstandige woonruimten, 2.2.2.1: "De oppervlakten
voor privé- en gemeenschappelijke overige ruimten worden afzonderlijk
berekend."

Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.2.1: "per
ruimte delen waar nodig, salderen, daarna éénmaal afronden op hele m²,
daarna × 0,75." en "dat past bij delen vóór afronden (20,50 → 21 m²), niet
bij apart afronden per categorie (20 m² → 15,00)".

## Rapport

```text
OPPERVLAKTE VAN OVERIGE RUIMTEN
  Subtotaal                                                                      15.75 pt
    - Privé
      - Berging                                                      10.40 m²
    - Gedeeld met 4 onzelfstandige woonruimten
      - Zolder                                                       40.40 m²
  Correctie: zolder zonder vaste trap                                            -1.25 pt
                                                                                ------
  Totaal                                                                         14.50 pt
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
      "oppervlakte": 10.4
    },
    {
      "id": "zolder",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "ZOL",
        "naam": "Zolder"
      },
      "naam": "Zolder",
      "oppervlakte": 40.4,
      "bouwkundigeElementen": [
        {
          "id": "vlizotrap",
          "naam": "Vlizotrap",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "VTR",
            "naam": "Vlizotrap"
          }
        }
      ],
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 4
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
      "code": "OOZ",
      "naam": "Oppervlakte van overige ruimten"
    }
  },
  "punten": 14.5,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__subtotaal",
        "naam": "Subtotaal"
      },
      "punten": 15.75
    },
    {
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__subtotaal__prive",
        "naam": "Privé",
        "bovenliggendeCriterium": {
          "id": "oppervlakte_van_overige_ruimten__subtotaal"
        }
      }
    },
    {
      "aantal": 10.4,
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__subtotaal__prive__berging",
        "naam": "Berging",
        "bovenliggendeCriterium": {
          "id": "oppervlakte_van_overige_ruimten__subtotaal__prive"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__subtotaal__gedeeld_met_4_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 4 onzelfstandige woonruimten",
        "bovenliggendeCriterium": {
          "id": "oppervlakte_van_overige_ruimten__subtotaal"
        }
      }
    },
    {
      "aantal": 40.4,
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__subtotaal__gedeeld_met_4_onzelfstandige_woonruimten__zolder",
        "naam": "Zolder",
        "bovenliggendeCriterium": {
          "id": "oppervlakte_van_overige_ruimten__subtotaal__gedeeld_met_4_onzelfstandige_woonruimten"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__zolder__correctie_zolder_zonder_vaste_trap",
        "naam": "Correctie: zolder zonder vaste trap"
      },
      "punten": -1.25
    }
  ]
}
```
