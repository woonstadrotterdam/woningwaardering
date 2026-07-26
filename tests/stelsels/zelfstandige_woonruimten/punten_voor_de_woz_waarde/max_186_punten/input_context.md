# max_186_punten

## Doel

Test de uitzondering op de WOZ-cap: als de woning zonder cap ≥ 187 punten zou halen maar met cap onder 187 zakt, geldt minimaal **186 punten** totaal. WOZ-punten worden beperkt tot 65,75 (correctie −30,00).

## Beleidsbron

- Implementatietoelichting: [§2.11.7 Uitzonderingen op de WOZ-cap](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#2117-de-uitzonderingen-op-de-woz-cap)
- Beleidsboek (quote): "wanneer een woning zonder de 'cap op de WOZ' 187 of meer punten krijgt en door 'de cap op de WOZ' minder dan 187 punten krijgt: dan geldt een minimale waardering van 186 punten voor de woning."

## Handmatige berekening

| Stap                          | Punten |
| ----------------------------- | ------ |
| Berekende WOZ-punten (I + II) | 95,74  |
| Na maximering tot 186 totaal  | 65,75  |
| Correctie                     | −30,00 |
