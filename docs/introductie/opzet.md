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

De `CriteriumId` class (in `woningwaardering/stelsels/criterium_id.py`) genereert alle `criterium.id`-waarden in de output. Segmenten worden samengevoegd met dubbele underscores (`__`).

### Vaste segmentvolgorde

```text
{stelselgroep}__[{ruimte_id}?]__[totaal?]__[{criterium_segment}?]__[bucket?]
```

| Segment | Wanneer | Voorbeeld |
|---------|---------|-----------|
| `stelselgroep` | Altijd; gelijk aan de uitvoerende stelselgroep in `criteriumGroep` | `keuken` |
| `ruimte_id` | Bladregel per ruimte | `Space_108014713` |
| `totaal` | Alleen aggregaat-/subtotaalregels in de output | … |
| `criterium_segment` | Subgroep of criteriumdeel (niet de ruimte zelf) | `verwarmde_vertrekken`, `label` |
| `bucket` | Deel-dimensie (privé / gedeeld) | `prive`, `gedeeld_met__4__adressen` |

**Regels:**

- Bladregels (ruimte, factor, label, correcties) bevatten **geen** `totaal`.
- Het stelsel (`ZEL`/`ONZ`) staat niet in `criterium.id`; dat staat in `criteriumGroep.stelsel`.
- Zelfde VERA-input levert dezelfde id's op (contract voor tests en diffs).
- `criterium.naam` op **bladregels** bevat geen `(gedeeld met …)`; de deel-dimensie staat in `criterium.id` (bucket) en/of in het label van een **totaal**-regel (`Totaal (gedeeld met N …)`).
- `groep.punten` is de som van regels zonder `bovenliggendeCriterium` (roots), na kwart-afronding per stelselgroep waar van toepassing.
- Bij subtotalen: `criterium_segment` = **subgroep** (`totaal_subgroep`, bv. `verwarmde_vertrekken`).
- Bij bladregels zonder `ruimte_id`: `criterium_segment` = **criteriumdeel** (`blad_criterium`, bv. `label`, WOZ-onderdeel).

**Voorbeelden:**

- `buitenruimten__Space_108014713` — blad
- `buitenruimten__totaal__prive` — totaal privé (onzelfstandig); zelfstandig: `buitenruimten__totaal`
- `verkoeling_en_verwarming__totaal__verwarmde_vertrekken__prive` — subgroep-totaal (onz.); zelfstandig zonder `__prive`
- `gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__totaal__gedeeld_met__4__adressen`
- `gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__totaal__gedeeld_met__4__adressen` — adressen-bucket (ZEL gemeenschappelijk)
- `gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__totaal__verwarmde_vertrekken__gedeeld_met__4__adressen` — verkoeling-subgroep (ZEL gemeenschappelijk)
- `energieprestatie__label` — eenheidsniveau zonder `totaal`

Bij gedeelde voorzieningen: `prive` als het aantal ≤ 1 is **en** het stelsel onzelfstandig is (of `stelsel` niet op `CriteriumId` is gezet); bij zelfstandig weglaten zolang er geen `gedeeld_met__N__…` nodig is. Anders `gedeeld_met__{N}__{adressen|onzelfstandige_woonruimten}`.

Factory-methodes op `CriteriumId`: `blad_ruimte`, `blad_criterium`, `totaal_deel`, `totaal_subgroep`.

### Groepering via `bovenliggendeCriterium`

Voor subtotalen en subgroepen verwijst een bladregel via JSON-veld `bovenliggendeCriterium` naar het `id` van de aggregaatregel. De hiërarchie kan meerdere niveaus hebben (bijv. blad → subgroep-totaal → onz-bucket-totaal bij onzelfstandige verkoeling, of blad → adressen-totaal → onz-totaal bij 2D-deel).

**Invarianten** (gecontroleerd in tests via `validate_criterium_ids_in_groep`):

- Elk `id` is uniek binnen één stelselgroep-output.
- Geen cycli in `bovenliggendeCriterium`.
- Elke parent-`id` komt voor als output-regel in dezelfde stelselgroep.

Het begrip _criteriumsleutel_ in de domeintaal verwijst naar deze logische groepering; in VERA-json heet het veld `bovenliggendeCriterium`.
