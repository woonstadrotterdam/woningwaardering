![](https://img.shields.io/pypi/pyversions/woningwaardering)
![Build Status](https://github.com/woonstadrotterdam/woningwaardering/actions/workflows/cicd.yml/badge.svg)
[![Version](https://img.shields.io/pypi/v/woningwaardering)](https://pypi.org/project/woningwaardering/)
![](https://img.shields.io/github/license/woonstadrotterdam/woningwaardering)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

# Woningwaardering

Ga voor uitgebreide documentatie over de **woningwaardering** package naar [Read The Docs](https://woningwaardering.readthedocs.io/stable/).

<!--tip-start-->

> [!TIP]
> Deze versie kan gebruikt worden voor het berekenen van de woningwaardering volgens het woningwaarderingsstelsel voor zelfstandige woonruimten volgens [het beleidsboek van de huurcommissie van juli 2026 (Wet Betaalbare Huur)](https://www.huurcommissie.nl/huurcommissie-helpt/beleidsboeken_html). Aan de berekeningen en output van deze package kunnen geen rechten worden ontleend. Raadpleeg de [documentatie](https://woningwaardering.readthedocs.io/stable/), [de toelichting op de implementatie van het beleidsboek](https://woningwaardering.readthedocs.io/stable/implementatietoelichtingen/) en [de openstaande issues](https://github.com/woonstadrotterdam/woningwaardering/issues) aandachtig om de package op een constructieve manier te gebruiken en de resultaten correct te interpreteren.

<!--tip-end-->

## Doel

<!--overzicht-start-->

Het Microservices team van Woonstad Rotterdam is in Q1 2024 begonnen met het ontwikkelen met een open-source Python-package waarmee het mogelijk wordt om het puntensysteem van het [woningwaarderingsstelsel](https://aedes.nl/huurbeleid-en-betaalbaarheid/woningwaarderingsstelsel-wws) toe te passen. We gaan hierbij uit van de [VERA-standaard](https://www.coraveraonline.nl/index.php/VERA-standaard) [referentiedata v4.3.260116](https://github.com/Aedes-datastandaarden/vera-referentiedata) & [openapi v4.1.5](https://github.com/Aedes-datastandaarden/vera-openapi) van de corporatiesector voor de in- en output van de package. De reden van het maken van deze package is het volgende:

De package maakt het mogelijk om de woningwaardering te berekenen op basis van een digitale representatie van een woning. Steeds meer woningcorporaties en bedrijven digitaliseren hun woningbestand, vaak met behulp van een bouwwerkinformatiemodel (BIM). Met behulp van deze package worden bulkberekeningen van woningwaarderingen mogelijk. Bovendien kan de woningwaardering door deze package als API te gebruiken in een webapplicatie worden geïntegreerd. Onze berekening biedt een completere en inzichtelijkere berekening van het woningwaarderingsstelsel dan de momenteel beschikbare tools, zoals die van de [huurcommissie](https://www.huurcommissie.nl/huurders/sociale-huurwoning/maximale-huurprijs-berekenen). Omdat onze package volledig open-source is zijn alle geïmplementeerde regels transparent en traceerbaar. Het helpt ook woningcorporaties en bedrijven te voldoen aan de wetgeving zoals de [Wet Betaalbare Huur](https://www.volkshuisvestingnederland.nl/onderwerpen/wet-betaalbare-huur).

> [!NOTE]
> Voor vragen kunt u contact opnemen met Team Microservices via [Tomer Gabay](mailto:tomer.gabay@woonstadrotterdam.nl), [Tiddo Loos](mailto:tiddo.loos@woonstadrotterdam.nl) of [Ben Verhees](mailto:ben.verhees@woonstadrotterdam.nl).

---

![werking-package](https://raw.githubusercontent.com/woonstadrotterdam/woningwaardering/main/docs/afbeeldingen/diagram.png)
_Voorbeeld van hoe wij de woningwaardering package gebruiken bij Woonstad Rotterdam_.

---

Voorbeeld van de tekstuele output van de package voor een zelfstandige woonruimte:

```text
SAMENVATTING
  Oppervlakte van vertrekken                                          141.00 pt
  Oppervlakte van overige ruimten                                       5.25 pt
  Verkoeling en verwarming                                             14.00 pt
  Buitenruimten                                                        15.00 pt
  Energieprestatie                                                     22.00 pt
  Keuken                                                                7.00 pt
  Sanitair                                                             15.00 pt
  Gemeenschappelijke parkeerruimten
  Gemeenschappelijke vertrekken, overige ruimten en voorzieningen
  Punten voor de WOZ-waarde                                            64.75 pt
  Bijzondere voorzieningen
  Prijsopslag monumenten en nieuwbouw
                                                                      ---------
  Totaal afgerond op hele punten                                      284.00 pt
  Maximaal redelijke huur                                1900.64 EUR

OPPERVLAKTE VAN VERTREKKEN
  Slaapkamer 1                                             21.05 m²
  Woonkamer                                                41.00 m²
  Keuken                                                   20.37 m²
  Badruimte                                                 7.50 m²
  Slaapkamer 2                                             15.98 m²
  Slaapkamer 3                                             19.15 m²
  Slaapkamer 4                                             15.82 m²
                                                      ----------      ---------
  Totaal                                                  140.87 m²   141.00 pt

OPPERVLAKTE VAN OVERIGE RUIMTEN
  Berging                                                   6.65 m²
                                                      ----------      ---------
  Totaal                                                    6.65 m²     5.25 pt

VERKOELING EN VERWARMING
  Verwarmde vertrekken
    - Slaapkamer 1                                                      2.00 pt
    - Woonkamer                                                         2.00 pt
    - Keuken                                                            2.00 pt
    - Badruimte                                                         2.00 pt
    - Slaapkamer 2                                                      2.00 pt
    - Slaapkamer 3                                                      2.00 pt
    - Slaapkamer 4                                                      2.00 pt
                                                                      ---------
  Totaal                                                               14.00 pt

BUITENRUIMTEN
  Privé                                                    71.00 m²    24.85 pt
    - Balkon 1                                              3.14 m²
    - Balkon 2                                              3.14 m²
    - Tuin                                                 49.11 m²
    - Dakterras                                            15.93 m²
  Privé buitenruimten aanwezig                                          2.00 pt
  Maximaal 15 punten                                                  -11.85 pt
                                                                      ---------
  Totaal                                                               15.00 pt

ENERGIEPRESTATIE
  C (Energie-index)                                                    22.00 pt
                                                                      ---------
  Totaal                                                               22.00 pt

KEUKEN
  Keuken
    - Lengte aanrecht                                    2700.00 mm     7.00 pt
                                                                      ---------
  Totaal                                                                7.00 pt

SANITAIR
  Badruimte
    - Staand Toilet                                         1.00 st     2.00 pt
    - Wastafel                                              2.00 st     2.00 pt
    - Bad en douche                                         1.00 st     7.00 pt
  Toiletruimte
    - Staand Toilet                                         1.00 st     3.00 pt
    - Wastafel                                              1.00 st     1.00 pt
                                                                      ---------
  Totaal                                                               15.00 pt

PUNTEN VOOR DE WOZ-WAARDE
  WOZ-waarde op waardepeildatum 01-01-2024             694000.00 EUR
  Onderdeel I                                                          45.27 pt
    - Factor I                                          15329.00 EUR
  Onderdeel II                                                         19.38 pt
    - Oppervlakte van vertrekken en overige ruimten       148.00 m²
    - Factor II                                           242.00 EUR
  Afronding op kwartpunten                                              0.10 pt
                                                                      ---------
  Totaal                                                               64.75 pt
```

<!--overzicht-end-->

<!--implementatie-beleidsboek-start-->

## Implementatie beleidsboek huurcommissie

Voor het berekenen van een woningwaardering volgen we de beleidsboeken van de Nederlandse Huurcommissie voor de waarderingsstelsels voor [zelfstandige](https://www.huurcommissie.nl/support/beleidsboeken/waarderingsstelsel-zelfstandige-woonruimte) en [onzelfstandige](https://www.huurcommissie.nl/support/beleidsboeken/waarderingsstelsel-onzelfstandige-woonruimte) woonruimten.
De beleidsboeken van de Huurcommissie sluiten aan op de Nederlandse wet- en regelgeving zoals beschreven in het [Besluit huurprijzen woonruimte](https://wetten.overheid.nl/BWBR0003237/2026-01-01).

Om woningwaarderingen te kunnen berekenen, vertalen we het gepubliceerde beleid naar Python-code.
Een woningwaardering berekenen we op basis van eigenschappen van een woning, zoals oppervlakten van ruimten en energielabel.
De stelselgroepen waarop punten worden toegekend, zijn vastgelegd in het [woningwaarderingstelselgroep](https://www.coraveraonline.nl/index.php/Referentiedata:WONINGWAARDERINGSTELSELGROEP) op [www.coraveraonline.nl](https://www.coraveraonline.nl/).
Deze volgen we ook in de opzet van de `woningwaardering`-package.
Elke stelselgroep heeft een eigen Python-object met een naam die overeenkomt met [woningwaarderingstelselgroep](https://www.coraveraonline.nl/index.php/Referentiedata:WONINGWAARDERINGSTELSELGROEP).

Tijdens de ontwikkeling van deze package komt het voor dat we inconsistenties in de beleidsboeken vinden of dat er ruimte is voor interpretatie. Daarnaast kan het voorkomen dat de VERA-modellen, met eventuele uitbreidingen, niet toereikend zijn om de stelselgroep volgens het beleidsboek tot op de letter nauwkeurig te implementeren. In de [implementatietoelichtingen](https://woningwaardering.readthedocs.io/stable/implementatietoelichtingen/) onderbouwen wij hoe elke stelselgroep is geïmplementeerd en welke keuzes daarin gemaakt zijn.

<!--implementatie-beleidsboek-end-->

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

Ga voor voorbeelden van het gebruik van de woningwaardering package naar de [documentatie](https://woningwaardering.readthedocs.io/stable/aan-de-slag/#gebruik).
