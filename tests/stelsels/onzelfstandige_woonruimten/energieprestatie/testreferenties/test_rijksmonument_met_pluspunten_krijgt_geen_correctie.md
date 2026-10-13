# test_rijksmonument_met_pluspunten_krijgt_geen_correctie

Een rijksmonument met een positief aantal punten voor de energieprestatie houdt die punten.

Bron: wettekst, Bijlage I onder B, onderdeel 4.2: "Indien de woonruimte
bestaat uit of deel uitmaakt van een rijksmonument, een provinciaal monument
of een gemeentelijke monument als bedoeld in artikel 8a worden voor deze
rubriek geen minpunten toegekend. Voor energielabel E, F en G en daaraan
gelijkgestelde Energie-indexen en bouwjaren, geldt in afwijking van de
bovenstaande tabellen in dat geval een toekenning van nul punten."

De punten komen hier uit de energieprestatievergoeding: 0,50 punt per m².

Bron: beleidsboek onzelfstandige woonruimten, 2.4.6.3: "Bij een EPV wordt
de energieprestatie daarom gewaardeerd met een 0,50 punt per m2."

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
