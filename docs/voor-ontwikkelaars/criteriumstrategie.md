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

Meestal draagt een subgroep zelf geen punten; die staan op de onderliggende waarderingen. Bij de oppervlakte-stelselgroepen (`oppervlakte_van_vertrekken` en `oppervlakte_van_overige_ruimten`) is dat anders: daar staan de punten op de subgroep, berekend over het afgeronde groepstotaal, en dragen de onderliggende ruimteregels alleen het aantal vierkante meters.

In de praktijk begin je met `WaarderingsgroepBuilder(stelsel, stelselgroep)`, hang je daar waarderingen en eventuele groeperende lagen onder, en sluit je af met `build()`.

`build()` telt de punten op en rondt de totaalpunten van de stelselgroep af op kwartpunten. Ontstaat door die afronding een verschil tussen de som van de waarderingen en het stelselgroeptotaal, dan voegen we dat verschil toe als waardering **Afronding op kwartpunten**. Het eindresultaat is een `WoningwaarderingResultatenWoningwaarderingGroep`.
