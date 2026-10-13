# test_keuken_aangeleverd_als_overige_ruimte_is_een_vertrek

Een keuken die als overige ruimte is aangeleverd, wordt als vertrek gewaardeerd.

De package waarschuwt dat de aangeleverde ruimtesoort afwijkt van de
ruimtesoort waarmee de keuken is gewaardeerd.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 1: "In afwijking van
bovenstaande eisen is een ruimte die uitsluitend als keuken dient en een
badkamer of doucheruimte altijd een vertrek."

Bron: implementatietoelichting zelfstandige woonruimten, 2.2.1.2:
"Uitzonderingen: keuken, badkamer en doucheruimte zijn volgens het
beleidsboek altijd een vertrek, en zo waarderen wij die ook, los van het
meegegeven `Ruimtesoort`."

## Rapport

```text
OPPERVLAKTE VAN VERTREKKEN
  Keuken                                                              1.00 m²
                                                                    ------      ------
  Totaal                                                              1.00 m²     1.00 pt
```

## Waarschuwingen

- UserWarning: Ruimte 'Keuken' (keuken) is aangeleverd als Overige ruimten maar wordt gewaardeerd als Vertrek.

## Input

```json
{
  "ruimten": [
    {
      "id": "keuken",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "KEU",
        "naam": "Keuken"
      },
      "naam": "Keuken",
      "oppervlakte": 1.0
    }
  ]
}
```

## Output

```json
{
  "criteriumGroep": {
    "stelsel": {
      "code": "ZEL",
      "naam": "Zelfstandige woonruimten"
    },
    "stelselgroep": {
      "code": "OVZ",
      "naam": "Oppervlakte van vertrekken"
    }
  },
  "punten": 1.0,
  "woningwaarderingen": [
    {
      "aantal": 1.0,
      "criterium": {
        "id": "oppervlakte_van_vertrekken__keuken",
        "naam": "Keuken",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    }
  ]
}
```
