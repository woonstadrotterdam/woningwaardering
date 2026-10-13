# test_energie_index_wordt_op_de_index_gewaardeerd_niet_op_het_label

Bij een energie-index uit 2020 bepaalt de index de punten per m², niet het label dat erbij is meegegeven.

Bron: beleidsboek onzelfstandige woonruimten, 2.4.4: "Bij een energie-index
wordt het puntenaantal bepaald door het relevante cijfer."

Een energie-index van 1,48 geeft 0,35 punt per m²; het meegegeven label A
zou 0,65 punt per m² geven.

Bron: wettekst, Bijlage I onder B, onderdeel 4.1, tabel met de kolommen
energieprestatie, energie-index, bouwjaar en punten per m²: "C 1,4 < EI ≤
1,8 1992 t/m 1999 0,35 punt", "A 0,8 < EI ≤ 1,2 2002 en later 0,65 punt".

De m² zijn die van de vertrekken die aan de huurder zijn toe te rekenen:
elk gemeenschappelijk vertrek gedeeld door het aantal onzelfstandige
woonruimten, onafgerond opgeteld.

Bron: wettekst, Bijlage I onder B, onderdeel 4.1: "Punten per m² die
volgens rubriek 1 zijn toe te rekenen aan de huurder".

Bron: wettekst, Bijlage I onder B, onderdeel 1: "Oppervlakte
gemeenschappelijk(e) vertrek(ken) op hetzelfde adres", "1 punt per m², te
delen door het aantal onzelfstandige woonruimten dat toegang en
gebruiksrecht heeft".

Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.4: volgens
rubriek 1 toe te rekenen "is de onafgeronde toerekening (eerst delen, dan
salderen), niet het afgeronde puntenresultaat van rubriek 1."

## Rapport

```text
ENERGIEPRESTATIE
  A -> C (Energie-index)                                              3.67 m²     1.28 pt
  Afronding op kwartpunten                                                       -0.03 pt
                                                                                ------
  Totaal                                                                          1.25 pt
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
      "begindatum": "2020-08-01",
      "einddatum": "2030-08-01",
      "label": {
        "code": "A",
        "naam": "A"
      },
      "waarde": "1.48"
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
  "punten": 1.25,
  "woningwaarderingen": [
    {
      "aantal": 3.67,
      "criterium": {
        "id": "energieprestatie__label",
        "naam": "A -> C (Energie-index)",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": 1.28
    },
    {
      "criterium": {
        "id": "energieprestatie__afronding_op_kwartpunten",
        "naam": "Afronding op kwartpunten"
      },
      "punten": -0.03
    }
  ]
}
```
