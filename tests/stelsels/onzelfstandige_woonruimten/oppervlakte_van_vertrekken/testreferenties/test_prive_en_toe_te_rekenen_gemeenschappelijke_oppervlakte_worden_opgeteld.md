# test_prive_en_toe_te_rekenen_gemeenschappelijke_oppervlakte_worden_opgeteld

De oppervlakte van privévertrekken en de toe te rekenen oppervlakte van gemeenschappelijke vertrekken worden opgeteld.

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.2.1.1
- wettekst, Bijlage I onder B, toelichting rubriek 1

De oppervlakte van alle vertrekken samen wordt na saldering afgerond op hele
vierkante meters.

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.2.1.1
- wettekst, Bijlage I onder A, toelichting rubriek 1 (via Bijlage I onder B, toelichting, inleiding)

## Rapport

```text
OPPERVLAKTE VAN VERTREKKEN
  Privé
    - Slaapkamer                                                     10.40 m²
  Gedeeld met 4 onzelfstandige woonruimten
    - Keuken                                                         40.40 m²
                                                                                ------
  Totaal                                                                         21.00 pt
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
      "oppervlakte": 10.4
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
      "oppervlakte": 40.4,
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
      "code": "OVZ",
      "naam": "Oppervlakte van vertrekken"
    }
  },
  "punten": 21.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "oppervlakte_van_vertrekken__prive",
        "naam": "Privé"
      }
    },
    {
      "aantal": 10.4,
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
        "id": "oppervlakte_van_vertrekken__gedeeld_met_4_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 4 onzelfstandige woonruimten"
      }
    },
    {
      "aantal": 40.4,
      "criterium": {
        "id": "oppervlakte_van_vertrekken__gedeeld_met_4_onzelfstandige_woonruimten__keuken",
        "naam": "Keuken",
        "bovenliggendeCriterium": {
          "id": "oppervlakte_van_vertrekken__gedeeld_met_4_onzelfstandige_woonruimten"
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
