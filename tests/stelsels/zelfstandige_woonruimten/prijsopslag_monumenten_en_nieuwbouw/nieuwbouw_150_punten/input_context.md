# nieuwbouw_150_punten

## Doel

Test dat een nieuwbouwwoning die in de middensector valt (volledige eenheid met bouw- en exploitatiedatum) recht heeft op een nieuwbouwopslag van **10%** op de maximale huurprijs.

## Beleidsbron

- Implementatietoelichting: [§2.13.6 Nieuwbouw](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#2137-nieuwbouw)
- Beleidsboek (quote): "+ 10% op de maximale huurprijs bij nieuwbouwwoning in de middensector"

## Handmatige berekening

| Criterium                                                    | Opslag     |
| ------------------------------------------------------------ | ---------- |
| Nieuwbouw (`beginBouwdatum` 2023, `inExploitatiedatum` 2024) | 10% (0,10) |

## Opmerkingen

- De testcase gebruikt een volledige eenheid (inclusief WOZ, energieprestatie en ruimten) om de middensectorpositie te bepalen; alleen de opslag wordt in deze stelselgroep getoetst.
