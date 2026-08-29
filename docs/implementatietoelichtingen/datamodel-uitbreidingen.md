# Datamodel uitbreidingen

## Ruimtedetailsoort kast

Binnen het woningwaarderingsstelsel mag onder bepaalde voorwaarden de oppervlakte van vaste kasten worden opgeteld bij de ruimte waar de deur van de kast zich bevindt. Als hier bij het inmeten geen rekening mee gehouden is, kan het attribuut verbonden_ruimten gebruikt worden om de met een ruimte verbonden vaste kasten mee te laten nemen in de waardering. Hiervoor is de VERA referentiedata binnen deze repository uitgebreid met ruimtedetailsoort `Kast`, code `KAS`.

## Verbonden ruimten

Het attribuut `verbonden_ruimten` bevat de ruimten die in verbinding staan met de ruimte die het attribuut bezit. `verbonden_ruimten` wordt gebruikt bij het berekenen van de waardering van kasten en verwarming van ruimten. `verbonden_ruimten` heeft type `Optional[list[EenhedenRuimte]]` en is een uitbreiding op `EenhedenRuimte`. Voor deze uitbreiding staat issue [https://github.com/Aedes-datastandaarden/vera-openapi/issues/47](https://github.com/Aedes-datastandaarden/vera-openapi/issues/47) open ter aanvulling op het VERA model.

## Gedeeld met aantal adressen

Het attribuut `gedeeld_met_aantal_adressen` geeft het aantal adressen weer waarmee een bepaalde ruimte wordt gedeeld. Dit attribuut wordt gebruikt bij het berekenen van de waardering van een gedeelde ruimte. `gedeeld_met_aantal_adressen` heeft als type `Optional[int]`. Er staat een github issue open om dit ter discussie te stellen: [https://github.com/Aedes-datastandaarden/vera-openapi/issues/44](https://github.com/Aedes-datastandaarden/vera-openapi/issues/44)

Voorheen gebruikten we hiervoor het attribuut `gedeeld_met_aantal_eenheden`. Dit attribuut blijft als deprecated veld ondersteund voor backwards compatibility: de waarde wordt overgenomen naar `gedeeld_met_aantal_adressen`.

## Gedeeld met aantal onzelfstandige woonruimten

Het attribuut `gedeeld_met_aantal_onzelfstandige_woonruimten` geeft het aantal onzelfstandige woonruimten (op zelfde adres) weer waarmee een bepaalde ruimte wordt gedeeld. `gedeeld_met_aantal_onzelfstandige_woonruimten` heeft als type `Optional[int]`. Er staat een github issue open om dit ter discussie te stellen: [https://github.com/Aedes-datastandaarden/vera-openapi/issues/44](https://github.com/Aedes-datastandaarden/vera-openapi/issues/44)

## Bouwkundige elementen

In de beleidsboeken wordt soms op basis van een bouwkundig element dat aanwezig is in een ruimte, een uitzondering of nuance op een regel besproken. Dit kan bijvoorbeeld tot gevolg hebben dat er punten in mindering worden gebracht, of punten extra gegeven worden. Bijvoorbeeld bij de berekening van de oppervlakte van een zolder als vertrek of als overige ruimte is er informatie nodig over de trap waarmee de zolder te bereiken is. Daartoe is het VERA model `EenhedenRuimte` uitgebreid met het attribuut `bouwkundige_elementen` met als type `Optional[list[BouwkundigElementenBouwkundigElement]]`. Er staat een github issue open om `bouwkundige_elementen` standaard in het VERA model toe te voegen: [https://github.com/Aedes-datastandaarden/vera-openapi/issues/46](https://github.com/Aedes-datastandaarden/vera-openapi/issues/46)

> Inmiddels is het attribuut `bouwkundige_elementen` toegevoegd aan het VERA model `EenhedenRuimte` in VERA 4.1.6. Omdat wij VERA 4.1.5 gebruiken is het technisch gezien nog een uitbreiding van ons op het VERA-model.

## Verkoeld en verwarmd

In de VERA standaard is nog geen mogelijkheid om aan te geven of een ruimte verwarmd en/of verkoeld is. Het attribuut `verwarmde_vertrekken_aantal` bestaat wel, maar dit bestaat op niveau van de eenheid en daarin bestaat geen onderscheid tussen vertrekken en overige ruimten.  
Hierom hebben wij twee boolean kenmerken toegevoegd aan `EenhedenRuimte`: `verwarmd` en `verkoeld`. Deze kenmerken geven aan of een ruimte verwarmd en/of verkoeld is.

Dit is aangekaart in deze twee issues:

- [https://github.com/Aedes-datastandaarden/vera-openapi/issues/41](https://github.com/Aedes-datastandaarden/vera-openapi/issues/41)
- [https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/100](https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/100)

## Datum afsluiten huurovereenkomst

Voor een correcte waardering van rijksmonumenten dient de afsluitings datum van de huurovereenkomst opgegeven te worden. In de VERA standaard bestaat binnen het BVG domein geen model dat deze informatie bevat. Het VERA model `EenhedenEenheid` is uitgebreid met het attribuut `datum_afsluiten_huurovereenkomst`. Zie ook: [https://github.com/Aedes-datastandaarden/vera-openapi/issues/69](https://github.com/Aedes-datastandaarden/vera-openapi/issues/69)

## Installaties

Installaties zouden toegevoegd moeten worden aan het VERA model `EenhedenRuimte`. Het attribuut `installaties` bestaat al in de wiki, maar nog niet in de `vera-openapi` repository versie 4.1.5: [https://github.com/Aedes-datastandaarden/vera-openapi/issues/70](https://github.com/Aedes-datastandaarden/vera-openapi/issues/70). Op dit moment gebruiken wij `installaties` als attribuut op ruimte met als type `Optional[list[Installatiesoort]]`.

## Bouwkundige elementen naast installaties

Dezelfde voorziening mag zowel als bouwkundig element als als installatie op een ruimte worden meegegeven; beide attributen zijn geldige modelleringen. `installaties` bevat echter alleen een soortcode en geen id, terwijl een bouwkundig element wel een eigen id draagt. Er is dus geen identiteitskoppeling tussen beide representaties: we kunnen niet vaststellen of een meegegeven installatie hetzelfde object beschrijft als een bouwkundig element in dezelfde ruimte.

Voor de stelselgroep Sanitair houden we daarom per installatiesoort het hoogste van beide aantallen aan: het aantal meegegeven installaties, of het aantal bouwkundige elementen dat op die installatiesoort mapt. Een voorziening die dubbel is gemodelleerd telt zo niet twee keer mee, terwijl extra bouwkundige elementen wel meetellen.

| Bouwkundig element | Installatiesoort |
| --- | --- |
| `Wastafel` | `Wastafel` |
| `Fontein` | `Wastafel` |
| `Douche` | `Douche` |
| `Bad` | `Bad` |
| `Kast` | `Kastruimte` |
| `Closetcombinatie` | `Staand toilet` |

Omdat het resultaat een maximum is, verandert een tweede aanroep niets meer. Dat is nodig omdat meerdere stelselgroepen deze aanvulling op dezelfde eenheid uitvoeren. De bouwkundige elementen blijven behouden: zij dragen gegevens (id, afmetingen) die een installatiesoort niet kan bevatten.

> [!NOTE]
> De regel is een keuze bij ontbrekende informatie, geen beleidsregel. Bij één bouwkundig element naast twee installaties van dezelfde soort tellen we er twee, ook als het in werkelijkheid om drie voorzieningen gaat. Die restambiguïteit is niet op te lossen zolang `installaties` geen identiteit draagt. Geef bij voorkeur één representatie per voorziening mee.

## Aantal

Het attribuut `Eenhedenruimte.aantal` is als uitbreiding op het VERA-model toegevoegd. Hierdoor is het mogelijk om aan te geven hoeveel van deze specifieke ruimte er zijn. Dit attribuut wordt uitsluitend gebruikt in het berekenen van de punten voor Gemeenschappelijke Parkeerruimten. Hier door is het niet nodig om elk parkeervak van een parkeergarage of parkeerterrein mee te geven aan een eenheid.

> [!NOTE]
> Een privé-`carport` of privé-`parkeerplaats` wordt niet in rubriek 10 maar in rubriek 8 Buitenruimten gewaardeerd (zie [Parkeergelegenheden](#parkeergelegenheden)), en daar telt `aantal` niet mee: die rubriek waardeert de oppervlakte. Geef meerdere privé-plekken daarom als afzonderlijke ruimten mee, elk met hun eigen oppervlakte.

## Parkeergelegenheden

Als uitbreiding op de referentiedata zijn er verschillende parkeerruimten (`Ruimtedetailsoort`) toegevoegd, die overeenkomen met Type I, II en III parkeergelegenheden vanuit het WWS-beleidsboek:

| `Ruimtedetailsoort` | Code | Wettekst-criterium | Type |
| --- | --- | --- | --- |
| `parkeerplek_in_inpandige_afgesloten_parkeergarage` | `PIP` | in een afgesloten parkeergarage | Type I |
| `parkeerplek_in_uitpandige_afgesloten_parkeergarage` | `PUP` | in een afgesloten parkeergarage | Type I |
| `parkeerplek_buiten_met_dak_behorend_bij_complex` | `PBD` | buiten met dak | Type II |
| `parkeerplek_buiten_behorend_bij_complex` | `PBC` | buiten zonder dak | Type III |

> [!NOTE]
> `PIP`, `PUP`, `PBD` en `PBC` zijn Type-detailsoorten: zij zeggen iets over de **parkeergelegenheid**, niet over het gebruiksrecht. De plek kan aan één adres zijn toegewezen (privé) of gedeeld worden; in beide gevallen wordt zij in [rubriek 10](zelfstandige-woonruimten.md#210-gemeenschappelijke-parkeerruimten) gewaardeerd.
>
> Type II/III in de wettekst zijn "buiten behorende tot het complex of de woning". Locatie is geen typecriterium. `carport` en `parkeerplaats` zijn de VERA-buitenruimten daarvoor (privé in rubriek 8, gemeenschappelijk in rubriek 10). `PBD` en `PBC` vullen het gat dat VERA niet dekt: een Type II/III-plek in een gemeenschappelijke parkeergelegenheid. De codes `PBD`/`PBC` blijven staan omdat hernoemen de referentiedata zou breken.

> [!NOTE]
> `Ruimtedetailsoort.parkeerplaats` (`PAR`) is in de VERA-referentiedata omschreven als "Eigen parkeerplaats of oprit bij de woning" en is dus per definitie een privé-plek. Gebruik voor een gemeenschappelijke parkeerplek een van de Type-detailsoorten hierboven. Wordt een `parkeerplaats` toch als gemeenschappelijk meegegeven, dan volgt een `UserWarning` en waarderen we de plek als Type III.
