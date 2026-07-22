# Opzet woningwaardering package

## Implementatie beleidsboek huurcommissie

Voor het berekenen van een woningwaardering worden de [beleidsboeken van de Nederlandse Huurcommissie](https://www.huurcommissie.nl/huurcommissie-helpt/beleidsboeken) voor de waarderingstelsels voor zelfstandige en onzelfstandige woningen gevolgd.
De beleidsboeken van de Huurcommissie Nederland volgen Nederlandse wet- en regelgeving zoals beschreven in het [Besluit huurprijzen woonruimte](https://wetten.overheid.nl/BWBR0003237/2026-01-01).

Om berekeningen te maken met betrekking tot een woningwaardering wordt het gepubliceerde beleid vertaald naar Python-code.
Een woningwaardering wordt gemaakt op basis van woningelementen.
De stelselgroepen waarop gescoord wordt, zijn vastgelegd in het [woningwaarderingstelselgroep](https://www.coraveraonline.nl/index.php/Referentiedata:WONINGWAARDERINGSTELSELGROEP) op www.coraveraonline.nl.
Deze worden aangehouden in de opzet van de `woningwaardering`-package.
Voor elke stelselgroep wordt een apart Python-object gemaakt met een naam die overeenkomt met [woningwaarderingstelselgroep](https://www.coraveraonline.nl/index.php/Referentiedata:WONINGWAARDERINGSTELSELGROEP).

De woningwaardering package volgt de [beleidsboeken van de Nederlandse Huurcommissie](https://www.huurcommissie.nl/huurcommissie-helpt/beleidsboeken) en daarmee de Nederlandse wet en regelgeving m.b.t. het waarderen van woningen. Tijdens de ontwikkeling van deze package komt het voor dat we inconsistenties in de beleidsboeken vinden of dat er ruimte is voor interpretatie. Daarnaast kan het voorkomen dat de VERA modellen, met eventuele uitbreidingen, niet toereikend zijn om de stelselgroep volgens het beleidsboek tot op de letter nauwkeurig te implementeren. In de [implementatietoelichtingen](../implementatietoelichtingen/index.md) onderbouwen wij hoe elke stelselgroep is geïmplementeerd en welke keuzes daarin gemaakt zijn.  

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

## Criterium ID's

Criterium-id's worden afgeleid uit de **bovenliggende** in de hiërarchie. De builders in `woningwaardering/stelsels/builders.py` (`WaarderingsgroepBuilder` en `WaarderingBuilder`) zetten `criterium.id` en `bovenliggendeCriterium` synchroon.

- Onder de stelselgroep-groep: `{stelselgroep}__{segment}`
- Onder een bestaande waardering: `{bovenliggende_id}__{segment}`

Segmenten worden met dubbele underscores (`__`) aan elkaar gekoppeld. Een **criterium** draagt identiteit en hiërarchie; **punten** en **aantal** zitten op de waardering.

Gedeeld-met lagen:

- `prive` bij aantal ≤ 1
- `gedeeld_met_{n}_{soort}` bij aantal > 1 (enkele underscores rond het aantal en de soort)

Voorbeelden:

- `buitenruimten__prive__Space_108014713` (ruimteregel, privé)
- `buitenruimten__gedeeld_met_2_adressen__Space_108006357` (ruimteregel, gedeeld)
- `buitenruimten__prive` (gedeeld-met aggregaat)
- `gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_adressen` (gedeeld-met aggregaat)
- `gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_adressen__keuken` (categorie onder gedeeld-met aggregaat)
- `verkoeling_en_verwarming__verwarmde_vertrekken` (criteriumsleutel)

`WaarderingsgroepBuilder` bouwt een stelselgroep-groep op: start met `WaarderingsgroepBuilder(stelsel, stelselgroep)`, hang onderliggende waarderingen aan met `maak_onderliggende(...)`, dedupliceer gedeeld-met-criteria met `gedeeld_met(...)`, en sluit af met `bouw()` (sommeert de punten en levert een kale `WoningwaarderingResultatenWoningwaarderingGroep`). De `waarderingsgroep_builder` die stelselgroepen aan gedeelde helpers doorgeven is daarmee een `WaarderingsgroepBuilder` of `WaarderingBuilder`; de helpers hangen hun resultaten daar direct onder.

Detailregels zonder `ruimte_id` mogen geen criteriumnaam gebruiken die al als criteriumsleutel bestaat.

Met deze ID's kan gerefereerd worden aan specifieke criteria in de output van de woningwaardering.

### Criteriumsleutels

Een criteriumsleutel is een id volgens de **criteriumnaam-regel** (`{stelselgroep}__{criteriumnaam}`):

```text
verkoeling_en_verwarming__verwarmde_vertrekken
└──── stelselgroep ────┘  └── criteriumnaam ─┘
```

Detailregels (ruimteregels) verwijzen naar die sleutel via `bovenliggendeCriterium`: een VERA-object met daarin de `id` van de subgroep. Vervolgens wordt per unieke sleutel een aparte aggregaatregel aangemaakt met diezelfde `id` en een leesbare naam (bijv. _Verwarmde vertrekken_). Die aggregaatregel heeft geen eigen punten; de punten staan op de onderliggende detailregels.

```text
Verkoeling en verwarming
└── Verwarmde vertrekken                         ← criteriumsleutel (aggregaatregel)
    ├── Slaapkamer 1                             ← detailregel (punten)
    └── Woonkamer                                ← detailregel (punten)
```

Zie [aan de slag](../aan-de-slag/index.md) voor een volledig voorbeeld in JSON-output en output-tabel.

**Beperkingen en afspraken**

- Subgroepen zijn op hetzelfde niveau, niet genest. We ondersteunen geen geneste criteriumnaam-subgroepen (`criteriumsleutel → criteriumsleutel`).
- Detailregels zonder `ruimte_id` mogen geen criteriumnaam gebruiken die al als criteriumsleutel bestaat (zie hierboven).
- Een aggregaatregel met een criteriumsleutel-id mag wél een `bovenliggendeCriterium` hebben als dat een **gedeeld-met aggregaat** is (andere id-familie). Dat komt voor bij onzelfstandige woningen:

```text
verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten
└──── stelselgroep ────┘└ gedeeld_met 2 onzelfstandige woonruimten ┘
```
