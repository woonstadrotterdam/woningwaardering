# 2_laadpalen

## Doel

Test dat twee laadpalen in een privégarage als aparte bouwkundige elementen (`Bouwkundigelementdetailsoort.laadpaal`) worden geteld en gewaardeerd onder rubriek 12 (bijzondere voorzieningen).

De input bevat één garage met twee `bouwkundigeElementen` van detailsoort laadpaal. Verwacht wordt één waarderingsregel **Laadpalen** met `aantal` 2 en **4 punten** totaal.

## Beleidsbron

- Implementatietoelichting: [§2.12.3 Laadpalen](../../../../../docs/implementatietoelichtingen/onzelfstandige-woonruimten.md#2123-laadpalen)
- Beleidsboek (quote): "Een laadpaal voor elektrisch rijden die exclusief bestemd is voor gebruik door de bewoners, wordt gewaardeerd met 2 punten."

## Handmatige berekening

| Voorziening | Aantal | Punten per stuk | Totaal |
| ----------- | ------ | --------------- | ------ |
| Laadpaal    | 2      | 2 → 4           | 4      |
| **Totaal**  |        | **4**           |        |

## Opmerkingen

- De exclusiviteit voor bewoners is in deze testcase impliciet aangenomen; het VERA-inputmodel bevat geen apart attribuut daarvoor.
- Laadpalen in gemeenschappelijke parkeerruimten vallen onder rubriek 10, niet onder deze regel — zie [§2.12.3](../../../../../docs/implementatietoelichtingen/onzelfstandige-woonruimten.md#2123-laadpalen).
