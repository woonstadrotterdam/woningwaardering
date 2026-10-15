# test_rijksmonument_met_pluspunten_krijgt_geen_correctie

Een rijksmonument met een positief aantal punten voor de energieprestatie houdt die punten.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.6.1;
wettekst, Bijlage I onder B, onderdeel 4.2.

## Rapport

```text
ENERGIEPRESTATIE
  Energieprestatievergoeding                                          3.67 m²     1.83 pt
  Afronding op kwartpunten                                                       -0.08 pt
                                                                                ------
  Totaal                                                                          1.75 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "bouwjaar": 1921,
  "energieprestaties": [
    {
      "soort": {
        "code": "EI",
        "naam": "Energie-index"
      },
      "status": {
        "code": "DEF",
        "naam": "Definitief"
      },
      "begindatum": "2017-02-23",
      "einddatum": "2027-02-23",
      "label": {
        "code": "C",
        "naam": "C"
      },
      "waarde": "1.48"
    }
  ],
  "monumenten": [
    {
      "code": "RIJ",
      "naam": "Rijksmonument"
    }
  ],
  "prijscomponenten": [
    {
      "detailSoort": {
        "code": "EPV",
        "naam": "Energieprestatievergoeding"
      }
    }
  ],
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
      "oppervlakte": 10.0,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 5
    },
    {
      "id": "woonkamer",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "WOO",
        "naam": "Woonkamer"
      },
      "naam": "Woonkamer",
      "oppervlakte": 10.0,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 6
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
      "code": "ENE",
      "naam": "Energieprestatie"
    }
  },
  "punten": 1.75,
  "woningwaarderingen": [
    {
      "aantal": 3.67,
      "criterium": {
        "id": "energieprestatie__energieprestatievergoeding",
        "naam": "Energieprestatievergoeding",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": 1.83
    },
    {
      "criterium": {
        "id": "energieprestatie__afronding_op_kwartpunten",
        "naam": "Afronding op kwartpunten"
      },
      "punten": -0.08
    }
  ]
}
```
