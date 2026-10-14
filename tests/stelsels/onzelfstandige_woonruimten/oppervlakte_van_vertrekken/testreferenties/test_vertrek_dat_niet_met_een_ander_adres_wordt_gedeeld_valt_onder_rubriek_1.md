# test_vertrek_dat_niet_met_een_ander_adres_wordt_gedeeld_valt_onder_rubriek_1

Een vertrek dat niet met een ander adres wordt gedeeld, wordt in rubriek 1 gewaardeerd en niet in rubriek 9.

Het vertrek heeft `gedeeld_met_aantal_adressen` 1. Pas vanaf twee adressen
hoort een ruimte in rubriek 9.

Bron: beleidsboek onzelfstandige woonruimten, 2.2: "Gemeenschappelijke
ruimten die worden gedeeld met twee of meer adressen worden gewaardeerd
onder rubriek 9."

Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.4:
"Gemeenschappelijke vertrekken die met meerdere adressen worden gedeeld
(`gedeeldMetAantalAdressen` ≥ 2)" en "Rubriek 1 dekt alleen privévertrekken
en gemeenschappelijke vertrekken op hetzelfde adres; ruimten gedeeld met
meerdere adressen vallen onder rubriek 9".

## Rapport

```text
OPPERVLAKTE VAN VERTREKKEN
  Privé
    - Slaapkamer                                                      5.00 m²
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
      "oppervlakte": 5.0,
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
    }
  ]
}
```
