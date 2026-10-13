# test_rijksmonument_krijgt_geen_minpunten

Een rijksmonument krijgt geen minpunten voor de energieprestatie.

Bron: wettekst, Bijlage I onder B, onderdeel 4.2: "Indien de woonruimte
bestaat uit of deel uitmaakt van een rijksmonument, een provinciaal monument
of een gemeentelijke monument als bedoeld in artikel 8a worden voor deze
rubriek geen minpunten toegekend. Voor energielabel E, F en G en daaraan
gelijkgestelde Energie-indexen en bouwjaren, geldt in afwijking van de
bovenstaande tabellen in dat geval een toekenning van nul punten."

De eenheid heeft geen energieprestaties. De package waarschuwt daarvoor en
waardeert op het bouwjaar.

Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
genereert de package een `UserWarning`."

Bouwjaar 1921 geeft zonder de uitzondering -0,15 punt per m².

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
  Bouwjaar 1921                                                       3.67 m²    -0.55 pt
  Correctie monument                                                              0.55 pt
                                                                                ------
  Totaal                                                                          0.00 pt
```

## Waarschuwingen

- UserWarning: Eenheid (eenheid): 'energieprestaties' is None

## Input

```json
{
  "id": "eenheid",
  "bouwjaar": 1921,
  "energieprestaties": [],
  "monumenten": [
    {
      "code": "RIJ",
      "naam": "Rijksmonument"
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
  "punten": 0.0,
  "woningwaarderingen": [
    {
      "aantal": 3.67,
      "criterium": {
        "id": "energieprestatie__bouwjaar",
        "naam": "Bouwjaar 1921",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": -0.55
    },
    {
      "criterium": {
        "id": "energieprestatie__correctie_monument",
        "naam": "Correctie monument"
      },
      "punten": 0.55
    }
  ]
}
```
