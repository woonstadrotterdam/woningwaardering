{%
    include-markdown "../../README.md"
    start="<!--installatie-start-->"
    end="<!--installatie-end-->"
    heading-offset=1
%}

## Gebruik

De input voor de woningwaardering-package is een Eenheid object in het formaat van de VERA-standaard. Dit object is definieerbaar in JSON of m.b.v. Python classes.
Zie onderstaande voorbeelden voor de de input in JSON en Python.

> [!TIP]
> Zie de [implementatietoelichtingen](../implementatietoelichtingen/index.md) voor voorbeeld-inputs per stelselgroep.  


### JSON

```python
import warnings
from datetime import date

from woningwaardering import Woningwaardering
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
)
from woningwaardering.stelsels.utils import naar_tabel

warnings.simplefilter("default", UserWarning)

wws = Woningwaardering(
    peildatum=date(2026, 1, 1)  # bij niet meegeven wordt de huidige dag gebruikt.
)
with open(
    "tests/data/generiek/input/37101000032.json",
    "r+",
) as file:
    eenheid = EenhedenEenheid.model_validate_json(file.read())

    # Woningwaardering class kiest op basis van de input het zelfstandig of onzelfstandige stelsel.
    woningwaardering_resultaat = wws.waardeer(eenheid)
    print(
        woningwaardering_resultaat.model_dump_json(
            by_alias=True, indent=2, exclude_none=True
        )
    )
    tabel = naar_tabel(woningwaardering_resultaat)

    print(tabel)
```

<details>
<summary>Voorbeeld output in JSON</summary>

```json
{
  "groepen": [
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "OVZ",
          "naam": "Oppervlakte van vertrekken"
        }
      },
      "punten": 141.0,
      "woningwaarderingen": [
        {
          "aantal": 21.05,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_108014589",
            "naam": "Slaapkamer 1",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 41.0,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_108010632",
            "naam": "Woonkamer",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 20.37,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_108006229",
            "naam": "Keuken",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 7.5,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_108014563",
            "naam": "Badruimte",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 15.98,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_108017433",
            "naam": "Slaapkamer 2",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 19.15,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_108017431",
            "naam": "Slaapkamer 3",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 15.82,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_108014593",
            "naam": "Slaapkamer 4",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        }
      ]
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "OOZ",
          "naam": "Oppervlakte van overige ruimten"
        }
      },
      "punten": 5.25,
      "woningwaarderingen": [
        {
          "aantal": 6.65,
          "criterium": {
            "id": "oppervlakte_van_overige_ruimten__Space_108017427",
            "naam": "Berging",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        }
      ]
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "VKV",
          "naam": "Verkoeling en verwarming"
        }
      },
      "punten": 14.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__Space_108014589",
            "naam": "Slaapkamer 1",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__totaal__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__Space_108010632",
            "naam": "Woonkamer",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__totaal__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__Space_108006229",
            "naam": "Keuken",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__totaal__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__Space_108014563",
            "naam": "Badruimte",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__totaal__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__Space_108017433",
            "naam": "Slaapkamer 2",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__totaal__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__Space_108017431",
            "naam": "Slaapkamer 3",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__totaal__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__Space_108014593",
            "naam": "Slaapkamer 4",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__totaal__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__totaal__verwarmde_vertrekken",
            "naam": "Verwarmde vertrekken"
          },
          "punten": 14.0
        }
      ]
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "BUI",
          "naam": "Buitenruimten"
        }
      },
      "punten": 15.0,
      "woningwaarderingen": [
        {
          "aantal": 3.14,
          "criterium": {
            "id": "buitenruimten__Space_108014713",
            "naam": "Balkon 1",
            "bovenliggendeCriterium": {
              "id": "buitenruimten__totaal__prive"
            },
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 3.14,
          "criterium": {
            "id": "buitenruimten__Space_108010812",
            "naam": "Balkon 2",
            "bovenliggendeCriterium": {
              "id": "buitenruimten__totaal__prive"
            },
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 49.11,
          "criterium": {
            "id": "buitenruimten__Space_108006357",
            "naam": "Tuin",
            "bovenliggendeCriterium": {
              "id": "buitenruimten__totaal__prive"
            },
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 15.93,
          "criterium": {
            "id": "buitenruimten__Space_108006467",
            "naam": "Dakterras",
            "bovenliggendeCriterium": {
              "id": "buitenruimten__totaal__prive"
            },
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "criterium": {
            "id": "buitenruimten__aanwezig__prive",
            "naam": "Privé buitenruimten aanwezig"
          },
          "punten": 2.0
        },
        {
          "aantal": 71.0,
          "criterium": {
            "id": "buitenruimten__totaal__prive",
            "naam": "Totaal (privé)",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          },
          "punten": 24.85
        },
        {
          "criterium": {
            "id": "buitenruimten__maximering",
            "naam": "Maximaal 15 punten"
          },
          "punten": -11.85
        }
      ]
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "ENE",
          "naam": "Energieprestatie"
        }
      },
      "punten": 22.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "energieprestatie__label",
            "naam": "C (Energie-index)"
          },
          "punten": 22.0
        }
      ]
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "KEU",
          "naam": "Keuken"
        }
      },
      "punten": 7.0,
      "woningwaarderingen": [
        {
          "aantal": 2700.0,
          "criterium": {
            "id": "keuken__Space_108006229__lengte_aanrecht_Aanrecht_108006231",
            "naam": "Keuken: Lengte aanrecht",
            "meeteenheid": {
              "code": "MIL",
              "naam": "Millimeter"
            }
          },
          "punten": 7.0
        }
      ]
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "SAN",
          "naam": "Sanitair"
        }
      },
      "punten": 15.0,
      "woningwaarderingen": [
        {
          "aantal": 1.0,
          "criterium": {
            "id": "sanitair__Space_108014563__staand_toilet",
            "naam": "Badruimte - Staand Toilet"
          },
          "punten": 2.0
        },
        {
          "aantal": 2.0,
          "criterium": {
            "id": "sanitair__Space_108014563__wastafel",
            "naam": "Badruimte - Wastafel"
          },
          "punten": 2.0
        },
        {
          "aantal": 1.0,
          "criterium": {
            "id": "sanitair__Space_108014563__bad_en_douche",
            "naam": "Badruimte - Bad en douche"
          },
          "punten": 7.0
        },
        {
          "aantal": 1.0,
          "criterium": {
            "id": "sanitair__Space_108006223__staand_toilet",
            "naam": "Toiletruimte - Staand Toilet"
          },
          "punten": 3.0
        },
        {
          "aantal": 1.0,
          "criterium": {
            "id": "sanitair__Space_108006223__wastafel",
            "naam": "Toiletruimte - Wastafel"
          },
          "punten": 1.0
        }
      ]
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "GPA",
          "naam": "Gemeenschappelijke parkeerruimten"
        }
      },
      "punten": 0.0,
      "woningwaarderingen": []
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "GVR",
          "naam": "Gemeenschappelijke vertrekken, overige ruimten en voorzieningen"
        }
      },
      "punten": 0.0,
      "woningwaarderingen": []
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "WOZ",
          "naam": "Punten voor de WOZ-waarde"
        }
      },
      "punten": 64.75,
      "woningwaarderingen": [
        {
          "aantal": 694000.0,
          "criterium": {
            "id": "punten_voor_de_woz_waarde__woz_waarde",
            "naam": "WOZ-waarde op waardepeildatum 01-01-2024"
          }
        },
        {
          "aantal": 15329.0,
          "criterium": {
            "id": "punten_voor_de_woz_waarde__factor_I",
            "naam": "Factor I",
            "bovenliggendeCriterium": {
              "id": "punten_voor_de_woz_waarde__totaal__onderdeel_I"
            }
          }
        },
        {
          "criterium": {
            "id": "punten_voor_de_woz_waarde__totaal__onderdeel_I",
            "naam": "Onderdeel I"
          },
          "punten": 45.27
        },
        {
          "aantal": 148.0,
          "criterium": {
            "id": "punten_voor_de_woz_waarde__oppervlakte_vertrekken_en_overige_ruimten",
            "naam": "Oppervlakte van vertrekken en overige ruimten",
            "bovenliggendeCriterium": {
              "id": "punten_voor_de_woz_waarde__totaal__onderdeel_II"
            },
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 242.0,
          "criterium": {
            "id": "punten_voor_de_woz_waarde__factor_II",
            "naam": "Factor II",
            "bovenliggendeCriterium": {
              "id": "punten_voor_de_woz_waarde__totaal__onderdeel_II"
            }
          }
        },
        {
          "criterium": {
            "id": "punten_voor_de_woz_waarde__totaal__onderdeel_II",
            "naam": "Onderdeel II"
          },
          "punten": 19.38
        }
      ]
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "BIJ",
          "naam": "Bijzondere voorzieningen"
        }
      },
      "punten": 0.0,
      "woningwaarderingen": []
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "PMN",
          "naam": "Prijsopslag monumenten en nieuwbouw"
        }
      },
      "punten": 0.0,
      "woningwaarderingen": [],
      "opslagpercentage": 0.0
    }
  ],
  "maximaleHuur": 1900.64,
  "punten": 284.0,
  "stelsel": {
    "code": "ZEL",
    "naam": "Zelfstandige woonruimten"
  },
  "huurprijsopslag": 0.0,
  "maximaleHuurInclusiefOpslag": 1900.64
}
```

</details>

<details>
<summary>Voorbeeld output in tabel</summary>

```text
Oppervlakte van vertrekken                                          41.00 pt
Oppervlakte van overige ruimten
Verkoeling en verwarming                                             4.00 pt
Buitenruimten                                                       -5.00 pt
Energieprestatie                                                    22.00 pt
Keuken                                                               7.00 pt
Sanitair
Gemeenschappelijke parkeerruimten
Gemeenschappelijke vertrekken, overige ruimten en voorzieningen
Punten voor de WOZ-waarde                                          115.25 pt
Bijzondere voorzieningen
Prijsopslag monumenten en nieuwbouw
                                                                    --------
TOTAAL                                                             184.00 pt
Opslag                                                              0.00 EUR
Maximaal redelijke huur                                          1214.31 EUR

OPPERVLAKTE VAN VERTREKKEN
  Slaapkamer                                                21.05 m²
  Keuken                                                    20.37 m²
                                                            --------  --------
  Totaal                                                    41.42 m²  41.00 pt

VERKOELING EN VERWARMING
  Verwarmde vertrekken                                                 4.00 pt
    - Slaapkamer                                                                   2.00 pt
    - Keuken                                                                       2.00 pt
                                                                      --------
  Totaal                                                               4.00 pt

BUITENRUIMTEN
  Geen buitenruimten                                                  -5.00 pt
                                                                      --------
  Totaal                                                              -5.00 pt

ENERGIEPRESTATIE
  C (Energie-index)                                                   22.00 pt
                                                                      --------
  Totaal                                                              22.00 pt

KEUKEN
  Keuken: Lengte aanrecht                                 2700.00 mm   7.00 pt
                                                            --------  --------
  Totaal                                                  2700.00 mm   7.00 pt

PUNTEN VOOR DE WOZ-WAARDE
  WOZ-waarde op waardepeildatum 01-01-2024             694000.00 EUR
  Onderdeel I                                                         45.27 pt
    - Factor I                                              15329.00
  Onderdeel II                                                        69.95 pt
    - Oppervlakte van vertrekken en overige ruimten         41.00 m²
    - Factor II                                               242.00
                                                                      --------
  Totaal                                                              115.25 pt
```

</details>