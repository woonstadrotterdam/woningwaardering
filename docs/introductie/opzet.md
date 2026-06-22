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

Alle waarschuwingen die worden gegenereerd met `warnings.warn()`, worden standaard gelogd met `logger.warning()` en weergegeven in het standaardfout bestand.
Mocht door de gebruiker logging worden uitgezet, dan zullen de UserWarnings altijd te zien zijn voor de gebruiker in de output van de _stderr_.

### Warning vs Exception

Er wordt doorgaans in de stelselgroepversies gebruik gemaakt van `warnings.warn()` in plaats van het raisen van een exception.
Hierdoor bestaat de mogelijkheid om stelselgroepen te berekenen voor stelselgroepen waarvoor de data wel compleet genoeg is, mits de `warnings.simplefilter` naar `default` is gezet.

## Criterium ID's

De `CriteriumId`-class bouwt criteriumids als een **pad** van bovenliggendcriteriumids. Elk output-element is een criterium met een criteriumid; `punten` en `aantal` zijn optioneel.

### Padregel

```text
onderliggendcriteriumid == bovenliggendcriteriumid + "__" + criteriumid_toevoeging
```

- `__` scheidt **criteria** in het pad.
- `_` komt **binnen** één `criteriumid_toevoeging` voor (bijv. `gedeeld_met_4_adressen`).

### Terminologie

| Term | Betekenis |
|---|---|
| **stelselgroepcriterium** | Bovenste laag van het pad: alleen de stelselgroepnaam (bijv. `keuken`) |
| **gedeeld_met_criterium** | Onder stelselgroepcriterium: `prive` of `gedeeld_met_{n}_{soort}` |
| **geneste stelselgroep** | Stelselgroepcriterium (keuken, sanitair, …) onder een gedeeld-met-criterium in GEM/GBA-output |
| **groeperingscriterium** | Optioneel niveau onder geneste stelselgroep (bijv. `verwarmde_vertrekken`) |
| **ruimtecriterium** | Criterium per ruimte (bijv. `Space_108014713`) |
| **detailcriterium** | Installatie- of detailregel onder ruimte of groepering |
| **bovenliggendcriteriumid** | Id van het directe bovenliggende criterium (`bovenliggendeCriterium.id`) |
| **onderliggendcriteriumid** | Id van een criterium onder een bovenliggendcriterium |
| **criteriumid_toevoeging** | Segment dat aan het bovenliggendcriteriumid wordt geplakt |

Zie [CONTEXT.md](../../CONTEXT.md) voor definities en vermijden/gebruiken-tabel.

### Hiërarchie (GEM/GBA)

```text
stelselgroepcriterium
  └─ gedeeld_met_criterium
       └─ geneste stelselgroep
            ├─ groeperingscriterium (optioneel)
            │    └─ detailcriterium
            └─ ruimtecriterium
                 └─ detailcriterium
```

Lege geneste stelselgroepen worden overgeslagen in de output.

### Gedeeld-met

Gedeeld-met-criteria gebruiken één `criteriumid_toevoeging`:

- `prive` (aantal ≤ 1)
- `gedeeld_met_{n}_{soort}` (bijv. `gedeeld_met_4_adressen`, `gedeeld_met_8_onzelfstandige_woonruimten`)

### Voorbeelden

```text
# stelselgroepcriterium
keuken

# groeperingscriterium (bovenliggend, geen punten)
verkoeling_en_verwarming__verwarmde_vertrekken

# onderliggend ruimtecriterium (genest onder groepering)
verkoeling_en_verwarming__verwarmde_vertrekken__Space_108014713

# gedeeld-met-criterium (gedeeld met N adressen)
sanitair__gedeeld_met_8_onzelfstandige_woonruimten

# geneste stelselgroep onder gedeeld-met-criterium
gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_adressen__keuken

# ruimtecriterium onder gedeeld-met-criterium
buitenruimten__gedeeld_met_3_adressen__Space_108014713

# genest onder een berekeningsonderdeel (WOZ)
punten_voor_de_woz_waarde__onderdeel_II__factor_II
```

Geneste bovenliggendcriteria zijn toegestaan. Detailregels verwijzen via `bovenliggendeCriterium` naar het directe bovenliggende criterium. Top-level criteria binnen een groep (direct onder het stelselgroepcriterium) hebben geen `bovenliggendeCriterium`; de root staat alleen in `criteriumGroep`.

`met_criterium()` en `met_waardering()` vullen `naam` standaard uit `WEERGAVENAMEN` via het laatste padsegment (`CriteriumId.weergavenaam`). Geef `naam=` alleen bij dynamische of afwijkende teksten (ruimtenaam, datum, beleidssuffix).

Zie [aan de slag](../aan-de-slag/index.md) voor een volledig voorbeeld in JSON-output en output-tabel.
