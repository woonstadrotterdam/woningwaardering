# test_ruimte_met_onbekende_detailsoort_telt_niet_mee_als_vertrek

Een ruimte met een detailsoort die de package niet kent, wordt niet als vertrek geteld.

De ruimte van 10 m² heeft een detailsoort met de code BRG, die niet in de
VERA-referentiedata staat (een berging heeft de code BER). De package
classificeert zo'n ruimte niet en geeft daar geen waarschuwing voor. De
woonruimte heeft daardoor geen vertrekken en krijgt 4 punten aftrek. De
test legt dat huidige gedrag vast; de implementatietoelichting spreekt er
niet over.

Bron: wettekst, Bijlage I onder B, onderdeel 13: "Wanneer de totale
oppervlakte van vertrekken onder rubriek 1 minder is dan 8 m²", "– 4
punten".

Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
genereert de package een `UserWarning`."

## Rapport

```text
AFTREKPUNTEN
  Oppervlakte van vertrekken is minder dan 8 m²                       0.00 m²    -4.00 pt
                                                                                ------
  Totaal                                                                         -4.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "berging",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "BRG",
        "naam": "Berging"
      },
      "naam": "Berging",
      "oppervlakte": 10.0
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
      "code": "AFT",
      "naam": "Aftrekpunten"
    }
  },
  "punten": -4.0,
  "woningwaarderingen": [
    {
      "aantal": 0.0,
      "criterium": {
        "id": "aftrekpunten__oppervlakte_van_vertrekken_minder_dan_8m2",
        "naam": "Oppervlakte van vertrekken is minder dan 8 m²",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": -4.0
    }
  ]
}
```
