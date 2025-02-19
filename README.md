![](https://img.shields.io/pypi/pyversions/woningwaardering)
![Build Status](https://github.com/woonstadrotterdam/woningwaardering/actions/workflows/cicd.yml/badge.svg)
[![Version](https://img.shields.io/pypi/v/woningwaardering)](https://pypi.org/project/woningwaardering/)
![](https://img.shields.io/github/license/woonstadrotterdam/woningwaardering)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

# Woningwaardering

## 📊 Status

![](https://progress-bar.xyz/100/?title=zelfstandige_woonruimten_jan_2025&width=120)  
![](https://progress-bar.xyz/100/?title=onzelfstandige_woonruimten_jan_2025&width=108)

> ⚠️ Release v3.x.x kan gebruikt worden voor het berekenen van de woningwaardering volgens het woningwaarderingsstelsel voor zelfstandige woonruimten volgens [het beleidsboek van de huurcommissie van januari 2025 (Wet Betaalbare Huur)](https://www.huurcommissie.nl/huurcommissie-helpt/beleidsboeken_html). Aan de berekeningen en output van deze package kunnen geen rechten worden ontleend. Raadpleeg de [README](https://github.com/woonstadrotterdam/woningwaardering#), [de toelichting op de implementatie van het beleidsboek](https://github.com/woonstadrotterdam/woningwaardering/tree/main/docs/implementatietoelichting-beleidsboeken) en [de openstaande issues](https://github.com/woonstadrotterdam/woningwaardering/issues) aandachtig om de package op een constructieve manier te gebruiken en de resultaten correct te interpreteren.

## Doel

Het Microservices team van Woonstad Rotterdam is in Q1 2024 begonnen met het ontwikkelen met een open-source Python-package waarmee het mogelijk wordt om het puntensysteem van het [woningwaarderingsstelsel](https://aedes.nl/huurbeleid-en-betaalbaarheid/woningwaarderingsstelsel-wws) toe te passen. We gaan hierbij uit van de [VERA-standaard](https://www.coraveraonline.nl/index.php/VERA-standaard) [referentiedata v4.2.250117](https://github.com/Aedes-datastandaarden/vera-referentiedata), [openapi v4.1.5](https://github.com/Aedes-datastandaarden/vera-openapi)] van de corporatiesector voor de in- en output van de package. Dit project heeft drie hoofddoelen:

- het mogelijk maken van het berekenen van de woningwaardering op basis van een digitale representatie van een woning:
  - steeds meer woningcorperaties en bedrijven digitaliseren hun woningbestand, bijvoorbeeld met behulp van een bouwwerkinformatiemodel (BIM).
  - de combinatie van digitale representaties van woningen en deze package maakt het mogelijk om de woningwaardering in bulk te berekenen.
  - door deze package als API te gebruiken kan de woningwaardering in een webapplicatie worden geïntegreerd.
- om tot een completere en inzichtelijkere woningwaarderingsstelsel-berekening te komen dan die nu beschikbaar zijn via tools zoals bijvoorbeeld die van de [huurcommissie](https://www.huurcommissie.nl/huurders/sociale-huurwoning/maximale-huurprijs-berekenen).
- om als woningcorporatie of bedrijf te blijven voldoen aan de wetging zoals [Wet Betaalbare Huur](https://www.volkshuisvestingnederland.nl/onderwerpen/wet-betaalbare-huur).

---

![werking-package](https://raw.githubusercontent.com/woonstadrotterdam/woningwaardering/main/docs/afbeeldingen/diagram.png)
_Voorbeeld van hoe wij de woningwaardering package gebruiken bij Woonstad Rotterdam_.

---

Voor meer details over wat er precies is geïmplementeerd van het beleidsboek van januari 2025 verwijzen wij naar de [documentatie](https://github.com/woonstadrotterdam/woningwaardering/blob/main/docs/implementatietoelichting-beleidsboeken/) over de implementatie van dit beleidsboek.
Voor meer informatie over hoe documentatie van het beleidsboek is gemaakt, verwijzen wij naar het hoofdstuk [Implementatie beleidsboek huurcommissie](https://github.com/woonstadrotterdam/woningwaardering?tab=readme-ov-file#implementatie-beleidsboek-huurcommissie) in deze `README`.

Voor vragen kunt u contact opnemen met Team Microservices via [Tomer Gabay](mailto:tomer.gabay@woonstadrotterdam.nl), [Tiddo Loos](mailto:tiddo.loos@woonstadrotterdam.nl) of [Ben Verhees](mailto:ben.verhees@woonstadrotterdam.nl).

![voorbeeld-output](https://raw.githubusercontent.com/woonstadrotterdam/woningwaardering/main/docs/afbeeldingen/voorbeeld_output.jpg)
_Visueel voorbeeld van de output van de package voor een zelfstandige woonruimte._

## Opzet woningwaardering package

### Implementatie beleidsboek huurcommissie

Voor het berekenen van een woningwaardering worden de [beleidsboeken van de Nederlandse Huurcommissie](https://www.huurcommissie.nl/huurcommissie-helpt/beleidsboeken) voor de waarderingstelsels voor zelfstandige en onzelfstandige woningen gevolgd.
De beleidsboeken van de Huurcommissie Nederland volgen Nederlandse wet- en regelgeving zoals beschreven in [Artikel 14 van het "Besluit huurprijzen woonruimte"](https://wetten.overheid.nl/BWBR0003237/2024-01-01#Artikel14).

Om berekeningen te maken met betrekking tot een woningwaardering wordt het gepubliceerde beleid vertaald naar Python-code.
Een woningwaardering wordt gemaakt op basis van woningelementen.
De stelselgroepen waarop gescoord wordt, zijn vastgelegd in het [woningwaarderingstelselgroep](https://www.coraveraonline.nl/index.php/Referentiedata:WONINGWAARDERINGSTELSELGROEP) op www.coraveraonline.nl.
Deze worden aangehouden in de opzet van de `woningwaardering`-package.
Voor elke stelselgroep wordt een apart Python-object gemaakt met een naam die overeenkomt met [woningwaarderingstelselgroep](https://www.coraveraonline.nl/index.php/Referentiedata:WONINGWAARDERINGSTELSELGROEP).

De woningwaardering package volgt de [beleidsboeken van de Nederlandse Huurcommissie](https://www.huurcommissie.nl/huurcommissie-helpt/beleidsboeken) en daarmee de Nederlandse wet en regelgeving m.b.t. het waarderen van woningen. Tijdens de ontwikkeling van deze package komt het voor dat we inconsistenties in de beleidsboeken vinden of dat er ruimte is voor interpretatie. Daarnaast kan het voorkomen dat dat de VERA modellen, met eventuele uitbreidingen, niet toereikend zijn om de stelselgroep voglens het beleidsboek tot op de letter nauwkeurig te implementeren. In [implementatietoelichting-beleidsboeken](https://github.com/woonstadrotterdam/woningwaardering/tree/main/docs/implementatietoelichting-beleidsboeken) onderbouwen wij hoe elke stelselgroep is geïmplementeerd en welke keuzes daarin gemaakt zijn.  
In deze documenten wordt bijgehouden welke onderdelen van het beleidsboek wel en niet zijn geïmplementeerd per stelselgroep. De gepubliceerde tekst uit het beleidsboek wordt gekopieerd en wanneer een onderdeel niet in de code van de package is geïmplementeerd zal dit worden aangegeven met ~~doorgestreepte tekst~~.  
De reden van het niet implementeren van een regelonderdeel is vrijwel altijd dat het technisch niet mogelijk is op basis van het inputmodel van de VERA-standaard. Een voorbeeld hiervan is dat voor oppervlakte van vertrekken de minimale breedte van een vertrek over de volledige lengte 1,5m moet zijn. Omdat wij de data van de minimale breedte over de volledige lengte niet binnenkrijgen via het inputmodel kunnen wij dit onderdeel van de regel niet implementeren. **Dit betekent dat het aan de gebruiker is om met deze regelonderdelen rekening te houden bij het eenheid-inputmodel.** Een deel van de deze regelonderdelen wordt al afgevangen indien het eenheid-inputmodel voldoet aan de NEN-norm.
Regels die wel zijn geïmplementeerd zijn niet doorgestreept.
Keuzes die zijn gemaakt en of interpretaties die zijn gedaan, worden in een gemarkeerd blok weergegeven zoals hieronder is gedaan.

> Dit is een tekstblok waarmee commentaar van een developer wordt aangegeven in het beleidsboek.

### Repository-structuur

De repository-structuur is ingedeeld volgens de [referentiedata van stelselgroepen van de VERA-standaard](https://www.coraveraonline.nl/index.php/Referentiedata:WONINGWAARDERINGSTELSELGROEP); eerst de stelsels (bijvoorbeeld _zelfstandig_, _onzelfstandig_) en vervolgens de stelselgroepen (bijvoorbeeld _Energieprestatie_, _Wasgelegenheid_).
In de folders van de stelselgroepen bevindt zich de code voor het berekenen van de punten per stelselgroep. Indien bepaalde logica voor zowel zelfstandige als onzelfstandige woningen gelden, dan bevinden deze regels zich in de folder _gedeelde_logcia_.

### Design

Het design van de `woningwaardering`-package is zo gekozen dat stelselgroep-objecten en bijbehorende regels modulair zijn.

### Lookup tabellen

In lookup tabellen worden constanten en variabelen opgeslagen die nodig zijn bij het berekenen van de punten voor een stelselgroep.
In de `woningwaardering` package wordt CSV gebruikt als bestandstype voor het opslaan van een lookup tabel.
De keuze is op CSV gevallen omdat lookup data soms bestaat uit meerdere datarijen waardoor dit vaak minder leesbaar wordt wanneer dit bijvoorbeeld in json of yaml wordt opgeslagen.

### Warnings

In de `woningwaardering` package worden `UserWarnings` gegenereerd wanneer de inputdata niet volledig of correct wordt aangeleverd.
Deze waarschuwingen worden gegeven met een warning bericht en een type warning, bijvoorbeeld:

```python
warnings.warn("Dit is een warning", UserWarning)
```

Standaard genereert de `woningwaardering` package een error wanneer een `UserWarning` wordt gegeven.
Hoewel de package kan werken met incomplete data, is ervoor gekozen om standaard te falen bij incomplete inputdata, zodat de gebruiker hiervan op de hoogte wordt gebracht.
Het is echter ook mogelijk om het warning filter terug te zetten naar de standaardinstellingen, waardoor een warning m.b.t. incomplete data niet leidt tot een error, maar slechts een _warning_:

```python
warnings.simplefilter("default", UserWarning)
```

Alle waarschuwingen die worden gegenereerd met `warnings.warn()`, worden standaard gelogd met `logger.warning()` en weergegeven in het standaardfout bestand.
Mocht door de gebruiker logging worden uitgezet, dan zullen de UserWarnings altijd te zien zijn voor de gebruiker in de output van de _stderr_.

#### Warning vs Exception

Er wordt doorgaans in de stelgroepversies gebruik gemaakt van `warnings.warn()` in plaats van het raisen van een exception.
Hierdoor bestaat de mogelijkheid om stelselgroepen te berekenen voor stelselgroepen waarvoor de data wel compleet genoeg is, mits de `warnings.simplefilter` naar `default` is gezet.

### Criterium ID's

De `CriteriumId` class wordt gebruikt om ID's te genereren voor criteria in de woningwaardering. Deze ID's worden opgebouwd uit verschillende onderdelen die worden samengevoegd met dubbele underscores (`__`).

De opbouw van een criterium ID kan de volgende onderdelen bevatten:

- Stelselgroep (verplicht, bijvoorbeeld 'buitenruimten' of 'energieprestatie')
- Ruimte ID (optioneel, bijvoorbeeld 'Space_108014713')
- Criterium (optioneel, bijvoorbeeld 'factor_II' of 'woz_waarde')
- Gedeeld met aantal (optioneel, voor gedeelde voorzieningen)
- Gedeeld met soort (optioneel, 'adressen' of 'onzelfstandige_woonruimten')
- Totaal indicator (optioneel)

Voorbeelden van gegenereerde ID's:

- `buitenruimten__Space_108014713` (voor een specifieke ruimte)
- `buitenruimten__totaal__prive` (voor een privé totaal)
- `gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__totaal__gedeeld_met__4__adressen` (voor gedeelde voorzieningen)

Bij gedeelde voorzieningen wordt automatisch 'prive' toegevoegd als het aantal 1 of minder is, en anders wordt het aantal en soort toegevoegd (bijvoorbeeld `gedeeld_met__4__adressen`).

Met deze ID's kan gerefereerd worden aan specifieke criteria in de output van de woningwaardering.

#### Criteriumsleutels

Bij sommige stelselgroepen heb je een aantal criteria die een gemeenschappelijke groep vormen. Bijvoorbeeld bij _verkoeling en verwarming_ mag je maximaal 2 extra punten krijgen voor vertrekken die verkoeld én verwarmd zijn. Daarnaast mag je ook maximaal 4 punten krijgen voor het aantal verwarmde overige- en verkeersruimten. Om te kunnen berekenen wat de som is van een subgroep en bijvoorbeeld maximering toe te passen maken wij gebruik van zogenoemde `criteriumSleutels`. Indien een waardering onderdeel is van een subgroep, dan wordt aan deze waardering in het veld `bovenliggendCriterium` de `id` toegevoegd van de waardering die hoort bij de subgroep. In het voorbeeld hieronder is bijvoorbeeld de subgroep `Verwarmde vertrekken` binnen `verkoeling en verwarming` duidelijk te zien in de output-tabel. Voorgedefinieerde criteriumsleutels vind je in `woningwaardering/stelsels/criteriumsleutels.py`. Momenteel ondersteunen wij nog geen meerdere niveau's van subgroepen. Een criterium dat voor een ander criterium een bovenliggend criterium is, mag zelf geen bovenliggend criterium hebben.

## Installatie

Gebruikers kunnen de woningwaardering package installaren met `pip install woningwaardering`. Vervolgens kun je de package importeren en gebruiken op verschillende manieren.

### Monumenten

De woningwaardering package kan op basis van data van het Kadaster en Cultureel Erfgoed de monumentale status van een woning bepalen. Deze functionaliteit is optioneel en kan worden geïnstalleerd met `pip install woningwaardering[monumenten]`.

## Gebruik

### Optie 1; bijvoorbeeld via JSON bestand

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
    peildatum=date(2025, 1, 1)  # bij niet meegeven wordt de huidige dag gebruikt.
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
          },
          "punten": 1.1
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
          },
          "punten": 1.1
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
          },
          "punten": 17.19
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
          },
          "punten": 5.57
        },
        {
          "criterium": {
            "id": "buitenruimten__aanwezig__prive",
            "naam": "Buitenruimten aanwezig",
            "bovenliggendeCriterium": {
              "id": "buitenruimten__totaal__prive"
            }
          },
          "punten": 2.0
        },
        {
          "aantal": 71.32,
          "criterium": {
            "id": "buitenruimten__totaal__prive",
            "naam": "Totaal (privé)",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          },
          "punten": 26.96
        },
        {
          "criterium": {
            "id": "buitenruimten__maximering",
            "naam": "Maximaal 15 punten"
          },
          "punten": -11.96
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
      "punten": 63.0,
      "woningwaarderingen": [
        {
          "aantal": 643000.0,
          "criterium": {
            "id": "punten_voor_de_woz_waarde__woz_waarde",
            "naam": "WOZ-waarde op waardepeildatum 01-01-2023"
          }
        },
        {
          "aantal": 14543.0,
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
          "punten": 44.21
        },
        {
          "aantal": 147.52,
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
          "aantal": 229.0,
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
          "punten": 19.03
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
  "maximaleHuur": 1820.52,
  "punten": 282.0,
  "stelsel": {
    "code": "ZEL",
    "naam": "Zelfstandige woonruimten"
  },
  "huurprijsopslag": 0.0,
  "maximaleHuurInclusiefOpslag": 1820.52
}
```

</details>

<details>
<summary>Voorbeeld output in tabel</summary>

```text
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Groep                             | Naam                                                                        |       Aantal | Meeteenheid         |  Punten |  Opslag |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Oppervlakte van vertrekken        | Slaapkamer 1                                                                |        21.05 | Vierkante meter, m2 |         |         |
| Oppervlakte van vertrekken        | Woonkamer                                                                   |        41.00 | Vierkante meter, m2 |         |         |
| Oppervlakte van vertrekken        | Keuken                                                                      |        20.37 | Vierkante meter, m2 |         |         |
| Oppervlakte van vertrekken        | Badruimte                                                                   |         7.50 | Vierkante meter, m2 |         |         |
| Oppervlakte van vertrekken        | Slaapkamer 2                                                                |        15.98 | Vierkante meter, m2 |         |         |
| Oppervlakte van vertrekken        | Slaapkamer 3                                                                |        19.15 | Vierkante meter, m2 |         |         |
| Oppervlakte van vertrekken        | Slaapkamer 4                                                                |        15.82 | Vierkante meter, m2 |         |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Oppervlakte van vertrekken        | Totaal                                                                      |       140.87 | Vierkante meter, m2 |  141.00 |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Oppervlakte van overige ruimten   | Berging                                                                     |         6.65 | Vierkante meter, m2 |         |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Oppervlakte van overige ruimten   | Totaal                                                                      |         6.65 | Vierkante meter, m2 |    5.25 |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Verkoeling en verwarming          | Verwarmde vertrekken                                                        |              |                     |   14.00 |         |
| Verkoeling en verwarming          |  - Slaapkamer 1                                                             |              |                     |  [2.00] |         |
| Verkoeling en verwarming          |  - Woonkamer                                                                |              |                     |  [2.00] |         |
| Verkoeling en verwarming          |  - Keuken                                                                   |              |                     |  [2.00] |         |
| Verkoeling en verwarming          |  - Badruimte                                                                |              |                     |  [2.00] |         |
| Verkoeling en verwarming          |  - Slaapkamer 2                                                             |              |                     |  [2.00] |         |
| Verkoeling en verwarming          |  - Slaapkamer 3                                                             |              |                     |  [2.00] |         |
| Verkoeling en verwarming          |  - Slaapkamer 4                                                             |              |                     |  [2.00] |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Verkoeling en verwarming          | Totaal                                                                      |              |                     |   14.00 |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Buitenruimten                     | Totaal (privé)                                                              |        71.32 | Vierkante meter, m2 |   26.96 |         |
| Buitenruimten                     |  - Balkon 1                                                                 |       [3.14] | Vierkante meter, m2 |  [1.10] |         |
| Buitenruimten                     |  - Balkon 2                                                                 |       [3.14] | Vierkante meter, m2 |  [1.10] |         |
| Buitenruimten                     |  - Tuin                                                                     |      [49.11] | Vierkante meter, m2 | [17.19] |         |
| Buitenruimten                     |  - Dakterras                                                                |      [15.93] | Vierkante meter, m2 |  [5.57] |         |
| Buitenruimten                     |  - Buitenruimten aanwezig                                                   |              |                     |  [2.00] |         |
| Buitenruimten                     | Maximaal 15 punten                                                          |              |                     |  -11.96 |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Buitenruimten                     | Totaal                                                                      |              |                     |   15.00 |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Energieprestatie                  | C (Energie-index)                                                           |              |                     |   22.00 |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Keuken                            | Keuken: Lengte aanrecht                                                     |      2700.00 | Millimeter          |    7.00 |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Keuken                            | Totaal                                                                      |      2700.00 | Millimeter          |    7.00 |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Sanitair                          | Badruimte - Staand Toilet                                                   |         1.00 |                     |    2.00 |         |
| Sanitair                          | Badruimte - Wastafel                                                        |         2.00 |                     |    2.00 |         |
| Sanitair                          | Badruimte - Bad en douche                                                   |         1.00 |                     |    7.00 |         |
| Sanitair                          | Toiletruimte - Staand Toilet                                                |         1.00 |                     |    3.00 |         |
| Sanitair                          | Toiletruimte - Wastafel                                                     |         1.00 |                     |    1.00 |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Sanitair                          | Totaal                                                                      |              |                     |   15.00 |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Punten voor de WOZ-waarde         | WOZ-waarde op waardepeildatum 01-01-2023                                    |   [643000.0] |                     |         |         |
| Punten voor de WOZ-waarde         | Onderdeel I                                                                 |              |                     |   44.21 |         |
| Punten voor de WOZ-waarde         |  - Factor I                                                                 |    [14543.0] |                     |         |         |
| Punten voor de WOZ-waarde         | Onderdeel II                                                                |              |                     |   19.03 |         |
| Punten voor de WOZ-waarde         |  - Oppervlakte van vertrekken en overige ruimten                            |     [147.52] | Vierkante meter, m2 |         |         |
| Punten voor de WOZ-waarde         |  - Factor II                                                                |      [229.0] |                     |         |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Punten voor de WOZ-waarde         | Totaal                                                                      |              |                     |   63.00 |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Zelfstandige woonruimten          | Afgerond totaal                                                             |              |                     |  282.00 |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
|                                   | Maximale huur                                                               |      1820.52 | EUR                 |         |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
```

</details>

### Optie 2; via Python

```python
from datetime import date

from woningwaardering import Woningwaardering
from woningwaardering.stelsels.utils import naar_tabel
from woningwaardering.vera.bvg.generated import (
    BouwkundigElementenBouwkundigElement,
    EenhedenAdresseerbaarObjectBasisregistratie,
    EenhedenEenheid,
    EenhedenEenheidadres,
    EenhedenEnergieprestatie,
    EenhedenPand,
    EenhedenRuimte,
    EenhedenWoonplaats,
    EenhedenWozEenheid,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Bouwkundigelementsoort,
    Energielabel,
    Energieprestatiesoort,
    Energieprestatiestatus,
    Pandsoort,
    Ruimtedetailsoort,
    Ruimtesoort,
    Woningwaarderingstelsel,
)

wws = Woningwaardering(peildatum=date(2025, 1, 1))

eenheid = EenhedenEenheid(
    id="<id>",
    bouwjaar=1924,
    woningwaarderingstelsel=Woningwaarderingstelsel.zelfstandige_woonruimten,
    adres=EenhedenEenheidadres(
        straatnaam="<straatnaam>",
        huisnummer="<huisnummer>",
        huisnummer_toevoeging="",
        postcode="<postcode>",
        woonplaats=EenhedenWoonplaats(naam="ROTTERDAM"),
    ),
    adresseerbaar_object_basisregistratie=EenhedenAdresseerbaarObjectBasisregistratie(
        id="0599010000485697", bag_identificatie="0599010000485697"
    ),
    panden=[
        EenhedenPand(
            soort=Pandsoort.eengezinswoning,
        )
    ],
    woz_eenheden=[
        EenhedenWozEenheid(
            waardepeildatum=date(2022, 1, 1), vastgestelde_waarde=618000
        ),
        EenhedenWozEenheid(
            waardepeildatum=date(2023, 1, 1), vastgestelde_waarde=643000
        ),
    ],
    energieprestaties=[
        EenhedenEnergieprestatie(
            soort=Energieprestatiesoort.energie_index,
            status=Energieprestatiestatus.definitief,
            begindatum=date(2019, 2, 25),
            einddatum=date(2029, 2, 25),
            registratiedatum="2019-02-26T14:51:38+01:00",
            label=Energielabel.c,
            waarde="1.58",
        )
    ],
    gebruiksoppervlakte=187,
    monumenten=[],
    ruimten=[
        EenhedenRuimte(
            id="Space_108014589",
            soort=Ruimtesoort.vertrek,
            detail_soort=Ruimtedetailsoort.slaapkamer,
            naam="Slaapkamer",
            inhoud=60.4048,
            oppervlakte=21.047,
            verwarmd=True,
        ),
        EenhedenRuimte(
            id="Space_108006229",
            soort=Ruimtesoort.vertrek,
            detail_soort=Ruimtedetailsoort.keuken,
            naam="Keuken",
            inhoud=57.4359,
            oppervlakte=20.3673,
            verwarmd=True,
            bouwkundige_elementen=[
                BouwkundigElementenBouwkundigElement(
                    id="Aanrecht_108006231",
                    naam="Aanrecht",
                    omschrijving="Aanrecht in Keuken",
                    soort=Bouwkundigelementsoort.voorziening,
                    detail_soort=Bouwkundigelementdetailsoort.aanrecht,
                    lengte=2700,
                )
            ],
        ),
    ],
)

woningwaardering_resultaat = wws.waardeer(eenheid)
print(
    woningwaardering_resultaat.model_dump_json(
        by_alias=True, indent=2, exclude_none=True
    )
)
tabel = naar_tabel(woningwaardering_resultaat)

print(tabel)
```

De output daarvan is een VERA woningwaarderingstelsel object. Dit object kan vervolgens worden omgezet naar een tabel zoals hierboven is gedaan.

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
      "punten": 41.0,
      "woningwaarderingen": [
        {
          "aantal": 21.05,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_108014589",
            "naam": "Slaapkamer",
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
          "code": "VKV",
          "naam": "Verkoeling en verwarming"
        }
      },
      "punten": 4.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__Space_108014589",
            "naam": "Slaapkamer",
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
            "id": "verkoeling_en_verwarming__totaal__verwarmde_vertrekken",
            "naam": "Verwarmde vertrekken"
          },
          "punten": 4.0
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
      "punten": -5.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "buitenruimten__geen_buitenruimten",
            "naam": "Geen buitenruimten"
          },
          "punten": -5.0
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
      "punten": 112.0,
      "woningwaarderingen": [
        {
          "aantal": 643000.0,
          "criterium": {
            "id": "punten_voor_de_woz_waarde__woz_waarde",
            "naam": "WOZ-waarde op waardepeildatum 01-01-2023"
          }
        },
        {
          "aantal": 14543.0,
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
          "punten": 44.21
        },
        {
          "aantal": 41.42,
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
          "aantal": 229.0,
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
          "punten": 67.79
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
  "maximaleHuur": 1151.72,
  "punten": 181.0,
  "stelsel": {
    "code": "ZEL",
    "naam": "Zelfstandige woonruimten"
  },
  "huurprijsopslag": 0.0,
  "maximaleHuurInclusiefOpslag": 1151.72
}
```

</details>

<details>
<summary>Voorbeeld output in tabel</summary>

```text
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Groep                             | Naam                                                                        |       Aantal | Meeteenheid         |  Punten |  Opslag |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Oppervlakte van vertrekken        | Slaapkamer                                                                  |        21.05 | Vierkante meter, m2 |         |         |
| Oppervlakte van vertrekken        | Keuken                                                                      |        20.37 | Vierkante meter, m2 |         |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Oppervlakte van vertrekken        | Totaal                                                                      |        41.42 | Vierkante meter, m2 |   41.00 |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Verkoeling en verwarming          | Verwarmde vertrekken                                                        |              |                     |    4.00 |         |
| Verkoeling en verwarming          |  - Slaapkamer                                                               |              |                     |  [2.00] |         |
| Verkoeling en verwarming          |  - Keuken                                                                   |              |                     |  [2.00] |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Verkoeling en verwarming          | Totaal                                                                      |              |                     |    4.00 |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Buitenruimten                     | Geen buitenruimten                                                          |              |                     |   -5.00 |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Energieprestatie                  | C (Energie-index)                                                           |              |                     |   22.00 |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Keuken                            | Keuken: Lengte aanrecht                                                     |      2700.00 | Millimeter          |    7.00 |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Keuken                            | Totaal                                                                      |      2700.00 | Millimeter          |    7.00 |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Punten voor de WOZ-waarde         | WOZ-waarde op waardepeildatum 01-01-2023                                    |   [643000.0] |                     |         |         |
| Punten voor de WOZ-waarde         | Onderdeel I                                                                 |              |                     |   44.21 |         |
| Punten voor de WOZ-waarde         |  - Factor I                                                                 |    [14543.0] |                     |         |         |
| Punten voor de WOZ-waarde         | Onderdeel II                                                                |              |                     |   67.79 |         |
| Punten voor de WOZ-waarde         |  - Oppervlakte van vertrekken en overige ruimten                            |      [41.42] | Vierkante meter, m2 |         |         |
| Punten voor de WOZ-waarde         |  - Factor II                                                                |      [229.0] |                     |         |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Punten voor de WOZ-waarde         | Totaal                                                                      |              |                     |  112.00 |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Zelfstandige woonruimten          | Afgerond totaal                                                             |              |                     |  181.00 |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
|                                   | Maximale huur                                                               |      1151.72 | EUR                 |         |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
```

</details>
