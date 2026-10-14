# test_oppervlakte_wordt_afgerond_na_optellen_van_alle_overige_ruimten

De oppervlakten van alle overige ruimten worden eerst opgeteld en dan afgerond op hele m².

Het scenario is het rekenvoorbeeld uit de toelichting bij de wettekst.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 2: "De oppervlakte
per overige ruimte wordt afgerond op 2 decimalen. De afronding van de
oppervlakte van alle overige ruimte samen vindt plaats op hele vierkante
meters na saldering van de oppervlakte van de afzonderlijke overige
ruimten" en "Dit vertaalt zich dan naar 25 x 0,75 punt (per m²) = 18,75
punten."

## Rapport

```text
OPPERVLAKTE VAN OVERIGE RUIMTEN
  Garage                                                             19.34 m²
  Bijkeuken                                                           6.06 m²
                                                                    ------      ------
  Totaal                                                             25.40 m²    18.75 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "garage",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "GAR",
        "naam": "Garage"
      },
      "naam": "Garage",
      "oppervlakte": 19.3392
    },
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
      "oppervlakte": 6.0557
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
  "punten": 18.75,
  "woningwaarderingen": [
    {
      "aantal": 19.34,
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__garage",
        "naam": "Garage",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "aantal": 6.06,
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__bijkeuken",
        "naam": "Bijkeuken",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    }
  ]
}
```
