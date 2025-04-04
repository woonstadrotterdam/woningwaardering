![](https://img.shields.io/pypi/pyversions/woningwaardering)
![Build Status](https://github.com/woonstadrotterdam/woningwaardering/actions/workflows/cicd.yml/badge.svg)
[![Version](https://img.shields.io/pypi/v/woningwaardering)](https://pypi.org/project/woningwaardering/)
![](https://img.shields.io/github/license/woonstadrotterdam/woningwaardering)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

# Woningwaardering

Ga voor uitgebreide documentatie over de **woningwaardering** package naar [Read The Docs](https://woningwaardering.readthedocs.io/nl/latest/).

## Status

![](https://progress-bar.xyz/100/?title=zelfstandige_woonruimten_jan_2025&width=120)  
![](https://progress-bar.xyz/100/?title=onzelfstandige_woonruimten_jan_2025&width=108)

<!--tip-start-->

> [!TIP]
> Release v3.x.x kan gebruikt worden voor het berekenen van de woningwaardering volgens het woningwaarderingsstelsel voor zelfstandige woonruimten volgens [het beleidsboek van de huurcommissie van januari 2025 (Wet Betaalbare Huur)](https://www.huurcommissie.nl/huurcommissie-helpt/beleidsboeken_html). Aan de berekeningen en output van deze package kunnen geen rechten worden ontleend. Raadpleeg de [documentatie](https://woningwaardering.readthedocs.io/nl/latest/), [de toelichting op de implementatie van het beleidsboek](https://woningwaardering.readthedocs.io/nl/latest/implementatietoelichtingen/) en [de openstaande issues](https://github.com/woonstadrotterdam/woningwaardering/issues) aandachtig om de package op een constructieve manier te gebruiken en de resultaten correct te interpreteren.

<!--tip-end-->

## Doel

<!--overzicht-start-->

Het Microservices team van Woonstad Rotterdam is in Q1 2024 begonnen met het ontwikkelen met een open-source Python-package waarmee het mogelijk wordt om het puntensysteem van het [woningwaarderingsstelsel](https://aedes.nl/huurbeleid-en-betaalbaarheid/woningwaarderingsstelsel-wws) toe te passen. We gaan hierbij uit van de [VERA-standaard](https://www.coraveraonline.nl/index.php/VERA-standaard) [referentiedata v4.2.250307](https://github.com/Aedes-datastandaarden/vera-referentiedata) & [openapi v4.1.5](https://github.com/Aedes-datastandaarden/vera-openapi) van de corporatiesector voor de in- en output van de package. Dit project heeft drie hoofddoelen:

- het mogelijk maken van het berekenen van de woningwaardering op basis van een digitale representatie van een woning:
  - steeds meer woningcorperaties en bedrijven digitaliseren hun woningbestand, bijvoorbeeld met behulp van een bouwwerkinformatiemodel (BIM).
  - de combinatie van digitale representaties van woningen en deze package maakt het mogelijk om de woningwaardering in bulk te berekenen.
  - door deze package als API te gebruiken kan de woningwaardering in een webapplicatie worden geïntegreerd.
- om tot een completere en inzichtelijkere woningwaarderingsstelsel-berekening te komen dan die nu beschikbaar zijn via tools zoals bijvoorbeeld die van de [huurcommissie](https://www.huurcommissie.nl/huurders/sociale-huurwoning/maximale-huurprijs-berekenen).
- om als woningcorporatie of bedrijf te blijven voldoen aan de wetging zoals [Wet Betaalbare Huur](https://www.volkshuisvestingnederland.nl/onderwerpen/wet-betaalbare-huur).

> [!NOTE]
> Voor vragen kunt u contact opnemen met Team Microservices via [Tomer Gabay](mailto:tomer.gabay@woonstadrotterdam.nl), [Tiddo Loos](mailto:tiddo.loos@woonstadrotterdam.nl) of [Ben Verhees](mailto:ben.verhees@woonstadrotterdam.nl).

---

![werking-package](https://raw.githubusercontent.com/woonstadrotterdam/woningwaardering/main/docs/afbeeldingen/diagram.png)
_Voorbeeld van hoe wij de woningwaardering package gebruiken bij Woonstad Rotterdam_.

---

![voorbeeld-output](https://raw.githubusercontent.com/woonstadrotterdam/woningwaardering/main/docs/afbeeldingen/voorbeeld_output.jpg)
_Visueel voorbeeld van de output van de package voor een zelfstandige woonruimte._

<!--overzicht-end-->

Voor meer details over wat er precies is geïmplementeerd van het beleidsboek van januari 2025 verwijzen wij naar de [documentatie](https://woningwaardering.readthedocs.io/nl/latest/implementatietoelichtingen.html) over de implementatie van dit beleidsboek.

Voor meer informatie over hoe de documentatie van het beleidsboek is gemaakt, verwijzen wij naar het hoofdstuk [Implementatie beleidsboek huurcommissie](https://woningwaardering.readthedocs.io/nl/latest/opzet_woningwaardering.html#implementatie-beleidsboek-huurcommissie).

# Opzet woningwaardering package

Voor de opzet van de Woningwaarderingpackage verwijzen we graag naar de [documentatie](https://woningwaardering.readthedocs.io/nl/latest/opzet_woningwaardering.html). Hier zal onder andere worden ingegaan op de implemenatie van de Beleidsboeken van de huurcommissie en de repository structuur worden besproken.

<!--installatie-start-->

# Installatie

Gebruikers kunnen de woningwaardering package installaren met

```bash
pip install woningwaardering
```

Vervolgens kun je de package importeren en gebruiken op verschillende manieren.

De woningwaardering package kan op basis van data van het Kadaster en Cultureel Erfgoed de monumentale status van een woning bepalen. Deze functionaliteit is optioneel en kan worden geïnstalleerd met

```bash
pip install woningwaardering[monumenten]
```

<!--installatie-end-->

# Gebruik

Ga voor voorbeelden van het gebruik van de woningwaardering package naar de [documentatie](https://woningwaardering.readthedocs.io/nl/latest/gebruik.html#voorbeeld-per-stelselgroep).
