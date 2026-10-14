# test_aanrecht_in_een_overig_vertrek_is_een_open_keuken

Een aanrecht in een verwarmd overig vertrek is een open keuken.

Het vertrek wordt met 2 onzelfstandige woonruimten gedeeld en krijgt
daarom de helft van de 4 punten.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.3.2: "Elke
ruimte (uitgezonderd `keuken`, `bijkeuken`, `badkamer`,
`badkamer_met_toilet` en `doucheruimte`) die als vertrek wordt gewaardeerd
en waarin een aanrecht vanaf 1 meter staat, heeft dus een open keuken, ook
bijvoorbeeld een `serre`, `overig vertrek` of een `berging` die als vertrek
wordt aangeleverd."

Bron: wettekst, Bijlage I onder A, toelichting rubriek 3: "een open keuken
als afzonderlijk verwarmd vertrek beschouwd en krijgt dus twee punten indien
er verwarming aanwezig is".

Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
overeenkomstige toepassing is."

Bron: wettekst, Bijlage I onder B, rubriek 3: "Verwarming per
gemeenschappelijk vertrek op hetzelfde adres 2 punten, te delen door het
aantal onzelfstandige woonruimten dat toegang en gebruiksrecht heeft".

## Rapport

```text
VERKOELING EN VERWARMING
  Gedeeld met 2 onzelfstandige woonruimten
    - Verwarmde vertrekken
      - Overig vertrek met open keuken                                            2.00 pt
                                                                                ------
  Totaal                                                                          2.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "overig_vertrek",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "OVT",
        "naam": "Overig vertrek"
      },
      "naam": "Overig vertrek",
      "oppervlakte": 10.0,
      "bouwkundigeElementen": [
        {
          "id": "aanrecht",
          "naam": "Aanrecht",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "AAN",
            "naam": "Aanrecht"
          },
          "lengte": 1500.0
        }
      ],
      "verwarmd": true,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
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
      "code": "VKV",
      "naam": "Verkoeling en verwarming"
    }
  },
  "punten": 2.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 2 onzelfstandige woonruimten"
      }
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verwarmde_vertrekken",
        "naam": "Verwarmde vertrekken",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten"
        }
      }
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verwarmde_vertrekken__overig_vertrek",
        "naam": "Overig vertrek met open keuken",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verwarmde_vertrekken"
        }
      },
      "punten": 2.0
    }
  ]
}
```
