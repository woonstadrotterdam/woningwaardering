# Pull requests met `/pr`

Waar de skill `/pr` botst met dit bestand, gaat dit bestand voor.

- Volg de PR-template, geef elk feit één plek en schrijf alleen wat een reviewer niet uit de diff haalt.
- **Samenvatting** zegt in één of twee zinnen wat er verandert en waarom. Een visual uit `/pr` alleen als de codewijziging in de diff niet te overzien is.
- Veranderen punten of huurprijs, dan is het voor/na-bewijs uit `/pr` het overzicht uit [Voor En Na](voor-en-na.md) onder de Samenvatting, met per situatie de test die het vastlegt, zodat de reviewer de input in de testreferentie vindt. Alleen daar staan getallen voor en na. Verandert een situatie die geen test heeft, voeg dan een test toe of noem haar als situatie zonder test.
- Veranderen punten of huurprijs, vul dan **Huurprijscheck** in. Heeft `/code-review` de wijziging al doorgerekend, neem dan dat rapport over. Reken anders zelf door volgens de skill `huurprijscheck` (sectie **Bij code-review**).
- Beantwoord de Blast Radius uit `/pr` onder **Impact op eindgebruiker**: vink de soorten aan en noem bij de andere soorten wat er verandert. Zet bij ja het label `impact eindgebruiker`, zodat reviewers zien dat de PR intensieve review vraagt.
- Het oordeel one-way/two-way door uit `/pr` laat je weg: wat na een release niet terug kan, is impact op de eindgebruiker of een breaking change, en die hebben al een label.
- De afweging tussen bronnen staat alleen onder **Bronverwijzing**.
