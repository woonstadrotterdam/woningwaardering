# 15004000185

## Doel

Stelsel-ketentest voor het volledige woningwaarderingsstelsel onzelfstandige woonruimten (ONZ). De testcase modelleert een onzelfstandige kamer in een meergezinswoning in Rotterdam (bouwjaar 1998) met een mix van privé- en gedeelde ruimten.

De eenheid heeft één privé slaapkamer (verwarmd) en deelt keuken, hal, toilet en badruimte met één andere onzelfstandige woonruimte (`gedeeldMetAantalOnzelfstandigeWoonruimten`: 2). Er is geen energieprestatie opgevoerd; de energieprestatie wordt daarom bepaald op basis van het bouwjaar. WOZ-waarden zijn beschikbaar tot en met peildatum 2024-01-01.

Verwacht wordt **54 punten** totaal en een maximale huur van **€ 550,19**.

## Beleidsbron

- Implementatietoelichting: [Hoofdstuk 2 – Het woningwaarderingsstelsel voor een onzelfstandige woning](../../../../../docs/implementatietoelichtingen/onzelfstandige-woonruimten.md#hoofdstuk-2-het-woningwaarderingsstelsel-voor-een-onzelfstandige-woning)
- Beleidsboek (quote): "1 punt per m² per privévertrek" en "1 punt per m² per gemeenschappelijke ruimte / onzelfstandige woonruimten met toegang en gebruiksrecht" — zie [§2.2.1 Vertrekken](../../../../../docs/implementatietoelichtingen/onzelfstandige-woonruimten.md#221-vertrekken)

## Handmatige berekening

| Rubriek                                                                                                | Berekening                                                                                    |   Punten |
| ------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------- | -------: |
| Oppervlakte vertrekken                                                                                 | Privé slaapkamer 20,04 m² + (gedeelde keuken 7,50 + badruimte 1,70) / 2 = 24,64 m² → afgerond |     25,0 |
| Oppervlakte overige ruimten                                                                            | Hal is verkeersruimte; toilet (1,0 m²) onder minimum 2,0 m²                                   |      0,0 |
| Verwarming                                                                                             | 2 punten per verwarmd privévertrek (slaapkamer)                                               |      2,0 |
| Energieprestatie                                                                                       | Geen energielabel; bouwjaar 1998 × 24,5 m² vertrekken (0,35 p/m²)                             |      8,5 |
| Keuken                                                                                                 | Aanrecht 2.220 mm (tabel: 7 punten) / 2 gedeelde woonruimten                                  |      3,5 |
| Sanitair                                                                                               | Staand toilet 3 / 2 + douche 3 / 2                                                            |      3,0 |
| WOZ-waarde                                                                                             | € 205.000 / 58 m² = € 3.534/m² vs. gemiddelde Groot-Rijnmond € 3.537 (−0,07%) → binnen ±10%   |     12,0 |
| Buitenruimten, gemeenschappelijke ruimten, parkeer, bijzondere voorzieningen, aftrek, monumentenopslag | Niet van toepassing                                                                           |      0,0 |
| **Totaal**                                                                                             |                                                                                               | **54,0** |

Relevante implementatietoelichtingen per rubriek:

- [§2.2 Rubriek 1 en 2: vertrekken en overige ruimten](../../../../../docs/implementatietoelichtingen/onzelfstandige-woonruimten.md#22-rubriek-1-en-2-vertrekken-en-overige-ruimten)
- [§2.3 Rubriek 3: Verwarming en verkoeling](../../../../../docs/implementatietoelichtingen/onzelfstandige-woonruimten.md#23-rubriek-3-verwarming-en-verkoeling)
- [§2.4 Rubriek 4: Energieprestatie](../../../../../docs/implementatietoelichtingen/onzelfstandige-woonruimten.md#24-rubriek-4-energieprestatie)
- [§2.5 Rubriek 5: Keuken](../../../../../docs/implementatietoelichtingen/onzelfstandige-woonruimten.md#25-rubriek-5-keuken)
- [§2.6 Rubriek 6: Sanitair](../../../../../docs/implementatietoelichtingen/onzelfstandige-woonruimten.md#26-rubriek-6-sanitair)
- [§2.11 Rubriek 11: Punten voor de WOZ-waarde](../../../../../docs/implementatietoelichtingen/onzelfstandige-woonruimten.md#211-rubriek-11-punten-voor-de-woz-waarde)

## Opmerkingen

- Keuken en badruimte zijn als vertrek ingeschoten (detailsoort keuken/badruimte); het toilet is overige ruimte maar te klein voor waardering.
- De hal is een verkeersruimte en levert geen punten op in rubriek 1 of 2.
- Gedeelde voorzieningen (keuken, sanitair, verwarming) worden gedeeld door het aantal onzelfstandige woonruimten met toegang, niet door het aantal adressen.
- De BAG-gebruiksoppervlakte (58 m²) geldt voor de gehele woning en wordt gebruikt bij de WOZ-berekening.
- Deze testcase wordt ook als voorbeeldbestand gebruikt in meerdere stelselgroep-modules onder `woningwaardering/stelsels/onzelfstandige_woonruimten/`.
