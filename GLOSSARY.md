# Woningwaardering

Een open-source Python-package die woonruimten waardeert volgens het woningwaarderingsstelsel (WWS), op basis van de beleidsregels van de Huurcommissie en de VERA-standaard. Bronnen, autoriteitsvolgorde en projectgrenzen staan in [docs/voor-ontwikkelaars/bronnen.md](docs/voor-ontwikkelaars/bronnen.md).

## Waarderen

**Woningwaardering**:
De berekening van punten voor een woonruimte volgens het WWS.

**WWS**:
Het woningwaarderingsstelsel: het puntensysteem waarmee de kwaliteit van woonruimte wordt gewaardeerd.

**Woonruimte**:
De woning of wooneenheid die gewaardeerd wordt, zelfstandig of onzelfstandig.

**Eenheid**:
De digitale representatie van een woonruimte in het VERA BVG-model, waarop de waardering gebaseerd wordt.

**Stelsel**:
Het waarderingsregime voor zelfstandige of onzelfstandige woonruimten; bepaalt welke stelselgroepen gelden.

**Stelselgroep**:
Een onderdeel van het WWS waarop afzonderlijk punten worden berekend, zoals energieprestatie of sanitair.

**Peildatum**:
De datum waarop de waardering wordt bepaald en waartegen geldigheid van regels en energielabel wordt getoetst.

**Toe te rekenen aantal**:
Het aandeel van een hoeveelheid dat aan de huurder is toe te rekenen: het aantal gedeeld door het aantal woonruimten of adressen waarmee gedeeld wordt (1 bij privé).
_Vermijd_: toegerekend aantal

**Maximering**:
Een waardering die een maximum oplegt aan de punten van één of meer andere waarderingen.

## Output-structuur

**Waardering**:
Eén regel in de uitkomst van een stelselgroep; draagt `punten` en `aantal` en verwijst naar een criterium.

**Criterium**:
De identiteit, naam en plek in de hiërarchie van een waardering; heeft zelf nooit punten.

**Criterium-id**:
Een pad-id die de plek van een criterium in de hiërarchie beschrijft.

**Subgroep**:
Een groeperend criterium binnen een stelselgroep; geen stelselgroep, ook als het dezelfde naam draagt als een stelselgroep.

**Bovenliggende / onderliggende**:
De relatie tussen waarderingen via `bovenliggendeCriterium`; een waardering zonder bovenliggende staat _direct onder de stelselgroep_, waarderingen met dezelfde bovenliggende staan _op hetzelfde niveau_.
_Vermijd_: ouder, kind, parent, child, sibling, knoop, node, leaf, wortel, root, boom, tree

**Rij**:
Eén waardering zoals weergegeven in het tekstrapport.

## Bronnen

**Beleidsboek**:
De door de Huurcommissie gepubliceerde uitleg van de wettekst van het WWS; bedoeld wordt de actuele online HTML-versie.
_Vermijd_: PDF-beleidsboek (als bron van waarheid)

**Wettekst**:
Het Besluit huurprijzen woonruimte, de hoogste bron van autoriteit voor puntberekeningen.

**Huurprijscheck**:
De rekentool van de Huurcommissie voor de maximale huurprijs; bron van autoriteit wanneer wettekst en beleidsboek niet sluitend zijn.

**Implementatietoelichting**:
Onze markdown-kopie van het beleidsboek per stelselgroep, met doorhalingen en interpretaties van hoe regels in code zijn vertaald.

## VERA

**VERA**:
De sectorstandaard van Aedes voor gegevensuitwisseling in de corporatiesector, gebruikt voor input, output en referentiedata.

**BVG**:
Het VERA-domein voor vastgoed- en eenheidsgegevens.

**Referentiedata**:
Door VERA gepubliceerde enumeraties en codetabellen, zoals `Woningwaarderingstelsel` en `Woningwaarderingstelselgroep`.

**Modeluitbreiding**:
Een lokale uitbreiding op de VERA-modellen voor informatie die de standaard niet bevat maar het WWS wel nodig heeft.

**Lookuptabel**:
Tabulaire regeldata of constanten die nodig zijn voor puntberekeningen.

## Waarschuwingen

**UserWarning**:
Een waarschuwing voor incomplete of onjuiste inputdata.

**DeprecationWarning**:
Een waarschuwing voor verouderde input die nog wel wordt geaccepteerd.
