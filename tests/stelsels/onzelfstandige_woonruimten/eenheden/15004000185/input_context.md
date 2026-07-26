# 15004000185

## Opmerkingen

Stelsel-ketentest voor het volledige woningwaarderingsstelsel onzelfstandige woonruimten (ONZ). De testcase modelleert een onzelfstandige eenheid in een meergezinswoning in Rotterdam (bouwjaar 1998) met een mix van privé- en gedeelde ruimten.

De eenheid heeft één privé slaapkamer (verwarmd) en deelt keuken, hal, toilet en badruimte met één andere onzelfstandige woonruimte (`gedeeldMetAantalOnzelfstandigeWoonruimten`: 2). Er is geen energieprestatie opgevoerd; de energieprestatie wordt daarom bepaald op basis van het bouwjaar. WOZ-waarden zijn beschikbaar tot en met peildatum 2024-01-01.

Verwacht wordt **54 punten** totaal.

- Keuken en badruimte zijn als vertrek ingeschoten (detailsoort keuken/badruimte); het toilet is overige ruimte maar te klein voor waardering.
- De hal is een verkeersruimte en levert geen punten op in rubriek 1 of 2.
- Gedeelde voorzieningen (keuken, sanitair, verwarming) worden gedeeld door het aantal onzelfstandige woonruimten met toegang, niet door het aantal adressen.
- De BAG-gebruiksoppervlakte (58 m²) geldt voor de gehele woning en wordt gebruikt bij de WOZ-berekening.
- Deze testcase wordt ook als voorbeeldbestand gebruikt in meerdere stelselgroep-modules onder `woningwaardering/stelsels/onzelfstandige_woonruimten/`.
