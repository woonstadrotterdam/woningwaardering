# Opzet woningwaardering package

## Implementatie beleidsboek huurcommissie

Voor het berekenen van een woningwaardering volgen we de beleidsboeken van de Nederlandse Huurcommissie voor de waarderingsstelsels voor [zelfstandige](https://www.huurcommissie.nl/support/beleidsboeken/waarderingsstelsel-zelfstandige-woonruimte) en [onzelfstandige](https://www.huurcommissie.nl/support/beleidsboeken/waarderingsstelsel-onzelfstandige-woonruimte) woonruimten.
De beleidsboeken van de Huurcommissie sluiten aan op de Nederlandse wet- en regelgeving zoals beschreven in het [Besluit huurprijzen woonruimte](https://wetten.overheid.nl/BWBR0003237/2026-01-01).

Om woningwaarderingen te kunnen berekenen, vertalen we het gepubliceerde beleid naar Python-code.
Een woningwaardering berekenen we op basis van eigenschappen van een woning, zoals oppervlakten van ruimten en energielabel.
De stelselgroepen waarop punten worden toegekend, zijn vastgelegd in het [woningwaarderingstelselgroep](https://www.coraveraonline.nl/index.php/Referentiedata:WONINGWAARDERINGSTELSELGROEP) op [www.coraveraonline.nl](https://www.coraveraonline.nl/).
Deze volgen we ook in de opzet van de `woningwaardering`-package.
Elke stelselgroep heeft een eigen Python-object met een naam die overeenkomt met [woningwaarderingstelselgroep](https://www.coraveraonline.nl/index.php/Referentiedata:WONINGWAARDERINGSTELSELGROEP).

De woningwaardering package volgt de beleidsboeken van de Nederlandse Huurcommissie voor [zelfstandige](https://www.huurcommissie.nl/support/beleidsboeken/waarderingsstelsel-zelfstandige-woonruimte) en [onzelfstandige](https://www.huurcommissie.nl/support/beleidsboeken/waarderingsstelsel-onzelfstandige-woonruimte) woonruimten, en daarmee de Nederlandse wet en regelgeving m.b.t. het waarderen van woningen. Tijdens de ontwikkeling van deze package komt het voor dat we inconsistenties in de beleidsboeken vinden of dat er ruimte is voor interpretatie. Daarnaast kan het voorkomen dat de VERA modellen, met eventuele uitbreidingen, niet toereikend zijn om de stelselgroep volgens het beleidsboek tot op de letter nauwkeurig te implementeren. In de [implementatietoelichtingen](../implementatietoelichtingen/index.md) onderbouwen wij hoe elke stelselgroep is geïmplementeerd en welke keuzes daarin gemaakt zijn.  

## Repository-structuur

De repository-structuur volgt de [referentiedata van stelselgroepen van de VERA-standaard](https://www.coraveraonline.nl/index.php/Referentiedata:WONINGWAARDERINGSTELSELGROEP): eerst de stelsels (bijvoorbeeld _zelfstandig_ en _onzelfstandig_) en daarbinnen de stelselgroepen (bijvoorbeeld _Energieprestatie_ en _Wasgelegenheid_).
In de folders van de stelselgroepen staat de code voor het berekenen van de punten per stelselgroep. Als bepaalde logica voor zowel zelfstandige als onzelfstandige woningen geldt, staat die in de folder _gedeelde_logica_.

## Design

De `woningwaardering`-package is zo opgezet dat stelselgroep-objecten en bijbehorende regels modulair zijn.

## Lookuptabellen

In lookuptabellen slaan we constanten en variabelen op die nodig zijn om de punten van een stelselgroep te berekenen.
In de `woningwaardering`-package gebruiken we CSV als bestandsformaat voor lookuptabellen.
Dat formaat is bewust gekozen: zodra lookuptabeldata uit meerdere rijen bestaat, blijft CSV vaak beter leesbaar dan bijvoorbeeld JSON of YAML.

## Warnings

In de `woningwaardering`-package genereren we `UserWarning`s wanneer inputdata onvolledig of onjuist is.
Deze waarschuwingen geven we mee met een bericht en een warningtype, bijvoorbeeld:

```python
warnings.warn("Dit is een warning", UserWarning)
```

Standaard leidt een `UserWarning` in de `woningwaardering`-package tot een error.
Hoewel de package kan werken met incomplete data, kiezen we ervoor om standaard te falen bij incomplete inputdata, zodat gebruikers weten dat invoer ontbreekt of onjuist is.
Het is echter ook mogelijk om het warningfilter terug te zetten naar de standaardinstellingen. In dat geval leidt een waarschuwing over incomplete of onjuiste data niet tot een error, maar verschijnt die alleen als waarschuwing:

```python
warnings.simplefilter("default", UserWarning)
```

Soms ondersteunen we tijdelijk nog even velden die eigenlijk niet meer gebruikt mogen worden, bijvoorbeeld na een wijziging in VERA. In dat geval tonen we een `DeprecationWarning`. Zo'n `DeprecationWarning` tonen we wel en loggen we ook, maar die leidt niet tot een error.

Alle waarschuwingen die met `warnings.warn()` worden gegenereerd, loggen we via `logger.warning()` (als logging aanstaat) en tonen we via de standaardfoutuitvoer (_stderr_).
Ook als logging uitstaat, blijven deze waarschuwingen zichtbaar via _stderr_.

### Warning vs Exception

In de stelselgroepen gebruiken we doorgaans `warnings.warn()` in plaats van het raisen van een exceptie.
Daardoor kunnen stelselgroepen waarvoor de data wel compleet genoeg is nog steeds worden berekend, mits `warnings.simplefilter` op `default` staat.

## Criteriumstrategie

Tijdens een `waardeer()`-aanroep bouw je de uitkomst van een stelselgroep eerst op als een hiërarchie van waarderingen. Daarvoor gebruiken we de builders in `woningwaardering/stelsels/builders.py`. Een `WaarderingsgroepBuilder` verzamelt de waarderingen binnen één stelselgroep, terwijl een `WaarderingBuilder` één afzonderlijke waardering opbouwt. Pas bij `build()` vertalen we die hiërarchie naar een resultaat in VERA-format: een platte lijst waarderingen waarin de samenhang via `bovenliggendeCriterium` is vastgelegd.

Je bouwt die hiërarchie op met drie methoden. Met `met_onderliggend(...)` voeg je een inhoudelijke waardering toe: een regel die punten en/of een aantal kan dragen. Met `met_subgroep(...)` voeg je een groeperende tussenlaag toe waaronder je meerdere waarderingen kunt bundelen. Met `gedeeld_met(...)` voeg je de laag toe die aangeeft of een ruimte privé is of met hoeveel adressen en onzelfstandige woonruimten hij gedeeld wordt.

### Criterium-id's

Binnen de hiërarchische structuur heeft elke waardering een criterium met een uniek id. Dat id is een pad-id: de builders leiden het af uit de positie van de waardering in de structuur en houden `criterium.id` en `bovenliggendeCriterium` daarbij gerelateerd aan elkaar.

Een waardering direct onder de stelselgroep krijgt het id `{stelselgroep}__{segment}`. Een waardering onder een andere waardering krijgt een id op basis van het bovenliggende criterium: `{bovenliggende_id}__{segment}`. De segmenten worden steeds met een dubbele underscore (`__`) aan elkaar gekoppeld.

Het criterium-id beschrijft daarmee zowel de identiteit van het criterium als de plek ervan in de hiërarchie. De punten en het aantal horen bij de waardering zelf en maken geen onderdeel uit van het criterium.

Voor de gedeeld-met-lagen gelden vaste segmentnamen: `prive` bij een aantal van ten hoogste 1, en `gedeeld_met_{n}_{soort}` bij een aantal groter dan 1 (met enkele underscores rond het aantal en de soort).

Een paar voorbeelden:

- `buitenruimten__prive__Space_108014713`
- `buitenruimten__gedeeld_met_2_adressen__Space_108006357`
- `buitenruimten__prive`
- `gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_adressen`
- `gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_adressen__keuken`
- `verkoeling_en_verwarming__verwarmde_vertrekken`

Zo'n stelselgroep bouw je stapsgewijs op: je begint met `WaarderingsgroepBuilder(stelsel, stelselgroep)`, hangt inhoudelijke waarderingen aan met `met_onderliggend(...)`, structurele tussenlagen met `met_subgroep(...)` en gedeeld-met-lagen met `gedeeld_met(...)`, en sluit af met `build()`. Die laatste telt de punten op en rondt de totaalpunten van de stelselgroep af op kwartpunten. Ontstaat door die afronding een verschil tussen de som van de waarderingen en de totaalpunten van de stelselgroep, dan voegen we dat verschil toe als waardering **Afronding op kwartpunten**. Uiteindelijk leveren deze stappen een `WoningwaarderingResultatenWoningwaarderingGroep` op.

### Lazy activatie

Een subgroep of gedeeld-met-laag verschijnt pas in de output zodra er daadwerkelijk iets onder hangt, of zodra er punten, een aantal of een opslagpercentage aan wordt toegekend. Zo blijven lege groeperende regels achterwege: een laag zonder inhoud blijft onzichtbaar en telt niet mee.

### Gelaagd delen met `gedeeld_met`

Bij gedeelde ruimten kan er op twee niveaus sprake zijn van deling. `gedeeld_met(...)` voegt daarom eerst, waar van toepassing, de laag voor deling met onzelfstandige woonruimten toe, en daaronder de laag voor deling met adressen. Als er op geen van beide niveaus wordt gedeeld, ontstaat er één privélaag.

### Subgroepen

Een subgroep is een groeperend criterium binnen een stelselgroep; het is nadrukkelijk zelf géén stelselgroep. Wat een subgroep groepeert, verschilt per stelselgroep. In een gemeenschappelijke stelselgroep, zoals `gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen`, spiegelt de id van een subgroep een stelselgroep-naam (bijvoorbeeld `sanitair`, `verkoeling_en_verwarming` of `oppervlakte_van_vertrekken`), omdat daar de logica van een hele stelselgroep genest wordt hergebruikt; onder zo'n subgroep kan vervolgens nóg een subgroep hangen. In een gewone stelselgroep is een subgroep juist een inhoudelijk onderdeel van die ene stelselgroep, zoals `verwarmde_vertrekken` of `verkoelde_vertrekken` binnen Verkoeling en verwarming.

Meestal draagt een subgroep zelf geen punten: die staan op de onderliggende detailregels. Op een enkele plek is dat anders. Bij de oppervlakte-stelselgroepen (`oppervlakte_van_vertrekken` en `oppervlakte_van_overige_ruimten`) worden de punten berekend over het op hele vierkante meters afgeronde groepstotaal, en daarom op de subgroep zelf gezet. De onderliggende ruimteregels dragen dan alleen het aantal vierkante meters en geen punten.

### Voorbeeld van de opbouw

De onderstaande bomen tonen een gemeenschappelijke stelselgroep voor een zelfstandige en een onzelfstandige eenheid. Links staat telkens een herkenbare voorbeeldnaam, rechts de rol die de regel in de structuur speelt.

> Uiteindelijk, door hoe VERA is opgebouwd, is élke regel hieronder technisch gezien een waardering met een criterium.

**Zelfstandig**

```text
Gemeenschappelijke vertrekken, overige ruimten en voorzieningen  ← stelselgroep
└─ Gedeeld met 5 adressen                                         ← gedeeld-met-criterium
   ├─ Oppervlakte van vertrekken                                  ← subgroep met punten
   │  └─ Keuken                                                   ← waardering met aantal (m²); punten op subgroep
   ├─ Verkoeling en verwarming                                    ← subgroep 
   │  └─ Verwarmde vertrekken                                     ← subgroep 
   │     └─ Keuken                                                ← waardering met punten
   └─ Keuken                                                      ← subgroep 
      └─ Keuken                                                   ← subgroep (per ruimte)
         ├─ Lengte aanrecht                                       ← waardering met punten
         └─ Extra voorzieningen                                   ← subgroep 
            └─ Inbouw koelkast                                    ← waardering met punten
```

**Onzelfstandig**

```text
Gemeenschappelijke binnenruimten gedeeld met meerdere adressen   ← stelselgroep
└─ Gedeeld met 4 onzelfstandige woonruimten                       ← gedeeld-met-criterium
   └─ Gedeeld met 4 adressen                                      ← gedeeld-met-criterium
      ├─ Oppervlakte van vertrekken                               ← subgroep met punten
      │  └─ Keuken                                                ← waardering met aantal (m²); punten op subgroep
      ├─ Verkoeling en verwarming                                 ← subgroep
      │  └─ Verwarmde vertrekken                                  ← subgroep
      │     └─ Keuken                                             ← waardering met punten
      ├─ Keuken                                                   ← subgroep
      │  └─ Keuken                                                ← subgroep (per ruimte)
      │     ├─ Lengte aanrecht                                    ← waardering met punten
      │     └─ Extra voorzieningen                                ← subgroep
      │        └─ Inbouw koelkast                                 ← waardering met punten
      └─ Sanitair                                                 ← subgroep
         └─ Toilet                                                ← subgroep (per ruimte)
            └─ Wastafel                                           ← waardering met punten
```
