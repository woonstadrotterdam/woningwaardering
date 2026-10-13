# test_gemeenschappelijke_carport_of_parkeerplaats_wordt_niet_als_buitenruimte_gewaardeerd

Een gemeenschappelijke carport of parkeerplaats wordt niet als buitenruimte gewaardeerd.

De carport wordt met 3 onzelfstandige woonruimten op hetzelfde adres
gedeeld, de parkeerplaats met 2 adressen.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 8: "Gedeelde
buitenruimte die als parkeerplek bedoeld is, wordt gewaardeerd volgens
rubriek 10."

Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
overeenkomstige toepassing is."

Bron: implementatietoelichting onzelfstandige woonruimten, 2.8.3: "Een
`carport` of `parkeerplaats` is een VERA-buitenruimte: privé wordt die hier
gewaardeerd, gemeenschappelijk in rubriek 10".

Bron: implementatietoelichting onzelfstandige woonruimten, 2.10.2: "Voor
een onzelfstandige woonruimte telt daarnaast
`Eenhedenruimte.gedeeld_met_aantal_onzelfstandige_woonruimten` groter dan 1
als gemeenschappelijk: de plek wordt dan binnen het eigen adres gedeeld."

## Rapport

Geen waarderingen voor Buitenruimten.

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "carport",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "CAR",
        "naam": "Carport"
      },
      "naam": "Carport",
      "oppervlakte": 12.0,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 3
    },
    {
      "id": "parkeerplaats",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "PAR",
        "naam": "Parkeerplaats"
      },
      "naam": "Parkeerplaats",
      "oppervlakte": 12.0,
      "gedeeldMetAantalAdressen": 2
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
      "code": "BUI",
      "naam": "Buitenruimten"
    }
  },
  "punten": 0.0,
  "woningwaarderingen": []
}
```
