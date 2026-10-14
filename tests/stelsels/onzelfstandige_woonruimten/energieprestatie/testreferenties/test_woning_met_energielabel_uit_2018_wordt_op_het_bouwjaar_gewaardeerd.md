# test_woning_met_energielabel_uit_2018_wordt_op_het_bouwjaar_gewaardeerd

Een energielabel uit 2018 telt niet mee: het bouwjaar bepaalt de punten per m².

Bron: beleidsboek onzelfstandige woonruimten, 2.4.3: "Een energielabel dat
is afgegeven in de periode van 1 januari 2015 tot 1 januari 2021 krijgt geen
punten in het woningwaarderingsstelsel."

Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.3: "Een
energieprestatie van een ander soort dan energie-index in de periode
2015-2021, of een energie-index zonder bruikbare `waarde`, telt niet mee
(2.4.3, punt 4); de waardering valt dan terug op het bouwjaar (2.4.5)."

Bouwjaar 1970 geeft -0,15 punt per m².

Bron: wettekst, Bijlage I onder B, onderdeel 4.1, tabel met de kolommen
energieprestatie, energie-index, bouwjaar en punten per m²: "Indien geen
energielabel of EI beschikbaar is, wordt gewaardeerd met het bouwjaar" en
"G EI > 2,7 1976 of ouder – 0,15 punt".

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
  Bouwjaar 1970                                                       3.67 m²    -0.55 pt
  Afronding op kwartpunten                                                        0.05 pt
                                                                                ------
  Totaal                                                                         -0.50 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "bouwjaar": 1970,
  "energieprestaties": [
    {
      "soort": {
        "code": "VEL",
        "naam": "Voorlopig energielabel"
      },
      "status": {
        "code": "DEF",
        "naam": "Definitief"
      },
      "begindatum": "2018-06-01",
      "einddatum": "2028-06-01",
      "label": {
        "code": "A",
        "naam": "A"
      }
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
  "punten": -0.5,
  "woningwaarderingen": [
    {
      "aantal": 3.67,
      "criterium": {
        "id": "energieprestatie__bouwjaar",
        "naam": "Bouwjaar 1970",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": -0.55
    },
    {
      "criterium": {
        "id": "energieprestatie__afronding_op_kwartpunten",
        "naam": "Afronding op kwartpunten"
      },
      "punten": 0.05
    }
  ]
}
```
