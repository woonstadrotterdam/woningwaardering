# Criteriumstrategie

Tijdens een `waardeer()`-aanroep bouw je de uitkomst van een stelselgroep eerst op als een hiërarchie van waarderingen. Daarvoor gebruiken we de builders in `woningwaardering/stelsels/builders.py`. Een `WaarderingsgroepBuilder` verzamelt de waarderingen binnen één stelselgroep, terwijl een `WaarderingBuilder` één afzonderlijke waardering opbouwt. Pas bij `build()` vertalen we die hiërarchie naar een resultaat in VERA-format: een platte lijst waarderingen waarin de samenhang via `bovenliggendeCriterium` is vastgelegd.

Je bouwt die hiërarchie op met drie methoden:

- `met_onderliggend(...)` — inhoudelijke waardering (punten en/of aantal)
- `met_subgroep(...)` — groeperende tussenlaag
- `gedeeld_met(...)` — privé- of deel-laag (onzelfstandige woonruimten en/of adressen)

## Structuur van de output

De onderstaande voorbeelden tonen een gemeenschappelijke stelselgroep voor een zelfstandige en een onzelfstandige eenheid. Links staat een herkenbare naam, rechts de rol in de structuur.

> Door hoe VERA is opgebouwd is élke regel hieronder een waardering met een criterium.

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

De uitkomst van een stelselgroep is een hiërarchie van waarderingen. De samenhang loopt via `bovenliggendeCriterium`: elke regel is een waardering met een criterium; een criterium kan onderliggende criteria hebben. Punten en aantallen horen bij de waardering; het criterium draagt de identiteit, naam en plek in de hiërarchie.

Een mogelijke verzameling waarderingen binnen een stelselgroep is:

1. **Gedeeld-met** (indien gedeelde ruimte): geeft aan met hoeveel adressen en/of onzelfstandige woonruimten de ruimte wordt gedeeld.
2. **Subgroep**: een groeperend criterium binnen de stelselgroep (zelf géén stelselgroep). Wat een subgroep groepeert, verschilt per stelselgroep.
3. **Waardering** — een inhoudelijke waardering met punten en/of een aantal.

Bij gedeelde ruimten kan er op twee niveaus sprake zijn van deling: eerst (waar van toepassing) deling met onzelfstandige woonruimten, daaronder deling met adressen.

Een subgroep of gedeeld-met-laag verschijnt pas in de output als er inhoud onder hangt, of als er punten, een aantal of een opslagpercentage aan wordt toegekend. Lege groeperende lagen blijven weg.

Meestal draagt een subgroep zelf geen punten: die staan op de onderliggende waarderingen. Bij de oppervlakte-stelselgroepen (`oppervlakte_van_vertrekken` en `oppervlakte_van_overige_ruimten`) staan de punten juist op de subgroep (berekend over het afgeronde groepstotaal); de onderliggende ruimteregels dragen dan alleen het aantal vierkante meters.

Stapsgewijs: begin met `WaarderingsgroepBuilder(stelsel, stelselgroep)`, hang waarderingen en lagen aan, en sluit af met `build()`. Die laatste telt de punten op en rondt de totaalpunten van de stelselgroep af op kwartpunten. Ontstaat door die afronding een verschil tussen de som van de waarderingen en de totaalpunten van de stelselgroep, dan voegen we dat verschil toe als waardering **Afronding op kwartpunten**. Uiteindelijk leveren deze stappen een `WoningwaarderingResultatenWoningwaarderingGroep` op.

Een subgroep of gedeeld-met-laag verschijnt pas in de output zodra er inhoud onder hangt, of zodra er punten, een aantal of een opslagpercentage aan wordt toegekend (`lazy` activatie in de builders).
