# zolder_zonder_vaste_trap

## Doel

Gedeelde berging en grote gedeelde zolder (vlizotrap), gedeeld met 2 adressen. Oppervlaktepunten worden berekend op hele m² over het totaal van alle overige ruimten in dezelfde oppervlaktegroep. De zoldercorrectie bedraagt maximaal 5 punten bruto, maar niet meer dan de punten die de zolder zelf aan dat totaal toevoegt. In dit voorbeeld is de zolderbijdrage groter dan 5 punten bruto; de correctie blijft op 5 punten. De zolder draagt na de correctie nog punten bij naast de berging.

Verwacht totaal: **5,75 punten**.

## Beleidsbron

- Implementatietoelichting: [§2.2.2.3 Zolderruimte zonder vaste trap](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#2223-zolderruimte-zonder-vaste-trap)
- Beleidsboek (quote):
  "Als een zolderruimte niet voldoet aan de vereisten voor waardering als een 'vertrek', maar wel als overige ruimte kan worden aangemerkt en er is geen vaste trap naar de zolder, dan worden er 5 punten afgetrokken van de waarde die aan het vloeroppervlak wordt toegekend."
  (...)
  "Maar: er kunnen nooit meer punten afgetrokken worden dan het totaal aantal punten dat de zolderruimte zelf waard is."

## Handmatige berekening

| Component                              | Berekening                     | Punten   |
| -------------------------------------- | ------------------------------ | -------- |
| Subtotaal oppervlakte (6 + 16 m², / 2) | (0,75 × 22) / 2                | 8,25     |
| Correctie zolder zonder vaste trap     | min(5, zolderpunten bruto) / 2 | −2,5     |
| **Totaal**                             |                                | **5,75** |

## Opmerkingen

- De zolder heeft een vlizotrap (`Bouwkundigelementdetailsoort.vlizotrap`), geen vaste trap.
- Correctie wordt berekend op bruto punten en daarna gedeeld door het aantal adressen.
