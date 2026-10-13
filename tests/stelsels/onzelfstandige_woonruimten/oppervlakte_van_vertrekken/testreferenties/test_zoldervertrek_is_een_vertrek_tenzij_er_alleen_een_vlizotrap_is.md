# test_zoldervertrek_is_een_vertrek_tenzij_er_alleen_een_vlizotrap_is

Een zoldervertrek is een vertrek, tenzij het alleen via een vlizotrap bereikbaar is.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 1: "Zolderruimten
slechts als vertrek gewaardeerd worden, indien deze bereikbaar zijn via een
vaste trap en indien de vloer begaanbaar en het dak beschoten is."

Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
overeenkomstige toepassing is."

Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.1.3: "De
detailsoort draagt eis 1 dus zelf; alleen het `Bouwkundigelement`
`vlizotrap` weerspreekt dat."

## Rapport

```text
OPPERVLAKTE VAN VERTREKKEN
  Privé
    - Zoldervertrek1                                                 10.00 m²
    - Zoldervertrek2                                                 10.00 m²
                                                                                ------
  Totaal                                                                         20.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "zoldervertrek1",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "ZVT",
        "naam": "Zoldervertrek"
      },
      "naam": "Zoldervertrek1",
      "oppervlakte": 10.0,
      "bouwkundigeElementen": [
        {
          "id": "trap",
          "naam": "Trap",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "TRA",
            "naam": "Trap"
          }
        }
      ]
    },
    {
      "id": "zoldervertrek2",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "ZVT",
        "naam": "Zoldervertrek"
      },
      "naam": "Zoldervertrek2",
      "oppervlakte": 10.0
    },
    {
      "id": "zoldervertrek3",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "ZVT",
        "naam": "Zoldervertrek"
      },
      "naam": "Zoldervertrek3",
      "oppervlakte": 10.0,
      "bouwkundigeElementen": [
        {
          "id": "vlizotrap",
          "naam": "Vlizotrap",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "VTR",
            "naam": "Vlizotrap"
          }
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
      "code": "OVZ",
      "naam": "Oppervlakte van vertrekken"
    }
  },
  "punten": 20.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "oppervlakte_van_vertrekken__prive",
        "naam": "Privé"
      }
    },
    {
      "aantal": 10.0,
      "criterium": {
        "id": "oppervlakte_van_vertrekken__prive__zoldervertrek1",
        "naam": "Zoldervertrek1",
        "bovenliggendeCriterium": {
          "id": "oppervlakte_van_vertrekken__prive"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "aantal": 10.0,
      "criterium": {
        "id": "oppervlakte_van_vertrekken__prive__zoldervertrek2",
        "naam": "Zoldervertrek2",
        "bovenliggendeCriterium": {
          "id": "oppervlakte_van_vertrekken__prive"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    }
  ]
}
```
