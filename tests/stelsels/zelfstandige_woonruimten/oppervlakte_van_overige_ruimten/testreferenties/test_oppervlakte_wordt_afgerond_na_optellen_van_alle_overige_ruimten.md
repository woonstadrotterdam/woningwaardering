# test_oppervlakte_wordt_afgerond_na_optellen_van_alle_overige_ruimten

De oppervlakten van alle overige ruimten worden eerst opgeteld en dan afgerond op hele m².

Bron:
- implementatietoelichting zelfstandige woonruimten, 2.2.2.1
- wettekst, Bijlage I onder A, toelichting rubriek 2

## Rapport

```text
OPPERVLAKTE VAN OVERIGE RUIMTEN
  Bijkeuken                                                           2.40 m²
  Berging                                                             2.40 m²
                                                                    ------      ------
  Totaal                                                              4.80 m²     3.75 pt
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
      "oppervlakte": 2.4
    },
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
      "oppervlakte": 2.4
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
      "code": "OOZ",
      "naam": "Oppervlakte van overige ruimten"
    }
  },
  "punten": 3.75,
  "woningwaarderingen": [
    {
      "aantal": 2.4,
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__bijkeuken",
        "naam": "Bijkeuken",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "aantal": 2.4,
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__berging",
        "naam": "Berging",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    }
  ]
}
```
