# Opzet woningwaardering package

## Implementatie beleidsboek huurcommissie

Voor het berekenen van een woningwaardering worden de beleidsboeken van de Nederlandse Huurcommissie voor de waarderingsstelsels voor [zelfstandige](https://www.huurcommissie.nl/support/beleidsboeken/waarderingsstelsel-zelfstandige-woonruimte) en [onzelfstandige](https://www.huurcommissie.nl/support/beleidsboeken/waarderingsstelsel-onzelfstandige-woonruimte) woonruimten gevolgd.
De beleidsboeken van de Huurcommissie Nederland volgen Nederlandse wet- en regelgeving zoals beschreven in het [Besluit huurprijzen woonruimte](https://wetten.overheid.nl/BWBR0003237/2026-01-01).

Om berekeningen te maken met betrekking tot een woningwaardering wordt het gepubliceerde beleid vertaald naar Python-code.
Een woningwaardering wordt gemaakt op basis van woningelementen.
De stelselgroepen waarop gescoord wordt, zijn vastgelegd in het [woningwaarderingstelselgroep](https://www.coraveraonline.nl/index.php/Referentiedata:WONINGWAARDERINGSTELSELGROEP) op www.coraveraonline.nl.
Deze worden aangehouden in de opzet van de `woningwaardering`-package.
Voor elke stelselgroep wordt een apart Python-object gemaakt met een naam die overeenkomt met [woningwaarderingstelselgroep](https://www.coraveraonline.nl/index.php/Referentiedata:WONINGWAARDERINGSTELSELGROEP).

De woningwaardering package volgt de beleidsboeken van de Nederlandse Huurcommissie voor [zelfstandige](https://www.huurcommissie.nl/support/beleidsboeken/waarderingsstelsel-zelfstandige-woonruimte) en [onzelfstandige](https://www.huurcommissie.nl/support/beleidsboeken/waarderingsstelsel-onzelfstandige-woonruimte) woonruimten, en daarmee de Nederlandse wet en regelgeving m.b.t. het waarderen van woningen. Tijdens de ontwikkeling van deze package komt het voor dat we inconsistenties in de beleidsboeken vinden of dat er ruimte is voor interpretatie. Daarnaast kan het voorkomen dat de VERA modellen, met eventuele uitbreidingen, niet toereikend zijn om de stelselgroep volgens het beleidsboek tot op de letter nauwkeurig te implementeren. In de [implementatietoelichtingen](../implementatietoelichtingen/index.md) onderbouwen wij hoe elke stelselgroep is geïmplementeerd en welke keuzes daarin gemaakt zijn.  

## Repository-structuur

De repository-structuur is ingedeeld volgens de [referentiedata van stelselgroepen van de VERA-standaard](https://www.coraveraonline.nl/index.php/Referentiedata:WONINGWAARDERINGSTELSELGROEP); eerst de stelsels (bijvoorbeeld _zelfstandig_, _onzelfstandig_) en vervolgens de stelselgroepen (bijvoorbeeld _Energieprestatie_, _Wasgelegenheid_).
In de folders van de stelselgroepen bevindt zich de code voor het berekenen van de punten per stelselgroep. Indien bepaalde logica voor zowel zelfstandige als onzelfstandige woningen gelden, dan bevinden deze regels zich in de folder _gedeelde_logica_.

## Design

Het design van de `woningwaardering`-package is zo gekozen dat stelselgroep-objecten en bijbehorende regels modulair zijn.

## Lookuptabellen

In lookuptabellen worden constanten en variabelen opgeslagen die nodig zijn bij het berekenen van de punten voor een stelselgroep.
In de `woningwaardering` package wordt CSV gebruikt als bestandstype voor het opslaan van een lookuptabel.
De keuze is op CSV gevallen omdat lookuptabeldata soms bestaat uit meerdere datarijen waardoor dit vaak minder leesbaar wordt wanneer dit bijvoorbeeld in json of yaml wordt opgeslagen.

## Warnings

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

Voor verouderde input (bijvoorbeeld hernoemde modelattributen) gebruikt de package `DeprecationWarning`. Die blijven werken als warning: ze worden getoond en gelogd, maar leiden niet tot een error.

Alle waarschuwingen die worden gegenereerd met `warnings.warn()`, worden standaard gelogd met `logger.warning()` en weergegeven in het standaardfout bestand.
Mocht door de gebruiker logging worden uitgezet, dan zullen de warnings altijd te zien zijn voor de gebruiker in de output van de _stderr_.

### Warning vs Exception

Er wordt doorgaans in de stelselgroepversies gebruik gemaakt van `warnings.warn()` in plaats van het raisen van een exception.
Hierdoor bestaat de mogelijkheid om stelselgroepen te berekenen voor stelselgroepen waarvoor de data wel compleet genoeg is, mits de `warnings.simplefilter` naar `default` is gezet.

## Criteriumstrategie

Tijdens een `waardeer()`-aanroep bouwen de builders in `woningwaardering/stelsels/builders.py` de uitkomst van een stelselgroep stap voor stap op. Een `WaarderingsgroepBuilder` verzamelt de waarderingen van één stelselgroep, en een `WaarderingBuilder` staat voor één waardering-in-opbouw. Terwijl de berekening loopt, hang je waarderingen onder elkaar tot een hiërarchie. Pas bij `build()` wordt die hiërarchie omgezet naar het VERA-resultaat: een platte lijst waarderingen waarin de onderlinge samenhang wordt vastgelegd met een verwijzing naar het bovenliggende criterium.

Je bouwt die hiërarchie op met drie methoden. Met `met_onderliggend(...)` voeg je een inhoudelijke waardering toe: een regel die punten en/of een aantal kan dragen. Met `met_subgroep(...)` voeg je een groeperende tussenlaag toe waaronder je meerdere waarderingen kunt bundelen. Met `gedeeld_met(...)` voeg je de laag toe die aangeeft of een ruimte privé is of met hoeveel adressen en onzelfstandige woonruimten hij gedeeld wordt.

### Lazy activatie

Een subgroep of gedeeld-met-laag verschijnt pas in de output zodra er daadwerkelijk iets onder hangt, of zodra er punten, een aantal of een opslagpercentage aan wordt toegekend. Zo blijven lege groeperende regels achterwege: een laag zonder inhoud blijft onzichtbaar en telt niet mee.

### Gelaagd delen met `gedeeld_met`

Bij gedeelde ruimten kan er op twee niveaus sprake zijn van deling. `gedeeld_met(...)` legt daarom eerst, waar van toepassing, de laag voor deling met onzelfstandige woonruimten aan, en daaronder de laag voor deling met adressen. Wordt er op geen van beide niveaus gedeeld, dan ontstaat er één privélaag.

### Subgroepen

Een subgroep is een groeperend criterium binnen een stelselgroep; het is nadrukkelijk zelf géén stelselgroep. Wat een subgroep groepeert, verschilt per rubriek. In een gemeenschappelijke rubriek, zoals `gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen`, spiegelt de id van een subgroep een stelselgroep-naam (bijvoorbeeld `sanitair`, `verkoeling_en_verwarming` of `oppervlakte_van_vertrekken`), omdat daar de logica van een hele stelselgroep genest wordt hergebruikt; onder zo'n subgroep kan vervolgens nóg een subgroep hangen. In een gewone rubriek is een subgroep juist een inhoudelijk onderdeel van die ene stelselgroep, zoals `verwarmde_vertrekken` of `verkoelde_vertrekken` binnen Verkoeling en verwarming.

Meestal draagt een subgroep zelf geen punten: die staan op de onderliggende detailregels. Op een enkele plek is dat anders. Bij de oppervlakterubrieken (`oppervlakte_van_vertrekken` en `oppervlakte_van_overige_ruimten`) worden de punten berekend over het op hele vierkante meters afgeronde groepstotaal, en daarom op de subgroep zelf gezet. De onderliggende ruimteregels dragen dan alleen het aantal vierkante meters en geen punten.

### Voorbeeld van de opbouw

De onderstaande bomen tonen een gemeenschappelijke rubriek voor een zelfstandige en een onzelfstandige eenheid. Links staat telkens een herkenbare voorbeeldnaam, rechts de rol die de regel in de structuur speelt.

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

### Criterium-id's

Elke waardering heeft een criterium met een eigen id, en dat id is een pad-id: het wordt afgeleid uit de plek in de hiërarchie, waarbij de builders `criterium.id` en `bovenliggendeCriterium` synchroon houden. Een waardering direct onder de stelselgroep-groep krijgt het id `{stelselgroep}__{segment}`; een waardering onder een andere waardering krijgt `{bovenliggende_id}__{segment}`. De segmenten worden steeds met een dubbele underscore (`__`) aan elkaar geplakt. Het id draagt de identiteit en de plek in de hiërarchie, terwijl de punten en het aantal bij de waardering horen en niet bij het criterium.

Voor de gedeeld-met-lagen gelden vaste segmentnamen: `prive` bij een aantal van ten hoogste 1, en `gedeeld_met_{n}_{soort}` bij een aantal groter dan 1 (met enkele underscores rond het aantal en de soort).

Een paar voorbeelden:

- `buitenruimten__prive__Space_108014713`
- `buitenruimten__gedeeld_met_2_adressen__Space_108006357`
- `buitenruimten__prive`
- `gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_adressen`
- `gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_adressen__keuken`
- `verkoeling_en_verwarming__verwarmde_vertrekken`

Zo'n stelselgroep-groep bouw je stapsgewijs op: je begint met `WaarderingsgroepBuilder(stelsel, stelselgroep)`, hangt inhoudelijke waarderingen aan met `met_onderliggend(...)`, structurele tussenlagen met `met_subgroep(...)` en gedeeld-met-lagen met `gedeeld_met(...)`, en sluit af met `build()`. Die laatste telt de punten op, rondt het rubriektotaal af op kwart en voegt bij punt-dragende groepen eventueel een **Afronding op kwartpunten**-sluitpost toe (zie `CONTEXT.md`), en levert een `WoningwaarderingResultatenWoningwaarderingGroep`.
