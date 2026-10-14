# test_kast_telt_mee_in_de_oppervlakte_voor_de_energieprestatie

De oppervlakte van een kast die met een vertrek is verbonden, telt mee in de m² voor de energieprestatie.

Bron: wettekst, Bijlage I onder B, onderdeel 4.1: "Punten per m² die
volgens rubriek 1 zijn toe te rekenen aan de huurder".

Bron: wettekst, Bijlage I onder A, toelichting rubriek 1: "Meting van de
oppervlakte van vertrekken vindt plaats van muur tot muur, op een hoogte van
1,50 meter boven de vloer, inclusief de oppervlakte van alle tot de woning
behorende losse en vaste kasten."

Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
overeenkomstige toepassing is."

Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.4: "De
kastoppervlakte telt ook mee bij de drempeltoets in `classificeer_ruimte`
(4,00 m² voor vertrek, 2,00 m² voor overige ruimte) en bij totalen voor
onder meer energieprestatie, gemeenschappelijke ruimten en
zoldercorrecties."

De eenheid heeft geen energieprestaties. De package waarschuwt daarvoor en
waardeert op het bouwjaar.

Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
genereert de package een `UserWarning`."

Bouwjaar 1970 geeft -0,15 punt per m².

Bron: wettekst, Bijlage I onder B, onderdeel 4.1, tabel met de kolommen
energieprestatie, energie-index, bouwjaar en punten per m²: "Indien geen
energielabel of EI beschikbaar is, wordt gewaardeerd met het bouwjaar" en
"G EI > 2,7 1976 of ouder – 0,15 punt".

## Rapport

```text
ENERGIEPRESTATIE
  Bouwjaar 1970                                                      22.00 m²    -3.30 pt
  Afronding op kwartpunten                                                        0.05 pt
                                                                                ------
  Totaal                                                                         -3.25 pt
```

## Waarschuwingen

- UserWarning: Eenheid (eenheid): 'energieprestaties' is None

## Input

```json
{
  "id": "eenheid",
  "bouwjaar": 1970,
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
      "verbondenRuimten": [
        {
          "id": "kast",
          "soort": {
            "code": "OVR",
            "naam": "Overige ruimten"
          },
          "detailSoort": {
            "code": "KAS",
            "naam": "Kast"
          },
          "naam": "Kast",
          "oppervlakte": 2.0
        }
      ]
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
  "punten": -3.25,
  "woningwaarderingen": [
    {
      "aantal": 22.0,
      "criterium": {
        "id": "energieprestatie__bouwjaar",
        "naam": "Bouwjaar 1970",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": -3.3
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
