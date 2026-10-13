# test_van_twee_energieprestaties_telt_alleen_de_geldige

Van twee energieprestaties bepaalt alleen de geldige de punten per m² van de vertrekken.

Bron: beleidsboek onzelfstandige woonruimten, 2.4.2: "De woonruimte krijgt
punten voor de energieprestatie als de woning een geldend energielabel of
energie-index heeft."

Het eerste energielabel is op twee gronden niet geldig: het is op de
peildatum vervallen en het is afgegeven in 2019.

Bron: beleidsboek onzelfstandige woonruimten, 2.4.3: "Aan een vervallen
energielabel of energie-index wordt geen waardering toegekend.", "Een
energielabel dat is afgegeven in de periode van 1 januari 2015 tot 1 januari
2021 krijgt geen punten in het woningwaarderingsstelsel."

Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.3: "De
peildatum moet vallen tussen begindatum en einddatum."

Het geldige energielabel A geeft 0,65 punt per m².

Bron: wettekst, Bijlage I onder B, onderdeel 4.1, tabel met de kolommen
energieprestatie, energie-index, bouwjaar en punten per m²: "A 0,8 < EI ≤
1,2 2002 en later 0,65 punt".

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
  A                                                                   3.67 m²     2.38 pt
  Afronding op kwartpunten                                                        0.12 pt
                                                                                ------
  Totaal                                                                          2.50 pt
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
      "begindatum": "2019-03-27",
      "einddatum": "2021-03-27",
      "label": {
        "code": "F",
        "naam": "F"
      },
      "waarde": "160"
    },
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
        "code": "A",
        "naam": "A"
      },
      "waarde": "170"
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
  "punten": 2.5,
  "woningwaarderingen": [
    {
      "aantal": 3.67,
      "criterium": {
        "id": "energieprestatie__label",
        "naam": "A",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": 2.38
    },
    {
      "criterium": {
        "id": "energieprestatie__afronding_op_kwartpunten",
        "naam": "Afronding op kwartpunten"
      },
      "punten": 0.12
    }
  ]
}
```
