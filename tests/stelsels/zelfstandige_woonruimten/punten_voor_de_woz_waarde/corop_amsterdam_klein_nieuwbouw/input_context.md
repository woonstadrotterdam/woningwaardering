# corop_amsterdam_klein_nieuwbouw

## Doel

Test de afwijkende WOZ-berekening voor een kleine nieuwbouwwoning (< 40 m²) in COROP-regio Amsterdam (bouwjaar 2020): factor II is € 103 in plaats van € 242, totaal **106,25 punten**.

## Beleidsbron

- Implementatietoelichting: [§2.11.6 Kleine nieuwbouw COROP Utrecht/Amsterdam](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#2116-uitzonderingsregel-waardering-kleine-nieuwbouwwoningen-in-corop-gebied-utrechtamsterdam-opgeleverd-tussen-2018---2022)
- Beleidsboek (quote): "de woning is kleiner dan 40 m² en, de woning ligt in de COROP-gebieden Amsterdam en Utrecht"

## Handmatige berekening

| Onderdeel | Berekening                | Punten     |
| --------- | ------------------------- | ---------- |
| I         | € 310.000 / € 15.329      | 20,22      |
| II        | € 310.000 / 35 m² / € 103 | 86,03…     |
| Totaal    | afgerond op kwart punt    | **106,25** |
