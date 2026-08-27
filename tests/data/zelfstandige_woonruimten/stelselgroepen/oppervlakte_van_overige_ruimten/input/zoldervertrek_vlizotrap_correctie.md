Deze eenheid bevat één ruimte met `Ruimtedetailsoort` `zoldervertrek` van 10 m², aangeleverd als `ruimtesoort` `vertrek` en alleen bereikbaar via een vlizotrap.

Het voorbeeld test twee dingen tegelijk. Ten eerste de terugval: de ruimte haalt de vertrek-eisen niet omdat er geen vaste trap is, en wordt daarom als overige ruimte gewaardeerd. Ten tweede dat de aftrek van 2.2.2.3 ook geldt voor `zoldervertrek`: een zoldervertrek is net als een `zolder` een zolderruimte, dus het ontbreken van een vaste trap kost punten.

Handmatige berekening: 10,00 m², afgerond 10 m² × 0,75 = 7,50 punten. De correctie is min(5, (10 − 0) × 0,75) = 5 punten aftrek. Totaal: 7,50 − 5,00 = 2,50 punten.
