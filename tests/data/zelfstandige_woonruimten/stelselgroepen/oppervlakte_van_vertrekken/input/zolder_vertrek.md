In deze file zitten vijf zolderruimten, waarvan er twee meetellen voor de punten van oppervlakte van vertrekken.

De VERA-detailsoort bepaalt of een zolderruimte een vertrek kan zijn. Alleen een `zoldervertrek` voldoet volgens VERA aan de afwerkingseisen en daarmee aan de eis uit 2.2.1.3 dat het dak beschoten is; een `zolder` "voldoet niet aan de afwerkingseisen" en wordt dus nooit als vertrek gewaardeerd. De detailsoort gaat daarnaast uit van een vaste trap; alleen een expliciet gemodelleerde vlizotrap weerspreekt dat.

- `Space_1`: zoldervertrek met een `trap` als bouwkundig element, 10 m² → vertrek.
- `Space_2`: zoldervertrek zonder trapelement, 10 m² → vertrek, want de detailsoort draagt de vaste trap. `Space_1` en `Space_2` staan naast elkaar om te laten zien dat het element niets toevoegt.
- `Space_3`: zoldervertrek met vlizotrap, 10 m² → geen vaste trap, dus geen vertrek; valt terug op overige ruimte.
- `Space_4`: zolder, aangeleverd als vertrek, 10 m² → nooit een vertrek, want een `zolder` voldoet niet aan de afwerkingseisen.
- `Space_5`: zolder als overige ruimte, 1 m² → te klein voor waardering.

Handmatige berekening: 10,00 + 10,00 = 20 m² × 1 punt = 20 punten.
