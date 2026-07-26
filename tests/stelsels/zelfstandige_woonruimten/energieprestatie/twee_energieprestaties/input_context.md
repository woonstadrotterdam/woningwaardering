# twee_energieprestaties

## Doel

Test dat bij meerdere energieprestaties de geldige prestatie wordt gekozen: een vereenvoudigd label F (2019–2021, ongeldig) wordt genegeerd ten gunste van het latere NTA8800-label A.

De input bevat twee energieprestaties: label F (verlopen periode) en label A (geldig vanaf 2021). Verwacht: **37 punten** voor label A (meergezinswoning).

## Beleidsbron

- Implementatietoelichting: [§2.4.3 Energieprestaties die niet geldig zijn](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#243-energieprestaties-die-_niet_-geldig-zijn-voor-de-woningwaardering), [§2.4.4 Punten voor geldige energieprestaties](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#244-punten-voor-geldige-energieprestaties)
- Beleidsboek (quote): "Een energielabel dat is afgegeven in de periode van 1 januari 2015 tot 1 januari 2021 krijgt geen punten in het woningwaarderingsstelsel."

## Handmatige berekening

| Energieprestatie          | Geldig?                   | Punten MGW |
| ------------------------- | ------------------------- | ---------- |
| Label F (NTA, 2019–2021)  | Nee (vereenvoudigd label) | —          |
| Label A (NTA, vanaf 2021) | Ja                        | 37         |
| **Totaal**                |                           | **37**     |
