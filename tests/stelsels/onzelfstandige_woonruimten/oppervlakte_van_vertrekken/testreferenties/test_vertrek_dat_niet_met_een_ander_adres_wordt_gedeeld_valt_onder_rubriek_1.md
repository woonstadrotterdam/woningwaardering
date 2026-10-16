# test_vertrek_dat_niet_met_een_ander_adres_wordt_gedeeld_valt_onder_rubriek_1

Een vertrek dat niet met een ander adres wordt gedeeld, wordt in rubriek 1 gewaardeerd en niet in rubriek 9.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.2;
wettekst, Bijlage I onder A, toelichting rubriek 9 (via Bijlage I onder
B, toelichting, inleiding).

## Rapport

```text
OPPERVLAKTE VAN VERTREKKEN
  Privé
    - Slaapkamer1                                                     5.00 m²
                                                                                ------
  Totaal                                                                          5.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "slaapkamer1",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer1",
      "oppervlakte": 5.0,
      "gedeeldMetAantalAdressen": 1
    },
    {
      "id": "slaapkamer2",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer2",
      "oppervlakte": 10.0,
      "gedeeldMetAantalAdressen": 2
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
  "punten": 5.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "oppervlakte_van_vertrekken__prive",
        "naam": "Privé"
      }
    },
    {
      "aantal": 5.0,
      "criterium": {
        "id": "oppervlakte_van_vertrekken__prive__slaapkamer1",
        "naam": "Slaapkamer1",
        "bovenliggendeCriterium": {
          "id": "oppervlakte_van_vertrekken__prive"
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
