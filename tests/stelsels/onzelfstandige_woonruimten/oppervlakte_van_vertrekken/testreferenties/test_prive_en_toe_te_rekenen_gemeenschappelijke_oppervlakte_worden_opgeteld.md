# test_prive_en_toe_te_rekenen_gemeenschappelijke_oppervlakte_worden_opgeteld

De oppervlakte van privévertrekken en de toe te rekenen oppervlakte van gemeenschappelijke vertrekken worden opgeteld.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.1.1;
wettekst, Bijlage I onder B, toelichting rubriek 1.

De oppervlakte per vertrek wordt afgerond op twee decimalen, en die van
alle vertrekken samen na saldering op hele vierkante meters.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.1.1;
wettekst, Bijlage I onder A, toelichting rubriek 1 (via Bijlage I onder
B, toelichting, inleiding).

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
