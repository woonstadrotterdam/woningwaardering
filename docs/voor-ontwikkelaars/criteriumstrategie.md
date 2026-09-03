# Criteriumstrategie

Tijdens een `waardeer()`-aanroep bouw je de uitkomst van een stelselgroep eerst op als een hiërarchie van waarderingen. Daarvoor gebruiken we de builders in `woningwaardering/stelsels/builders.py`. Een `WaarderingsgroepBuilder` verzamelt alle waarderingen binnen één stelselgroep; een `WaarderingBuilder` bouwt één afzonderlijke waardering op. Pas bij `build()` vertalen we die hiërarchie naar VERA-output: een platte lijst waarderingen waarin de samenhang via `bovenliggendeCriterium` is vastgelegd.

Je bouwt die hiërarchie op in drie verschillende soorten lagen:

- `gedeeld_met(...)` voor een deel-laag voor onzelfstandige woonruimten en/of adressen
- `met_subgroep(...)` voor een groeperende tussenlaag
- `met_onderliggend(...)` voor een inhoudelijke waardering met punten en/of aantal

## Structuur van de output

De voorbeelden hieronder tonen een gemeenschappelijke stelselgroep voor een zelfstandige en een onzelfstandige eenheid. Links staat een herkenbare naam, rechts de rol in de structuur.

> In VERA is elke regel in deze structuur een waardering met een criterium.

**Zelfstandig**

```text
Gemeenschappelijke vertrekken, overige ruimten en voorzieningen  ← stelselgroep
└─ Gedeeld met 5 adressen                                         ← gedeeld-met-criterium
   ├─ Oppervlakte van vertrekken                                  ← subgroep met punten
   │  └─ Keuken                                                   ← waardering met aantal (m²); punten op subgroep
   ├─ Verkoeling en verwarming                                    ← subgroep
   │  └─ Verwarmde vertrekken                                     ← subgroep
   │     └─ Keuken                                                ← waardering met punten
   └─ Keuken                                                      ← subgroep
      └─ Keuken                                                   ← subgroep (per ruimte)
         ├─ Lengte aanrecht                                       ← waardering met punten
         └─ Extra voorzieningen                                   ← subgroep
            └─ Inbouw koelkast                                    ← waardering met punten
```

**Onzelfstandig**

```text
Gemeenschappelijke binnenruimten gedeeld met meerdere adressen   ← stelselgroep
└─ Gedeeld met 4 onzelfstandige woonruimten                       ← gedeeld-met-criterium
   └─ Gedeeld met 4 adressen                                      ← gedeeld-met-criterium
      ├─ Oppervlakte van vertrekken                               ← subgroep met punten
      │  └─ Keuken                                                ← waardering met aantal (m²); punten op subgroep
      ├─ Verkoeling en verwarming                                 ← subgroep
      │  └─ Verwarmde vertrekken                                  ← subgroep
      │     └─ Keuken                                             ← waardering met punten
      ├─ Keuken                                                   ← subgroep
      │  └─ Keuken                                                ← subgroep (per ruimte)
      │     ├─ Lengte aanrecht                                    ← waardering met punten
      │     └─ Extra voorzieningen                                ← subgroep
      │        └─ Inbouw koelkast                                 ← waardering met punten
      └─ Sanitair                                                 ← subgroep
         └─ Toilet                                                ← subgroep (per ruimte)
            └─ Wastafel                                           ← waardering met punten
```

De hiërarchie binnen een stelselgroep loopt via `bovenliggendeCriterium`. Punten en aantallen horen bij de waardering; het criterium draagt de identiteit, naam en plek in de hiërarchie. De voorbeelden hierboven laten dus dezelfde drie soorten regels zien: een optionele gedeeld-met-laag, een of meer subgroepen en inhoudelijke waarderingen.

Bij gedeelde ruimten kan deling op twee niveaus voorkomen: eerst, waar van toepassing, deling met onzelfstandige woonruimten en daaronder deling met adressen.

Een subgroep of gedeeld-met-laag verschijnt alleen in de output als er inhoud onder hangt, of als er punten, een aantal of een opslagpercentage aan wordt toegekend. Lege groeperende lagen blijven dus weg; in de builders is dit `lazy` activatie.

Meestal draagt een subgroep zelf geen punten; die staan op de onderliggende waarderingen. Bij de oppervlakte-stelselgroepen (`oppervlakte_van_vertrekken` en `oppervlakte_van_overige_ruimten`) is dat anders: daar staan de punten op de subgroep of de stelselgroep, berekend over het afgeronde groepstotaal, en dragen de onderliggende ruimteregels alleen het aantal vierkante meters.

Voor onzelfstandig rubriek 1 en 2 staan de punten op de stelselgroep, niet op de gedeeld-met-laag ([#393](https://github.com/woonstadrotterdam/woningwaardering/issues/393)): eerst worden alle toe te rekenen m² gesaldeerd en daarna éénmaal afgerond ([#391](https://github.com/woonstadrotterdam/woningwaardering/issues/391)). Bij een zoldercorrectie (vlizotrap) komt er één subtotaal direct onder de stelselgroep, met de correctie op hetzelfde niveau; de gedeeld-met-lagen met de ruimteregels hangen onder dat subtotaal. Dat subtotaal draagt punten, geen aantal: de ruimteregels tonen werkelijke m². Of toe te rekenen m² in de output horen, staat in [#403](https://github.com/woonstadrotterdam/woningwaardering/issues/403).

In de praktijk begin je met `WaarderingsgroepBuilder(stelsel, stelselgroep)`, hang je daar waarderingen en eventuele groeperende lagen onder, en sluit je af met `build()`.

`build()` telt de punten op en rondt de totaalpunten van de stelselgroep af op kwartpunten (§2.1.4 / §2.1.6). Ontstaat door die afronding een verschil tussen de som van de waarderingen en het stelselgroeptotaal, dan voegen we dat verschil toe als waardering **Afronding op kwartpunten**. Het eindresultaat is een `WoningwaarderingResultatenWoningwaarderingGroep`.

Punten van een waardering worden in de berekening niet tussentijds op twee decimalen afgerond; alleen het rubriektotaal wordt op een kwart punt afgerond. Bij het vastleggen in de output krijgen de rijen wel twee decimalen. **Afronding op kwartpunten** sluit het verschil tussen de som van die getoonde rijen en het stelselgroeptotaal, zodat de puntenkolom in zowel de output als het rapport optelt tot het totaal. `tests/utils.py` bewaakt de outputinvarianten (rijen op ten hoogste twee decimalen, kolom telt op tot het totaal); `tests/stelsels/test_builders.py` bewaakt dat het totaal uit de onafgeronde builder-punten volgt.
