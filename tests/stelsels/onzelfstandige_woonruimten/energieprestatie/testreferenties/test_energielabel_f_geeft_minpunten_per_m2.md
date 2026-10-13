# test_energielabel_f_geeft_minpunten_per_m2

Een energielabel F geeft 0,10 minpunt per m² van de vertrekken.

Bron: beleidsboek onzelfstandige woonruimten, 2.4.4: "De labelklasse
(A++++ t/m G) bepaalt het aantal punten voor de energieprestatie."

Bron: wettekst, Bijlage I onder B, onderdeel 4.1, tabel met de kolommen
energieprestatie, energie-index, bouwjaar en punten per m²: "F 2,4 < EI ≤
2,7 1977 t/m 1978 – 0,10 punt".

De m² zijn die van de vertrekken die aan de huurder zijn toe te rekenen:
elk gemeenschappelijk vertrek gedeeld door het aantal onzelfstandige
woonruimten.

Bron: wettekst, Bijlage I onder B, onderdeel 4.1: "Punten per m² die
volgens rubriek 1 zijn toe te rekenen aan de huurder".

Bron: wettekst, Bijlage I onder B, onderdeel 1: "Oppervlakte
gemeenschappelijk(e) vertrek(ken) op hetzelfde adres", "1 punt per m², te
delen door het aantal onzelfstandige woonruimten dat toegang en
gebruiksrecht heeft".

## Rapport

```text
ENERGIEPRESTATIE
  F                                                                   9.00 m²    -0.90 pt
  Afronding op kwartpunten                                                       -0.10 pt
                                                                                ------
  Totaal                                                                         -1.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "bouwjaar": 1993,
  "energieprestaties": [
    {
      "soort": {
        "code": "NTA",
        "naam": "Energielabel conform NTA8800"
      },
      "status": {
        "code": "DEF",
        "naam": "Definitief"
      },
      "begindatum": "2021-03-27",
      "einddatum": "2031-03-27",
      "label": {
        "code": "F",
        "naam": "F"
      },
      "waarde": "160.92"
    }
  ],
  "monumenten": [],
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
      "oppervlakte": 20.0,
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
      "oppervlakte": 30.0,
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
  "punten": -1.0,
  "woningwaarderingen": [
    {
      "aantal": 9.0,
      "criterium": {
        "id": "energieprestatie__label",
        "naam": "F",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": -0.9
    },
    {
      "criterium": {
        "id": "energieprestatie__afronding_op_kwartpunten",
        "naam": "Afronding op kwartpunten"
      },
      "punten": -0.1
    }
  ]
}
```
