# Datamodel Uitbreidingen

Tijdens de ontwikkeling van de woningwaardering-package komt het voor dat de VERA modellen niet toereikend zijn om de punten voor een stelselgroep te berekenen. Daarom kunnen er indien nodig uitbreidingen gemaakt worden op de VERA modellen. In deze sectie onderbouwen en documenteren wij deze uitbreidingen. In de [documentatie over Referentiedata](https://woningwaardering.readthedocs.io/nl/latest/contribute.html#datamodellen) wordt uitgelegd hoe uitbreidingen toegevoegd moeten worden als contributor van dit project.

## Ruimtedetailsoort kast

Binnen het woningwaarderingsstelsel mag onder bepaalde voorwaarden de oppervlakte van vaste kasten worden opgeteld bij de ruimte waar de deur van de kast zich bevindt. Als hier bij het inmeten geen rekening mee gehouden is, kan het attribuut verbonden_ruimten gebruikt worden om de met een ruimte verbonden vaste kasten mee te laten nemen in de waardering. Hiervoor is de VERA referentiedata binnen deze repository uitgebreid met ruimtedetailsoort `Kast`, code `KAS`.

## Verbonden ruimten

Het attribuut `verbonden_ruimten` bevat de ruimten die in verbinding staan met de ruimte die het attribuut bezit. `verbonden_ruimten` wordt gebruikt bij het berekenen van de waardering van kasten en verwarming van ruimten. `verbonden_ruimten` heeft type `Optional[list[EenhedenRuimte]]` en is een uitbreiding op `EenhedenRuimte`. Voor deze uitbreiding staat een [github issue](https://github.com/Aedes-datastandaarden/vera-openapi/issues/47) open ter aanvulling op het VERA model.

## Gedeeld met aantal eenheden

Het attribuut `gedeeld_met_aantal_eenheden` geeft het aantal eenheden (één adres staat gelijk aan één eenheid) weer waarmee een bepaalde ruimte wordt gedeeld. Dit attribuut wordt gebruikt bij het berekenen van de waardering van een gedeelde ruimte met ruimtedetailsoort berging. `gedeeld_met_aantal_eenheden` heeft als type `Optional[int]`. Er staat een github issue open om dit ter discussie te stellen: https://github.com/Aedes-datastandaarden/vera-openapi/issues/44

## Gedeeld met aantal onzelfstandige woonruimten

Het attribuut `gedeeld_met_aantal_onzelfstandige_woonruimten` geeft het aantal onzelfstandige woonruimten (op zelfde adres) weer waarmee een bepaalde ruimte wordt gedeeld. `gedeeld_met_aantal_onzelfstandige_woonruimten` heeft als type `Optional[int]`. Er staat een github issue open om dit ter discussie te stellen: https://github.com/Aedes-datastandaarden/vera-openapi/issues/44

## Bouwkundige elementen

In de beleidsboeken wordt soms op basis van een bouwkundig element dat aanwezig is in een ruimte, een uitzondering of nuance op een regel besproken. Dit kan bijvoorbeeld tot gevolg hebben dat er punten in mindering worden gebracht, of punten extra gegeven worden. Bijvoorbeeld bij de berekening van de oppervlakte van een zolder als vertrek of als overige ruimte is er informatie nodig over de trap waarmee de zolder te bereiken is. Daartoe is het VERA model `EenhedenRuimte` uitgebreid met het attribuut `bouwkundige_elementen` met als type `Optional[list[BouwkundigElementenBouwkundigElement]]`. Er staat een github issue open om `bouwkundige_elementen` standaard in het VERA model toe te voegen: https://github.com/Aedes-datastandaarden/vera-openapi/issues/46

> Inmiddels is het attribuut `bouwkundige_elementen` toegevoegd aan het VERA model `EenhedenRuimte` in VERA 4.1.6. Omdat wij VERA 4.1.5 gebruiken is het technisch gezien nog een uitbreiding van ons op het VERA-model.

## Verkoeld en verwarmd

In de VERA standaard is nog geen mogelijkheid om aan te geven of een ruimte verwarmd en/of verkoeld is. Het attribuut `verwarmde_vertrekken_aantal` bestaat wel, maar dit bestaat op niveau van de eenheid en daarin bestaat geen onderscheid tussen vertrekken en overige ruimten.  
Hierom hebben wij twee boolean kenmerken toegevoegd aan `EenhedenRuimte`: `verwarmd` en `verkoeld`. Deze kenmerken geven aan of een ruimte verwarmd en/of verkoeld is.

Dit is aangekaart in deze twee issues:

- https://github.com/Aedes-datastandaarden/vera-openapi/issues/41
- https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/100

## Datum afsluiten huurovereenkomst

Voor een correcte waardering van rijksmonumenten dient de afsluitings datum van de huurovereenkomst opgegeven te worden. In de VERA standaard bestaat binnen het BVG domein geen model dat deze informatie bevat. Het VERA model `EenhedenEenheid` is uitgebreid met het attribuut `datum_afsluiten_huurovereenkomst`. Zie ook: https://github.com/Aedes-datastandaarden/vera-openapi/issues/69

## Installaties

Installaties zouden toegevoegd moeten worden aan het VERA model `EenhedenRuimte`. Het attribuut `installaties` bestaat al in de wiki, maar nog niet in de `vera-openapi` repository versie 4.1.5: https://github.com/Aedes-datastandaarden/vera-openapi/issues/70. VERA is hierin vrij verwarrend m.b.t. bouwkundige elementen / installaties / [voorzieningen](https://www.coraveraonline.nl/index.php/Referentiedata:VOORZIENINGSOORT). Op dit moment gebruiken wij `installaties` als attribuut op ruimte met als type `Optional[list[Voorzieningsoort]]`.

## Aantal

Het attribuut `Eenhedenruimte.aantal` is als uitbreiding op het VERA-model toegevoegd. Hierdoor is het mogelijk om aan te geven hoeveel van deze specifieke ruimte er zijn. Dit attribuut wordt uitsluitend gebruikt in het berekenen van de punten voor Gemeenschappelijke Parkeerruimten. Hier door is het niet nodig om elk parkeervak van een parkeergarage of parkeerterrein mee te geven aan een eenheid.

## Parkeergelegenheden

Als uitbreiding op de referentiedata is de `Ruimtesoort.Parkeergelegenheid` toegevoegd. Daarnaast zijn er verschillende parkerruimten (`Ruimtedetailsoort`) toegevoegd. Deze uitbreidingen zijn overgenomen vanuit de github issue https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/110#issuecomment-2190641829.
