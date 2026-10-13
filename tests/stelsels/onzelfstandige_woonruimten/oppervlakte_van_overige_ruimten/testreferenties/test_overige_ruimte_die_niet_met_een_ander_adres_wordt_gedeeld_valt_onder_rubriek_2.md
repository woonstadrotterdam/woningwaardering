# test_overige_ruimte_die_niet_met_een_ander_adres_wordt_gedeeld_valt_onder_rubriek_2

Een overige ruimte die niet met een ander adres wordt gedeeld, wordt in rubriek 2 gewaardeerd.

De bijkeuken heeft `gedeeld_met_aantal_adressen` 1. Pas vanaf twee adressen
hoort een ruimte in rubriek 9.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 9:
"Gemeenschappelijke vertrekken en overige ruimten zijn tot het woongebouw
behorende binnenruimten waar de bewoners van tenminste twee adressen in het
woongebouw krachtens de huurovereenkomst exclusieve toegang en
gebruiksrecht toe hebben."

Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
overeenkomstige toepassing is."

Bron: beleidsboek onzelfstandige woonruimten, 2.2: "Gemeenschappelijke
ruimten die worden gedeeld met twee of meer adressen worden gewaardeerd
onder rubriek 9."

## Rapport

```text
OPPERVLAKTE VAN OVERIGE RUIMTEN
  Privé
    - Bijkeuken                                                       8.00 m²
                                                                                ------
  Totaal                                                                          6.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "bijkeuken",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "BIJ",
        "naam": "Bijkeuken"
      },
      "naam": "Bijkeuken",
      "oppervlakte": 8.0,
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
      "code": "OOZ",
      "naam": "Oppervlakte van overige ruimten"
    }
  },
  "punten": 6.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__prive",
        "naam": "Privé"
      }
    },
    {
      "aantal": 8.0,
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__prive__bijkeuken",
        "naam": "Bijkeuken",
        "bovenliggendeCriterium": {
          "id": "oppervlakte_van_overige_ruimten__prive"
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
