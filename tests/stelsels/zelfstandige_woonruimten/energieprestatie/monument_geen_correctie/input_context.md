# monument_geen_correctie

## Doel

Test dat de monumentcorrectie niet van toepassing is wanneer de energieprestatie via een EPV wordt gewaardeerd (vast puntenaantal), ook al is de eenheid een rijksmonument.

De input bevat een rijksmonument als eengezinswoning met geldige energie-index (label C) en prijscomponent EPV. Verwacht: **32 punten** (EPV eengezinswoning), zonder monumentcorrectie.

## Beleidsbron

- Implementatietoelichting: [§2.4.6.3 Energieprestatievergoeding](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#2463-energieprestatievergoeding)
- Beleidsboek (quote): "Bij een EPV wordt voor een eengezinswoning 32 punten toegekend voor de energieprestatie en bij een meergezinswoning 28 punten."

## Handmatige berekening

| Situatie                            | Punten |
| ----------------------------------- | ------ |
| EPV eengezinswoning (rijksmonument) | 32     |

## Opmerkingen

- De monumentcorrectie uit [§2.4.6.1](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#2461-energieprestatie-van-monumenten) geldt voor negatieve label-/bouwjaarpunten (E, F, G); bij EPV is die route niet actief.
