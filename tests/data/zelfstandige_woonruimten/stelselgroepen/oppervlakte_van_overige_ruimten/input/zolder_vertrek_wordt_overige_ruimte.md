Deze eenheid bevat drie zolderruimten die alle drie als `ruimtesoort` `vertrek` zijn aangeleverd, maar geen van drieën aan de eisen van een vertrek voldoet. Het voorbeeld test of een zolderruimte die als vertrek is aangeleverd terugvalt op de eisen van een overige ruimte, net zoals dat bij andere vertrekken gebeurt die de minimale oppervlakte van 4 m² niet halen. Elke ruimte faalt op een andere eis.

- `Space_1`: een zoldervertrek dat met 3 m² te klein is voor een vertrek (2.2.1.2). Telt mee als overige ruimte, zonder correctie.
- `Space_2`: een zoldervertrek van 10 m² dat alleen via een vlizotrap bereikbaar is en daarmee geen vaste trap heeft (2.2.1.3). Telt mee als overige ruimte, met een correctie van maximaal 5 punten.
- `Space_3`: een `zolder` van 10 m². Een `zolder` voldoet volgens VERA niet aan de afwerkingseisen en daarmee niet aan de eis dat het dak beschoten is (2.2.1.3). Telt mee als overige ruimte, zonder correctie.

Handmatige berekening: 3,00 + 10,00 + 10,00 = 23,00 m², afgerond 23 m² × 0,75 = 17,25 punten. De correctie voor `Space_2` is min(5, (23 − 13) × 0,75) = 5 punten aftrek. Totaal: 17,25 − 5,00 = 12,25 punten.
