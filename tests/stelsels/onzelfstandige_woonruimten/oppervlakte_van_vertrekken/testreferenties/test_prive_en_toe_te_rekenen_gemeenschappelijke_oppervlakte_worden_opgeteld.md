# test_prive_en_toe_te_rekenen_gemeenschappelijke_oppervlakte_worden_opgeteld

De oppervlakte van privévertrekken en de toe te rekenen oppervlakte van gemeenschappelijke vertrekken worden opgeteld.

Het scenario is het rekenvoorbeeld uit de toelichting bij de wettekst, met
de keuken als gemeenschappelijk vertrek van drie onzelfstandige
woonruimten. Het onderscheidt niet of er één keer of per soort vertrek
wordt afgerond: beide geven 19 punten.

Bron: wettekst, Bijlage I onder B, toelichting rubriek 1: "Het aantal m² dat
volgens rubriek 1 aan de huurder is toe te rekenen is 10 m² + (40 m²/4) =
20 m²."

Bron: wettekst, Bijlage I onder A, toelichting rubriek 1: "De oppervlakte
per vertrek wordt afgerond op twee decimalen. De afronding van de
oppervlakte van alle vertrekken samen vindt plaats op hele vierkante meters
na saldering van de oppervlakte van alle vertrekken; bij 0,5 m² of meer
wordt afgerond naar boven, bij minder dan 0,5 m² naar beneden."

Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
overeenkomstige toepassing is."

## Rapport

```text
OPPERVLAKTE VAN VERTREKKEN
  Privé
    - Slaapkamer                                                     15.49 m²
  Gedeeld met 3 onzelfstandige woonruimten
    - Keuken                                                         11.24 m²
                                                                                ------
  Totaal                                                                         19.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "slaapkamer",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer",
      "oppervlakte": 15.4912
    },
    {
      "id": "keuken",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "KEU",
        "naam": "Keuken"
      },
      "naam": "Keuken",
      "oppervlakte": 11.2395,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 3
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
      "code": "OVZ",
      "naam": "Oppervlakte van vertrekken"
    }
  },
  "punten": 19.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "oppervlakte_van_vertrekken__prive",
        "naam": "Privé"
      }
    },
    {
      "aantal": 15.49,
      "criterium": {
        "id": "oppervlakte_van_vertrekken__prive__slaapkamer",
        "naam": "Slaapkamer",
        "bovenliggendeCriterium": {
          "id": "oppervlakte_van_vertrekken__prive"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "criterium": {
        "id": "oppervlakte_van_vertrekken__gedeeld_met_3_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 3 onzelfstandige woonruimten"
      }
    },
    {
      "aantal": 11.24,
      "criterium": {
        "id": "oppervlakte_van_vertrekken__gedeeld_met_3_onzelfstandige_woonruimten__keuken",
        "naam": "Keuken",
        "bovenliggendeCriterium": {
          "id": "oppervlakte_van_vertrekken__gedeeld_met_3_onzelfstandige_woonruimten"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    }
  ]
}
```
