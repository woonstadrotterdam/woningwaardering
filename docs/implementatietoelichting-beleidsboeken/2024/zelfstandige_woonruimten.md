# 2024. Zelfstandige Woonruimten

## 4.2 Oppervlakte van Vertrekken

### 4.2.1 Wat zijn vertrekken?

Het eerste onderdeel van de woningwaardering is de oppervlakte van vertrekken. Onder vertrekken worden woonkamer, andere kamers (hobbykamer, studeerkamer, slaapkamer en eetkamer), keuken, badkamer of doucheruimte verstaan. De waardering van vertrekken is 1 punt per m2.

Geen vertrekken zijn: schuren, zolderberging, kelders, wasruimten, bijkeukens, garages en bergingen, gang, (speel)hal en zogenoemde verkeersruimten (bijvoorbeeld overlopen). De oppervlakte van deze ruimten tellen dus niet mee als vertrekken.  

De Huurcommissie geeft op een aantal punten nadere invulling aan de hierboven genoemde wettelijke begrippen. Dat wordt hierna beschreven.

**Woonkamer of andere kamer**  
Een woonkamer of een andere kamer is dus een vertrek in de zin van het woningwaarderingsstelsel.

Hiervan is alleen sprake als:

- ~~De vloer begaanbaar is.~~
- ~~De muren en wanden uit vast materiaal bestaan.~~
- ~~En de daglichttoetreding, de ventilatiemogelijkheid en het aantal elektrische lichtpunten in overeenstemming zijn met de geldende verkeersopvattingen.~~
- De ruimte een oppervlakte heeft van minimaal 4 m2.
- ~~De ruimte over de volle lengte ten minste 1,50 m breed is.~~
- ~~De ruimte over ten minste 50% van de oppervlakte een vrije hoogte heeft van 2.10 m (gemeten vanaf de vloer tot het zichtbare plafond).~~

Alleen als aan al deze eisen is voldaan, wordt de (oppervlakte van de) woonruimte of andere kamer meegeteld als “vertrek”. Zo niet, dan wordt de oppervlakte meegeteld als “overige ruimte” (zie [paragraaf 4.3](#43-oppervlakte-van-overige-ruimten).).  
Uitzondering hierop geldt voor de keuken: de eisen van minimaal 4 m2 en ~~minimaal 1,50 m breedte~~ gelden niet voor de keuken en verzetten zich er dus niet tegen om een keuken als “vertrek” aan te merken en overeenkomstig te waarderen.

**Badkamer of doucheruimte**  
Een badkamer of doucheruimte is dus een vertrek in de zin van het woningwaarderingsstelsel.

Hiervan is alleen sprake als:

- ~~De vloer begaanbaar is.~~
- ~~De muren en wanden uit vast materiaal bestaan.~~
- ~~En de ventilatiemogelijkheid en het aantal elektrische lichtpunten in overeenstemming zijn met de geldende verkeersopvattingen.~~
- ~~De ruimte over ten minste 50% van de oppervlakte een vrije hoogte heeft van 2,00 m. (gemeten vanaf de vloer tot het zichtbare plafond).~~

~~Alleen als aan al deze eisen is voldaan, wordt de (oppervlakte van de) badkamer of doucheruimte meegeteld als “vertrek”. Zo niet, dan wordt de oppervlakte meegeteld als “overige ruimte” (zie verderop).~~

> Hoewel de VERA-standaard een onderscheid maakt tussen badkamer, doucheruimte en badkamer/toilet (badkamer met toilet) beschouwen wij ieder van deze ruimtes indien zij een toilet bevatten als een badkamer met toilet, conform hoe de huurcommissie omgaat met deze ruimtes.. Zie ook [dit Github issue](https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/96).

Voor gecombineerde bad-/doucheruimte met toilet geldt een minimale oppervlakte van 0,64 m².

> Elke Badkamer, Badkamer/toilet of Doucheruimte die als vertrek is aangemerkt wordt meegeteld als vertrek, tenzij onder aftrek van 1 m2 voor een in de ruimte geplaatst toilet de oppervlakte kleiner is dan 0,64 m². (Zie punt 5 in [4.2.2](#422-hoe-wordt-de-oppervlakte-van-vertrekken-gemeten)).

**Zolderruimte**  
Zolderruimten zijn in het algemeen “overige ruimte”. Echter, in geval een zolderruimte een functie heeft als “vertrek” (dus woonkamer, andere kamers, badkamer of doucheruimte), en ook voldoet aan de eisen die daarvoor gelden (zie hierboven), dan mag de zolderruimte meetellen als “vertrek”, mits deze ruimte bereikbaar is via een vaste trap ~~en het dak beschoten is~~.

> In het beleidsboek wordt er onderscheid gemaakt tussen een zolder vertrek met een vaste trap of zolder met een ander soort trap. Wanneer een zolder als vertrek wordt aangemerkt moet deze te bereiken zijn via een vaste trap. Daarom wordt er voor een zolder gekeken of er een vaste trap in de `bouwkundige_elementen` zit. Als dit het geval is dan telt de gehele oppervlakte van de zolder mee voor de punten van Oppervlakte van Vertrekken.

### 4.2.2 Hoe wordt de oppervlakte van vertrekken gemeten?

De wetgever heeft in de toelichting op het woningwaarderingsstelsel een aantal meetinstructies meegegeven:

1. Meting van de oppervlakte van vertrekken vindt plaats ~~van muur tot muur, op een hoogte van 1,50 m boven de vloer,~~ inclusief de oppervlakte van alle tot de woning behorende losse en vaste kasten (kleiner dan 2m²). ~~Deze meethoogte geldt ook als de oppervlakte afwijkt van die op vloerniveau.~~

De Huurcommissie hanteert hierbij de volgende uitgangspunten.

~~Als er sprake is van een pui wordt de binnenzijde van die pui (het kozijn) genomen. Een erker wordt meegerekend indien deze inwendig een vrije hoogte heeft van ten minste 1,50 m. Indien er sprake is van een zgn. entresol (tussenverdieping) dan dient de oppervlakte onder en/of boven deze entresol te worden meegerekend, indien de vrije hoogte ten minste 1,50m bedraagt.~~ Voor het meten van vertrekken die met elkaar in open verbinding staan, zie verderop.  
“Alle tot de woning behorende losse en vaste kasten” lees de Huurcommissie als: “alle tot de vertrekken behorende kasten”. De plaats van de deur van de kast bepaalt bij welk vertrek de kast behoort. Dus een kast die in een vertrek uitkomt wordt, ongeacht de afmeting, bij dat vertrek geteld. Dat geldt ook voor het waarderen van een kastenwand tussen twee vertrekken.

- Van vaste kasten (kleiner dan 2m²) wordt de netto oppervlakte bepaald en bij de oppervlakte van het betreffende vertrek opgeteld;
- Een kast, (kleiner dan 2m²) waarvan de deur uitkomt op een verkeersruimte, wordt niet gewaardeerd;
- Losse kasten zijn niet van belang bij het meten. De oppervlakte van het vertrek wordt bepaald, incl. de oppervlakte die wordt ingenomen door een losse kast;

> Binnen het woningwaarderingsstelsel mag onder bepaalde voorwaarden de oppervlakte van vaste kasten worden opgeteld bij de ruimte waar de deur van de kast zich bevindt. Als hier bij het inmeten geen rekening mee gehouden is, kan het attribuut `verbonden_ruimten` gebruikt worden om de met een ruimte verbonden vaste kasten mee te laten nemen in de waardering. Hiervoor is de VERA referentiedata binnen deze repository uitgebreid met ruimtedetailsoort Kast, code KAS.

2. ~~Als oppervlakte van een vertrek met een (ten dele hellend of verlaagd plafond geldt dat alleen het gedeelte waarboven het plafond ten minste 1,50m hoog is wordt meegeteld bij de berekening van de oppervlakte.~~

~~De Huurcommissie eist in geval van een (ten dele) hellend plafond dat de 1,50m-hoogte loopt tot het dakbeschot of tot het zichtbare dakvlak of plafond. Met gordingen en balken wordt bij de meting geen rekening gehouden.~~

3. ~~De vloeroppervlakte onder aanrechten, toestellen in de keuken, badkuip, lavet of douchebak, moederhaard, c.v.-ketel en boilerinstallatie, wordt meegeteld.~~

~~De Huurcommissie gaat hier als volgt mee om. Indien zich in een vertrek, of in een kast in een vertrek, een gas- en/of elektrameter bevindt, dan wordt de oppervlakte gewaardeerd onder aftrek van 30 x 60 cm (minimale afmeting meterkast bestaande bouw). De vloeroppervlakte onder radiatoren wordt meegeteld.~~

4. ~~De oppervlakte die wordt ingenomen door schoorsteenkanalen, ventilatiekanalen of stand- of grondleidingen (tenzij horizontale leidingen, zie hierna) wordt niet meegeteld.~~

~~Bij een schoorsteenmantel en/of rookkanaal (die naar boven of beneden breed kan uitlopen) is de oppervlakte op 1,50m-hoogte bepalend. De oppervlakte die wordt ingenomen door standleidingen (verticale leidingen) wordt niet meegeteld. De oppervlakte die wordt ingenomen door grondleidingen (horizontale leidingen), wordt wel meegeteld.~~

5. Indien een toilet in een badruimte of doucheruimte is geplaatst, wordt de oppervlakte van die ruimte met één vierkante meter verminderd.

6. ~~Van de oppervlakte onder een open dan wel gesloten vaste trap geldt dat gedeelte waar de ruimte tussen vloer en onderkant trap ten minste 1,50m hoog is.~~

7. Afronding van de oppervlakte op hele vierkante meters vindt plaats na saldering van de oppervlakte van alle vertrekken; bij 0,5m² of meer wordt afgerond naar boven, bij minder dan 0,5m² naar beneden. Waardering in punten vindt na saldering en afronding plaats.

De Huurcommissie licht dit als volgt toe:  

Afronding: eerst de oppervlakte per vertrek op 2 decimalen afronden en pas daarna de oppervlakte van alle vertrekken salderen en afronden op hele vierkante meters.

**_Voorbeeld:_**  
_kamer : lengte 3,76m x breedte 4,12m = 15,4912 m², afgerond : 15,49 m²_  
_keuken: lengte 2,95m x breedte 3,81m = 11,2395 m², afgerond : 11,24 m²_  
_Totaal : 26,73 m² Afronding op hele m² : 27 m²._

8. ~~Twee vertrekken die met elkaar in verbinding staan, worden in een bepaald geval als één vertrek gewaardeerd. Dit is het geval als zich tussen die twee vertrekken een opening bevindt, die breder is dan 50% van de muur, waarin deze opening zich bevindt (zie schets hieronder). Het moet hierbij gaan om een niet afsluitbare opening, die doorloopt tot aan de vloer. De muur wordt gemeten in het vertrek, waarin de tussenwand het smalst is.~~

## 4.3 Oppervlakte van overige ruimten

### 4.3.1 Wat zijn overige ruimten?

“Overige ruimten” die voor een puntenwaardering in aanmerking komen zijn:  

a. bijkeukens  
b. bergingen  
c. wasruimte  
d. ~~schuren~~  
e. garages  
f. zolderbergingen  
g. kelders  
h. parkeerplaats (zie paragraaf 4.9.6)

> In de VERA-referentiedata heeft schuur en schacht dezelfde detailsoortcode. Hierdoor is het niet mogelijk om schuur als overige ruimte te waarden, omdat schacht niet als overige ruimte wordt gewaardeerd. Bovendien is schuur geen ruimtedetailsoort in de Aedes ILS. Geef daarom een schuur aan als berging in het input-model.

Deze ruimten tellen alleen mee als de oppervlakte van een ruimte afzonderlijk gelijk is aan of groter dan twee vierkante meter, ~~voor zover de plafondhoogte ten minste 1,50 meter is boven de vloer.~~  

Verkeersruimten zoals hallen, gangen, en overlopen worden sowieso niet afzonderlijk gewaardeerd, dus krijgen geen punten op basis van dit onderdeel van het woningwaarderingsstelsel.

Tot bergingen worden de volgende ruimten gerekend: vaste kasten, bergingen in, achter, voor, dan wel onder de woning, bergingen onder de kap van etagewoningen, bergingen in flatgebouwen en dergelijke, mits deze een afzonderlijke ruimte vormen.

### 4.3.2 Hoe wordt de oppervlakte van overige ruimte gemeten?

De wetgever heeft een aantal eisen en meetinstructies meegegeven:

1. ~~De ruimten worden slechts als “overige oppervlakte” gewaardeerd, als de vloer begaanbaar is.~~

2. ~~Van de overige ruimten wordt de gehele oppervlakte gemeten, dus zonder aftrek van loop- of verkeersruimte. De oppervlakte van een trapgat wordt wel in mindering gebracht. De oppervlakte die een uitschuifbare of opvouwbare trap in gesloten toestand inneemt, wordt van de oppervlakte van de ruimte afgetrokken.~~

3. ~~Meting van de oppervlakte vindt plaats van muur tot muur, op een hoogte van 1,50m boven de vloer. En ook inclusief de oppervlakte van de moederhaard, CV-ketel en boilerinstallatie. Maar niet: de oppervlakte die wordt ingenomen door schoorsteenkanalen, ventilatiekanalen of stand- of grondleidingen.~~

~~De Huurcommissie meet als er sprake is van een pui, vanaf de binnenzijde van die pui (het kozijn). Ook een erker, die inwendig een vrije hoogte heeft van ten minste 1,50m, telt mee. De oppervlakte onder en/of boven een zogenaamde entresol (tussenverdieping) wordt meegerekend, indien de hoogte minstens 1,50m bedraagt.~~

~~De Huurcommissie berekent de hoogte van 1,50 meter door te meten tot het dakbeschot, het zichtbare dakvlak of plafond (gordingen en balken blijven buiten de meting).~~

4. Ook de oppervlakte van alle tot de woning behorende losse en vaste kasten (kleiner dan 2m²) wordt meegerekend.

Losse kasten zijn niet van belang bij het meten. De oppervlakte van de overige ruimte wordt bepaald, incl. de oppervlakte die wordt ingenomen door een losse kast.  
Van vaste kasten (kleiner dan 2m²) die uitkomen in een wel gewaardeerde overige ruimte wordt de netto oppervlakte bepaald en bij de oppervlakte opgeteld.  
Een kast, (kleiner dan 2m²) waarvan de deur uitkomt op een verkeersruimte, wordt niet gewaardeerd.

~~Indien zich in een overige ruimte, of een kast in een overige ruimte, een gas- en/of elektrameter bevindt, dan wordt de oppervlakte gewaardeerd onder aftrek van 30 x 60 cm (minimale afmeting meterkast bestaande bouw).~~

5. ~~De Huurcommissie telt de vloeroppervlakte onder radiatoren ook mee.~~  

~~Voor een schoorsteenmantel en/of rookkanaal (die naar boven of beneden breed kan uitlopen) vindt de Huurcommissie de oppervlakte op 1,50m-hoogte bepalend.~~

6. ~~Van de oppervlakte onder een vaste (open of gesloten) trap, telt mee dat gedeelte waar de ruimte tussen vloer en onderkant trap ten minste 1,50m hoog is.~~

7. ~~De oppervlakte die door een in ingeschoven toestand liggende inschuifbare of opvouwbare trap wordt ingenomen, wordt niet meegeteld.~~

8. Betreft het een zolderberging dan wordt ~~, naast de eis van een begaanbare vloer,~~ als voorwaarde gesteld, ~~dat het dak beschoten is en~~ dat de zolderruimte via een tot de woning behorende trap bereikbaar is. Indien aan deze voorwaarden niet is voldaan, tellen zolderber gingen bij de woningwaardering niet mee.

Indien geen vaste trap aanwezig is, wordt het aantal punten van de vloeroppervlakte van de zolderruimte met 5 verminderd, doch niet met meer punten dan voor de oppervlakte van de zolderruimten wordt gegeven.

~~Is er op de zolderverdieping ook nog een vertrek aanwezig dat alleen bereikbaar is via het zoldergedeelte dan wordt de oppervlakte van het zoldergedeelte verminderd met de loopruimte om het vertrek te bereiken. De dan resterende zolderoppervlakte dient minimaal 2 m2 te bedragen en wordt dan gewaardeerd als overige ruimte.~~

> Wanneer een zolder als overige ruimte wordt beschouwd, kijken we in de `bouwkundige_elementen` van de zolder of de zolder bereikbaar is via een trap. Wanneer deze bereikbaar is via een vaste trap telt de volledige oppervlakte mee voor de punten berekening van Oppervlakte van Overige ruimten. Wanneer deze wel bereikbaar is, maar niet via een vaste trap, moeten er 5 punten in mindering worden gebracht omdat de ruimte niet bereikt kan worden met een vaste trap. In onze implementatie hebben wij er voor gekozen om te checken of er dan wel een vlizotrap aanwezig is in de `bouwkundige_elementen`, aangezien dit de enige andere soort trap in het VERA model is waarmee een zolder ruimte bereikt zou kunnen worden. Daarnaast is het onze keuze om de 5 punten in mindering te brengen door de oppervlakte van de zolder te corrigeren. Het beleidsboek geeft aan dat de punten in mindering gebracht moeten worden op de punten berekend voor deze ruimte. Maar ook dat punten pas berekend moeten worden wanneer de totale oppervlakte van een eenheid bekend is en afgerond is. Dit is tegenstrijdig en daarom kiezen wij de implementatie die volgens ons het beleidsboek zo goed mogelijk benadert. Let op, door de afronding komt deze berekening niet helemaal juist uit, maar dit is de benadering waar wij nu voor kiezen.

9. Een overloop is een verkeersruimte en wordt dus niet gewaardeerd. ~~Als er met aftrek van de verkeersruimte en trap voldoende ruimte overblijft en deze (zolder)overloop kennelijk ook bedoeld is als bergruimte, dan wordt deze ruimte wel gewaardeerd.~~

10. Gemeenschappelijke bergingen worden gewaardeerd als overige ruimte als:

- ~~zij binnen het woongebouw liggen of tot de onroerende aanhorigheden behoren;~~
- ~~de vergoeding daarvoor in de huurprijs van de woning is begrepen;~~
- de oppervlakte, na deling door het aantal woningen, per woning minstens 2m2 bedraagt.

> Hiervoor is het `EenhedenRuimte` model uitgebreid met het attribuut `gedeeldMetAantalEenheden` of `gedeeld_met_aantal_eenheden` voor de Python representatie. Om deze berekening correct uit te voeren dient deze waarde gevuld te zijn. Zonder deze waarde wordt de volledige oppervlakte van een ruimte meegeteld.

De toekenning van punten bij een gemeenschappelijke berging is als volgt: totale oppervlakte, afronden in m2, delen door het aantal woningen en waarderen als “overige ruimte”. Kasten <2m2 en uitkomend in een verkeersruimte worden niet meegeteld.

1. Afronding van de oppervlakte op hele vierkante meters vindt plaats na saldering van de oppervlakte van alle afzonderlijke ruimten; bij 0,5m² of meer wordt afgerond naar boven, bij minder dan 0,5m² naar beneden. Waardering in punten vindt na saldering en afronding plaats.

De Huurcommissie licht dit als volgt toe:  
Afronding: eerst de oppervlakte per overige ruimte op 2 decimalen afronden en pas daarna de oppervlakte van alle overige ruimten salderen en afronden op hele vierkante meters.

**_Voorbeeld:_**  
_Garage : lengte 3,16m x breedte 6,12m = 19,3392 m², afgerond : 19,34 m²_  
_Bijkeuken: lengte 2,11m x breedte 2,87m = 6,0557 m², afgerond : 6,06 m²_  
_Totaal : 25,40 m² Afronding op hele m² : 25 m²._  

## 4.4 Verwarming

Het waarderingsstelsel kent punten toe voor verwarming. Hierbij gelden de volgende regels.

### 4.4.1 Punten voor verwarmde vertrekken en overige ruimtes

Punten voor verwarming kunnen aan de orde zijn zowel als het gaat om vertrekken als om overige ruimtes (zie voor deze begrippen paragraaf 4.2.1 en 4.3.1). Voor vertrekken kunnen maximaal 2 punten per verwarmd vertrek worden gerekend, voor verwarmde overige ruimtes maximaal 1 punt per ruimte (met een maximum van 4 punten voor alle overige ruimtes). Een en ander is afhankelijk van of het gaat om een collectief of individueel verwarmingssysteem, zie verderop, paragraaf 4.4.3.

### ~~4.4.2 Verwarmingselementen behorend tot de onroerende zaak~~

Per vertrek wordt voor de verwarming punten toegekend ~~, mits de verwarmingselementen, zoals bijvoorbeeld een radiator, tot de onroerende zaak of zijn onroerende aanhorigheid behoort. Dit is bij een radiator het geval als hij is bevestigd aan de muur of in de grond. Een mobiele elektrische radiator is dus geen verwarmingselement als hier bedoeld en maakt dus een vertrek niet tot een verwarmd vertrek waarvoor punten vanwege verwarming aan toegekend kunnen worden~~.

~~Hetzelfde geldt voor gevelkachels en gashaarden. Een verdikte buis, pijp of moederhaard wordt wél gerekend als verwarmingselement dat tot de onroerende zaak behoort, indien deze als zodanig bedoeld of herkenbaar is.~~

### 4.4.3 Collectief of individueel verwarmingssysteem

Voor het aantal punten per vertrek of overige ruimte is relevant of het gaat om een collectief verwarmingssysteem of een individueel systeem. Een cv-installatie waarmee meerdere woningen worden verwarmd, wordt voor de puntenwaardering vanwege het onderdeel warmte als een individueel systeem beschouwd.

In geval van een collectief verwarmingssysteem wordt per verwarmd vertrek 1,5 punt gerekend en per overige ruimte 0,75 punt. Van een collectief verwarmingssysteem is bijvoorbeeld sprake bij stadsverwarming, een WKO-installatie en blokverwarming.

In geval van een individueel verwarmingssysteem wordt per verwarmd vertrek met 2 punten gerekend. Voor overige ruimte 1 punt. Van een individueel verwarmingssysteem is bijvoorbeeld sprake in geval de woonruimte een eigen of gezamenlijke cv-installatie heeft.

### ~~4.4.4 Vertrekken die met elkaar in verbinding staan~~

~~Hierboven is genoemd dat per vertrek maximaal 2 punten voor verwarming kunnen worden gerekend. Een bijzondere situatie is de situatie dat twee vertrekken met elkaar verbonden zijn door een opening. (NB voor open keuken geldt een afzonderlijk regel, zie hierna in 4.4.6).~~

~~In de situatie dat vertrekken met elkaar in verbinding staan geldt het volgende. In geval de opening tussen beide vertrekken breder is dan 50% van de muur waarin de opening zich bevindt en de opening niet afsluitbaar is, worden deze vertrekken als één verwarmd vertrek beschouwd in het kader van de punten voor verwarming (zie schets hieronder). In geval de opening minder breed is dan 50% van de muur waarin de opening zich bevindt, worden de vertrekken als twee verwarmde vertrekken beschouwd in het kader van de punten voor de verwarming (zie schets hieronder).~~

~~Let op: hoeveel punten dan aan dat ene of die twee vertrek(ken) vanwege verwarming worden toegekend, hangt af van of het om een collectief of individueel verwarmingssysteem gaat, zie hierboven (onder 4.4.3).~~

~~Vertrekken die met een schuifwand met elkaar in verbinding staan, worden altijd als afzonderlijke vertrekken geteld, dus ongeacht de breedte van de opening.~~

### ~~4.4.5 Overige ruimten die met elkaar in verbinding staan~~

~~Hierboven is genoemd dat per overige ruimte maximaal 1 punt voor verwarming kan worden gerekend. Een bijzondere situatie is de situatie dat twee overige ruimtes met elkaar verbonden zijn door een opening. De vraag is ook hier of deze overige ruimtes dan als één of meer worden geteld. In geval de opening breder is dan 50% van de muur waarin de opening zich bevindt en de opening niet afsluitbaar is, worden deze overige ruimtes als één overige ruimte beschouwd in het kader van de punten voor verwarming (zie schets hieronder). In geval de opening minder breed is dan 50% van de muur waarin de opening zich bevindt, worden de overige ruimtes als twee overige ruimtes beschouwd in het kader van de punten voor de verwarming (zie schets hieronder).~~

~~Let op: hoeveel punten dan aan dat ene of die twee overige ruimte(s) vanwege verwarming worden toegekend, hangt af van of het om een collectief of individueel verwarmingssysteem gaat, zie hierboven (onder 4.4.3).~~

### 4.4.6 Open keukens

Voor open keukens gelden de volgende regels.

Een open keuken wordt als afzonderlijk verwarmd vertrek beschouwd en krijgt dus 2 punten in geval van een individueel verwarmingssysteem en 1,5 punt in geval van een collectief verwarmingssysteem.

~~Wanneer is sprake van een open keuken? Onder een open keuken wordt hier verstaan een keuken die in open verbinding staat met een ander vertrek, terwijl zich tussen de keuken en het andere vertrek een opening bevindt, die breder is dan 50% van de tussenmuur. Het moet hierbij gaan om een niet afsluitbare opening, die doorloopt tot aan de vloer. De muur wordt gemeten in het vertrek waarin de tussenwand het smalst is (zie schets hieronder). De aan- of afwezigheid van een verwarmingselement in het gedeelte open keuken is niet relevant.~~  
~~In geval de opening smaller is dan 50% van de tussenmuur, wordt de keuken niet als open keuken beschouwd. In dit geval dient de keuken zelf over een verwarmingselement te beschikken om als verwarmd vertrek gewaardeerd te worden.~~

Ook een aanrecht dat is geplaatst in een woon- of slaapvertrek is een open keuken, ook als er geen duidelijke afscheiding tussen keukengedeelte en de rest van het vertrek aanwezig is.

> Om een aanrecht in een woon- of slaapvertrek te waarderen als open keuken, moet de ruimte gespecificeerd worden met detailsoortcode `WOK` voor Woonkamer/keuken. Alternatief kan er in de bouwkundige elementen van een `Woonkamer`, `Slaapkamer` of `Woon-/slaapkamer` een bouwkundig element worden gespecificeerd met detailsoortcode `AAN` voor Aanrecht.

## 4.5 Energieprestatie

Een (groot) deel van het totale puntenaantal wordt bepaald door de energieprestatie van de woonruimte. Sinds 2011 speelt het energielabel een rol in het puntenstelsel, waarbi een energielabel of energie-index maximaal 10 jaar geldig is. De energieprestatie kan sinds 1 januari 2021 op drie manieren zin bepaald.

1. Een oud energielabel: registratie heeft plaatsgevonden vóór 1 januari 2015. In 2021 en later lopen veel sinds 1 juli 2011 verstrekte energielabels af, want de geldigheidsduur is tien jaar.
2. De energie-index: registratie op of na 1 januari 2015 tot 1 januari 2021. In 2025 en later lopen veel sinds 1 januari 2015 verstrekte energie-indexen af, want de geldigheidsduur is tien jaar.
3. Het energielabel op basis van primair fossiel energiegebruik: registratie op of na 1 januari 2021.

In [EP-online](https://www.ep-online.nl/) is te vinden wat de energieprestatie van een woning is.

> In de implemenatie is de combinatie `Energieprestatiesoort` met registratiedatum leidend om te beslissen welke lookup tabellen er worden gebruikt om na te gaan hoeveel punten er gegeven moeten worden voor het stelselgroep energieprestatie.

> In de tabellen ter ondersteuning van de tekst van het beleidsboek over de punten toekenning bij een nieuw energielabel is er voor gekozen om de implementatie van regel [4.5.3 Afwijkingsbevoegdheid hogere energielabelklasse dan A++](#453-afwijkingsbevoegdheid-hogere-energielabelklasse-dan-a) al toe te voegen aan de tabellen.

### 4.5.1 Puntentoekenning oud energielabel en energie-index

Bij een oud energielabel bepaalt de labelklasse (A t/m G) het aantal punten dat de verhuurder mag doorrekenen in de maximale huur. Een energielabel dat is geregistreerd vóór 2015 en dat niet ouder is dan tien jaar, is nog bruikbaar. ~~Bij een energie-index is de indeling in letters vervangen door een cijfer. De energie-index wordt meegenomen indien in EP-online staat aangegeven dat de energie-index geldig is voor het woningwaarderingsstelsel.~~

> De energie-index van een energieprestatie wordt niet gebruikt. In EP-Online hebben alle op energie-index gebaseerde energieprestaties ook een labelklasse. Deze labelklasse dient gebruikt te worden voor de waardering.

Zie hieronder de puntentoekenning van de energieprestatie bij een oud energielabel en een energie-index.

| (oude) Energielabel (afgegeven voor 1-1-2025)| Energie-index (afgegeven na 1-1-2025)| Eengezinswoning | Meergezinswoning |
| ----- | ------------- | --------------- | ----------------- |
| A++   | 0-0.6         | 44             | 40               |
| A+    | 0.6-0.8       | 40             | 36               |
| A     | 0.8-1.2       | 36             | 32               |
| B     | 1.2-1.4       | 32             | 28               |
| C     | 1.4-1.8       | 22             | 15               |
| D     | 1.8-2.1       | 14             | 11               |
| E     | 2.1-2.4       | 8              | 5                |
| F     | 2.4-2.7       | 4              | 1                |
| G     | 2.7-          | 0              | 0                |

### 4.5.2 Puntentoekenning nieuw energielabel

Per 1 januari 2021 geldt een nieuwe manier om de energieprestatie van een woonruimte te bepalen met een vernieuwd energielabel. Hierbij wordt gewerkt met een bepalingsmethode (NTA 8800) die een nieuwe indicator heeft voor de energieprestatie (in kWh/m2 per jaar). De uitkomst van de bepalingsmethode (NTA 8800) wordt gereduceerd tot een energielabel (van A++ tot G). Dit label wordt herleid tot punten voor het waarderingsstelsel.  

Aangezien de nieuwe bepalingsmethode tot structurele onderwaardering van de energieprestatie van kleine woningen leidt, wordt er in het kader van het nieuwe energielabel gewerkt met drie klassen met WWS-punten voor de energieprestatie. Dit is afhankelijk van de woninggrootte:

- \< 25 m2
- \> 25 m2 en < 40 m2
- \> 40 m2

> De hier gehanteerde woninggrootte wordt op een andere wijze bepaald dan de gebruiksoppervlakte. Hiervoor is het `EenhedenEnergieprestatie` model uitgebreid met het attribuut `gebruiksoppervlakteThermischeZone` of `gebruiksoppervlakte_thermische_zone` voor de Python representatie. In dit attribuut dient de gebruiksoppervlakte van de thermische zone die gebruikt is bij de registratie van de energieprestatie opgegeven worden.

Voor woningen met een oppervlakte  >= 40 m2 geldt het volgende puntenaantal:

| Label | Eengezinswoning | Meergezinswoning |
| ----- | --------------- | ----------------- |
| A++++ | 52              | 48                |
| A+++  | 48              | 44                |
| A++   | 44              | 40                |
| A+    | 40              | 36                |
| A     | 36              | 32                |
| B     | 32              | 28                |
| C     | 22              | 15                |
| D     | 14              | 11                |
| E     | 8               | 5                 |
| F     | 4               | 1                 |
| G     | 0               | 0                 |

Voor woningen met een oppervlakte >= 25m2 en < 40 m2 geldt het volgende puntenaantal:

| Label | Eengezinswoning | Meergezinswoning |
| ----- | --------------- | ----------------- |
| A++++ | 56              | 52                |
| A+++  | 52              | 48                |
| A++   | 48              | 44                |
| A+    | 44              | 40                |
| A     | 40              | 36                |
| B     | 36              | 32                |
| C     | 32              | 28                |
| D     | 22              | 15                |
| E     | 14              | 11                |
| F     | 4               | 1                 |
| G     | 0               | 0                 |

Voor woningen met een oppervlakte < 25m2 geldt het volgende puntenaantal:

| Label | Eengezinswoning | Meergezinswoning |
| ----- | --------------- | ----------------- |
| A++++ | 60              | 56                |
| A+++  | 56              | 52                |
| A++   | 52              | 48                |
| A+    | 48              | 44                |
| A     | 44              | 40                |
| B     | 40              | 36                |
| C     | 36              | 32                |
| D     | 32              | 28                |
| E     | 22              | 15                |
| F     | 4               | 1                 |
| G     | 0               | 0                 |

### 4.5.3 Afwijkingsbevoegdheid hogere energielabelklasse dan A++

De hierboven vermelde tabellen met de puntentoekenning voor de labelklasse gaan tot A++. Het is mogelijk dat, bij een nieuw energielabel, een betere energielabelklasse dan A++ wordt afgegeven. Een energielabel voor de woonruimte kan tot maximaal A++++ gaan. De Huurcommissie heeft de bevoegdheid gekregen om af te wijken van de hierboven aangegeven puntenwaardering indien de energieprestatie hoort bij een betere energielabelklasse dan A++. Een dergelijke afwijking is uitsluitend mogelijk indien de gemaakte kosten om deze energieprestatie te bereiken, aanmerkelijk afwijken van hetgeen als gangbaar wordt beschouwd, of indien de energieprestatie aanmerkelijk beter is dan hetgeen als gangbaar bij een energielabelklasse A++ wordt beschouwd.  

De Huurcommissie vult deze bevoegdheid als volgt in. Indien sprake is van een A+++ label dan kent de Huurcommissie, 4 extra punten toe, boven op de punten die aan het label A++ worden toegekend. Indien sprake is van een A++++ label dan wordt 8 extra punten toegekend, boven op de punten die worden gegeven voor een label A++. 

### 4.5.4 Bouwjaar bepalend bij geen geldig energielabel of Energie-Index

Indien de energieprestatie van een woonruimte (in de vorm van een energielabel of een energieindex) niet tijdig is vastgesteld, of als de geldigheidsduur van het energielabel is verstreken, dan bepaalt het bouwjaar van de woning het aantal WWS-punten. Een (geldig) energielabel of EnergieIndex wordt door de Huurcommissie in de puntentelling betrokken als deze tijdig beschikbaar is om daarmee rekening te houden in de uitspraak. In geval de opnamedatum van het energielabel of de Energie-Index is gelegen na de relevante peildatum, geldt hierbij als voorwaarde dat de feitelijke toestand (wat energieprestatie betreft) op opnamedatum niet verschilt van de feitelijke toestand op de desbetreffende peildatum. Alleen als er geen verschil is zal de Huurcommissie het energielabel of Energie-Index bij de woningwaardering betrekken. De bewislast ligt bij de verhuurder.  

De puntentelling is in geval het bouwjaar geldt als volgt: 

| Bouwjaar     | Eengezinswoning | Meergezinswoning |
| ------------ | --------------- | ---------------- |
| 2002 en ouder | 36              | 32               |
| 2000 t/m 2001 | 32              | 28               |
| 1998 t/m 1999 | 22              | 15               |
| 1992 t/m 1997 | 22              | 11               |
| 1984 t/m 1991 | 14              | 11               |
| 1979 t/m 1983 | 8               | 5                |
| 1977 t/m 1978 | 4               | 1                |
| 1976 en ouder | 0               | 0                |

### ~~4.5.5 Gerede twijfel energielabel~~

~~Als huurder twijfelt aan de juistheid van het toepasselijke energielabel dan heeft de Huurcommissie de bevoegdheid om een ‘eigen oordeel’ uit te spreken bij gerede twijfel van het energielabel. Een Huurcommissie eigen oordeel (HEO) kan worden uitgesproken indien de huurder met bewijsstukken gemotiveerd aantoont dat sprake is van een verkeerd energielabel/energie-index en dat het gewijzigde energielabel/energie-index van invloed is op de huurprijs. Indien de Huurcommissie tot een eigen oordeel wil komen dan laat de Huurcommissie onderzoeken wat de energieprestatie van de woning is.~~

~~Het eigen oordeel is uitsluitend in de voorliggende zaak van kracht, wordt niet geregistreerd in het register van de Rijksdienst voor Ondernemend Nederland en komt te vervallen na ontbinding van de huurovereenkomst.~~

> Wanneer een eigen oordeel van kracht is, en de waardering daarop gebaseerd moet worden, dient de gewijzigde energieprestatie opgegeven te worden in plaats van de geregistreerde energieprestatie.

### 4.5.6 Energieprestatievergoeding

Voor woningen die zelf (gedeeltelijk) in hun energieverbruik voorzien, door bijvoorbeeld zonnepanelen, kan bij het verhuren een energieprestatievergoeding (EPV) worden afgesproken. De woning zal dan moeten voldoen aan de eisen voor een EPV. Als dit het geval is dan is het aantal punten op basis van het puntenstelsel voor energieprestatie lager. Om te voorkomen dat in de gevallen waarin een energieprestatievergoeding is overeengekomen, de opwekking van energie voor de huurder tevens wordt verdisconteerd in de huurprijs, wordt voor deze woningen een correctiefactor toegepast op het aantal punten voor de energieprestatie. In die gevallen wordt de energieprestatie gewaardeerd met een aantal punten gelijk aan de waardering voor een Energie-Index 1,2 < EI ≤ 1,4 (of Energielabel B), met 32 punten voor een ééngezinswoning en 28 punten voor meergezins- en duplexwoningen.

> Hiervoor is het `EenhedenEnergieprestatie` model uitgebreid met het attribuut `energieprestatievergoeding`. Dit attribuut dient gevuld te zijn met een boolean die aangeeft of er bij het verhuren een energieprestatievergoeding (EPV) is overeengekomen.

## 4.6 Keuken

Het woningwaarderingsstelsel kent aan een zelfstandige woonruimte punten toe voor het onderdeel keukeninstallatie. Het woningwaarderingsstelsel geeft dus, naast punten voor de oppervlakte van de keuken (zijnde een vertrek, zie hiervoor onder [4.2.1](#421-wat-zijn-vertrekken)) ook punten voor de keukeninstallatie. Er zijn door de wetgever wel eisen gesteld om aan zo’n keukeninstallatie punten te mogen toekennen. En ook heeft de wetgever bepaald aan de hand waarvan je tot puntentoekenning komt. Hieronder wordt uiteengezet aan welke eisen moet zijn voldaan om punten aan een keukeninstallatie toe te kennen en op welke manier je de punten moet berekenen ([4.6.1](#461-voorzieningen-keuken)). Ook wordt besproken wanneer er extra kwaliteitspunten worden toegekend, welke keukenvoorzieningen daarvoor in aanmerking komen ([4.6.2](#462-voorzieningen-die-extra-kwaliteitspunten-opleveren)).

### 4.6.1 Voorzieningen keuken

Het woningwaarderingsstelsel geeft, naast punten voor de oppervlakte van het vertrek, ook punten voor de keukeninstallatie van zo’n vertrek.

**Keukeninstallatie?**  
Om punten vanwege de keukeninstallatie toe te kennen, moet het wel gaan om een inrichting van het vertrek dat als keukeninstallatie moet worden beschouwd. Daarvoor is in ieder geval vereist dat er een aanrecht aanwezig is. Zonder aanrecht spreken we niet van een keukeninstallatie. Aanvullend geldt nog dat de keuken voorzien moet zijn van een aan- en afvoer van water. Verder moet de keuken tenminste één aansluitpunt voor koken op gas of elektriciteit hebben. En het aanrecht moet zijn voorzien van minimaal twee onderkasten (met laden, deuren of schuiven).  

In geval aan deze eisen niet wordt voldaan, is er geen sprake van een keukeninstallatie in de zin van het woningwaarderingsstelsel en worden er dus geen punten voor keukeninstallatie gerekend, ongeacht de lengte van het aanrecht (zie hierna). Ook kom je dan niet toe aan extra punten vanwege de kwaliteit van de voorzieningen als bedoeld in paragraaf [4.6.2](#462-voorzieningen-die-extra-kwaliteitspunten-opleveren).

#### Punten: lengte van het aanrecht

Uitgangspunt voor de waardering van de keukeninstallatie is de lengte van het aanrecht:

- Is de lengte van het aanrecht minder dan 1 meter, dan worden er geen punten toegekend.
- Is de lengte van het aanrecht tussen de 1 en 2 meter, dan worden er 4 punten toegekend.
- Is de lengte van het aanrecht 2 meter of langer, dan worden er 7 punten toegekend.

De lengte van het aanrecht moet over midden van het bovenblad worden gemeten. Daarbij moeten de ingebouwde spoelbakken worden meegeteld. Ingebouwde kookplaten worden niet meegeteld.  

Een aanrecht met spoelbak, waarvan de lengte minder bedraagt dan 1 meter, voldoet dus niet aan de eis van 1 meter en wordt daarom niet als aanrecht gewaardeerd, maar als wastafel. Een aanrecht zonder onderkasten wordt gewaardeerd als een wastafel.  

Indien een aanrechtblad langer is dan de aanwezige onderkasten met de bedoeling dat er onder het langere gedeelte van het aanrechtblad een losstaande koelkast, vaatwasser, wasmachine e.d., kan worden geplaatst, dan wordt dit gedeelte van het aanrechtblad mee gemeten mits er onder het blad aansluitmogelijkheden aanwezig zijn voor genoemde apparatuur.  

Een ingebouwde (onroerende) koelkast, vaatwasser en/of oven beschouwen we als onderkast, mits daarnaast voldoende vervangende (andere) kastruimte aanwezig is.

Indien er sprake is van onderbouwapparatuur (roerend), dan kan dit niet in de plaats van een onderkast worden gesteld en dient er voldoende vervangende (andere) kastruimte aanwezig te zijn. Een kastruimte in de vorm van een plank kan niet als zodanig worden aangemerkt.

### ~~4.6.2 Voorzieningen die extra kwaliteitspunten opleveren~~

> Er is gekozen om de extra kwaliteitspunten niet te implementeren aangezien veel elemeten niet gemodelleerd zijn in het huidige VERA model.

~~Het woningwaarderingsstelsel kent de mogelijkheid om extra kwaliteitspunten te rekenen in geval de afwerking van de keuken daartoe aanleiding geeft. De extra kwaliteitspunten zijn een gestandaardiseerde invulling van de bevoegdheid van de Huurcommissie om investeringen ten behoeve van extra kwaliteit met extra punten te waarderen, tot maximaal het aantal punten dat reeds op grond van de aanrechtlengte is bepaald.~~

~~De Huurcommissie kent extra kwaliteitspunten toe als de keukenuitrusting uitstijgt boven het minimale niveau, te weten:~~
~~- een aanrechtblad met een lengte van minimaal 1 m (lengte incl. spoelbakken, exclusief afzuig installaties en inbouwkookplaten (tenzij 2-pits));~~
~~- én 2 kasten (onder of boven of staande);~~
~~- én wandtegelwerk of andersoortige waterdichte afwerking boven het aanrechtblad en in de kookhoek vanaf de vloer tot een hoogte van minimaal 1,5 m.~~

~~Indien de keukenuitrusting en/of -afwerking boven het minimale niveau uitstijgt, is de waardering als volgt. Hierna wordt de voorziening genoemd met aansluitend het aantal extra punten.~~

| Voorziening                                               | Aantal punten |
|-----------------------------------------------------------|---------------|
| inbouw kookplaat (gas/elektrisch)                         | 0,5           |
| inbouw kookplaat 5 of 6 pits luxe uitvoering (RVS e.d.)   | 0,75          |
| inbouw keramische kookplaat                               | 1,25          |
| inbouw inductiekookplaat                                  | 1,50          |
| inbouw oven (gas/elektrisch) of magnetron                 | 0,75          |
| inbouw combi oven/magnetron                               | 1,5           |
| inbouw oven inclusief kookplaat (gas/elektrisch)          | 1,25          |
| inbouw magnetron                                          | 0,75          |
| (inbouw) afzuigkap                                        | 0,5           |
| (inbouw) luxe uitgevoerde afzuigkap of wasemkap           | 0,75          |
| inbouw koelkast                                           | 0,75          |
| inbouw vrieskist of -kast                                 | 0,5           |
| inbouw vries/koelcombinatie                               | 1,25          |
| inbouw vaatwasmachine                                     | 1,25          |
| luxe mengkraan (bv. éénhandsbediening)                    | 0,25          |
| thermostatische watermengkraan                            | 0,5           |
| dubbele spoelbak                                          | 0,25          |
| extra wandbetegeling per 2 m2                             | 0,25          |
| vloertegels per 2 m2                                      | 0,25          |
| extra enkele kast *                                       | 0,25          |
| extra dubbele kast *                                      | 0,5           |

~~*Als er meer dan 6 kasten aanwezig zijn (enkele kasten van min. 50-60 cm breed) dan wordt per extra kastruimte 0,25 punt extra toegekend, tenzij het om vervangende kastruimte gaat voor de door inbouwapparatuur in beslag genomen ruimte.~~

~~Algehele luxe uitvoering (hardhouten of natuurstenen aanrechtblad, massief houten frontjes, ingebouwde verlichting, luxe wand, vloer en of plafondafwerking: ten hoogste 2 punten).~~

~~NB.: Een luxe uitvoering of ingebouwde voorziening/ apparatuur komt voor extra punten in aanmerking, ongeacht de onderhoudstoestand daarvan. Als de kosten van desbetreffende voorziening/ apparatuur aanzienlijk hoger zijn dan de kosten, die als basis voor bovengenoemde normering zijn gehanteerd, dan blijft een afwijkende puntentelling mogelijk. In beginsel wordt altijd uitgegaan van de waardering conform bovenstaande lijst.~~

~~Onder extra kastruimte wordt verstaan: elk gefixeerd element behorende tot de keuken/ het keukenblok, voorzien van een kastdeur, klep of lade én ongeacht de hoogte en breedte. Een element met twee deuren (bv. een hoekcarrousel) wordt als dubbele kast aangemerkt. Een element voorzien van laden wordt gewaardeerd als kast. Kastruimte boven een afzuigkap, waardoor het (lucht)afvoerkanaal verloopt, wordt meegeteld als volwaardige kastruimte.~~

## 4.7 Sanitair

Het woningwaarderingsstelsel kent aan een zelfstandige woonruimte punten toe voor het onderdeel sanitair. De waardering van het sanitair wordt bepaald op grond van de aanwezigheid van bepaalde voorzieningen binnen de woning. Hieronder wordt uiteengezet aan welke sanitaire voorzieningen punten worden toegekend en hoeveel punten die voorzieningen krijgen. Ook wordt besproken wanneer er extra kwaliteitspunten worden toegekend aan deze sanitaire voorzieningen.


### 4.7.1 Sanitaire voorzieningen

Het woningwaarderingsstelsel geeft punten aan de sanitaire voorzieningen toilet, wastafel, bad en douche. De puntentoekenning is als volgt:  
| Voorziening | Punten |
| -------- | -------- |
| toilet   | 3   |
| wastafel  | 1  |
| bidet    | 1  |
| lavet*   | 1  |
| douche   | 4  |
| bad      | 6  |
| bad en douche | 7  |

> De punten hierboven in de tabel zijn het aantal punten dat wordt toegekend aan de sanitaire voorziening. De gedetailleerde voorwaarden die hieronder volgen in het beleidsboek worden niet getoetst in de implementatie. Het is aan de gebruiker om alleen voorzieningen op te geven die voldoen aan de voorwaarden.

~~_*Een lavet wordt met vier punten gewaardeerd, als deze is voorzien van aansluitpunten voor warm en koud water én van douchegarnituur._~~

**Toilet**  
Drie punten worden toegekend aan een toilet ~~met waterspoeling als het toilet is geplaatst in een daartoe bestemde ruimte en als het toilet binnen het woongebouw is gelegen. Wanneer sprake is van een toilet dat buiten de woning maar binnen het woongebouw is gelegen, dan geldt dat het toilet in de waardering wordt meegenomen als het gebruik van het toilet door derden is uit te sluiten.~~  

**Wastafel**  
Wastafels worden met één punt gewaardeerd. ~~Als wastafels worden alle bakken geteld voor wassen en spoelen die op de waterleiding én op het huisriool zijn aangesloten. Een dergelijke bak wordt niet als wastafel gewaardeerd indien boven de bak een douche is aangebracht. Een bad en spoelbakken in een keukenaanrecht worden niet als wastafels gewaardeerd.~~ 

~~Als wastafel waardeert de Huurcommissie een fonteintje en een aanrecht dat niet voor punten in aanmerking komt, waarvan de aanrechtlengte korter is dan één meter.~~

**Bad en douche**  
Douches worden gewaardeerd met vier punten. ~~Als douche wordt meegeteld iedere door de verhuurder aangebrachte installatie voor het nemen van een stortbad. Hieronder valt eveneens een zogenaamde douchecabine, die voldoet aan bovengenoemde voorwaarden, als de douchecabine in een vertrek (anders dan bad- of doucheruimte) of overige ruimte is geplaatst. De oppervlakte van dat vertrek of van die overige ruimte wordt in dat geval niet verminderd met de door de douchecabine ingenomen oppervlakte.~~  

Aan baden worden zes punten toegekend, ~~ongeacht de lengte van het bad. Indien een bad is voorzien van een (hand)douche, dan wordt het douchegarnituur niet afzonderlijk geteld.~~  

Indien in de badruimte behalve het bad tevens een afzonderlijke douche is aangebracht, geldt een waardering van zeven punten.  

> Het is ambigu hoeveel punten er zouden moeten worden toegekend indien een badruimte meer dan één douche bevat en één bad of vice versa. I.v.m. de onwaarschijnlijkheid van het voortkomen van deze situatie is er gekozen om deze situatie niet te ondersteunen in de implementatie. Indien er een bad en een douche in dezelfde ruimte aanwezig zijn worden er 7 punten toegekend per combinatie van bad en douche.  
>
> Oftewel:
>
> - één bad en één douche in dezelfde ruimte: 7 punten  
> - één bad en twee douches in dezelfde ruimte: 7 punten
> - twee baden en één douche in dezelfde ruimte: 7 punten
> - twee baden en twee douches in dezelfde ruimte: 14 punten

~~**Voorzieningen in een bad- en doucheruimte**~~  
~~Indien sprake is van sanitaire voorzieningen in een bad- of doucheruimte[^24], dan worden alleen punten toegekend aan die voorzieningen indien de bad -of doucheruimte voldoet aan drie voorwaarden. Ten eerste moet de wand- en vloerafwerking van de bad- of douchruimte voldoende waterdicht zijn. Een bad in een vertrek met een niet-waterdichte vloer wordt door de Huurcommissie wel gewaardeerd, omdat het bad zelf als een waterdichte afwerking wordt gezien. Ten tweede moet de bad- en doucheruimte zijn voorzien van aansluitingspunten voor warm en koud water. Met aansluitingspunten voor warm en koud water wordt niet een warmwater apparaat bedoeld. Als sprake is van een geiser of boiler dan hoeven deze niet door de verhuurder te zijn verstrekt. Ten derde moet het bad of de douche zijn voorzien van douchegarnituur. Met douchegarnituur bedoelt de Huurcommissie een warm- en koudwaterkraan of een mengkraan. Indien het aansluitpunt voor warm en koud water bedoeld is voor gecombineerd gebruik van zowel een wastafel als de naastgelegen douche of bad (bijvoorbeeld door middel van een zogenaamde zwenkarm), dan wordt uitsluitend de douche of het bad gewaardeerd. Dus niet én 1 punt voor wastafel én 4 of 6 punten voor douche of lavet, respectievelijk bad. Indien in de bad- of doucheruimte een toilet is geplaatst wordt dit toilet volledig gewaardeerd met drie punten.~~

### ~~4.7.2	 Voorzieningen die extra kwaliteitspunten opleveren~~

> Er is gekozen om de extra kwaliteitspunten niet te implementeren aangezien veel elemeten niet gemodelleerd zijn in het huidige VERA model.

~~Extra kwaliteitspunten kunnen worden toegekend indien het sanitair en/of de afwerking van de bad- of doucheruimte een kwaliteitsniveau heeft dat, op het moment van de woningwaardering[^25], het gangbare kwaliteitsniveau van sociale huurwoningen overschrijdt. Met het gangbare kwaliteitsniveau bedoelt de Huurcommissie het kwaliteit-/uitrustingsniveau van nieuwe socialehuurwoningen (niet ouder dan vijf jaar). In dit verband In dit verband heeft de bad- en/of doucheruimte van een nieuwe sociale huurwoning de volgende kenmerken:~~

- ~~een waterdichte vloerafwerking;~~
- ~~betegeling rondom tot resp. 1,50 m hoogte voor badruimte en 1,80 m voor doucheruimte;~~
- ~~en wastafel inclusief mengkraan met spiegel en planchet én;~~
- ~~een douche of bad met aansluitpunten voor warm en koud water en voorzien van douchegarnituur.~~

[^24]: De Huurcommissie verstaat onder een bad-/doucheruimte een (afzonderlijke) ruimte met een vrije hoogte van ten minste 2 meter, gemeten vanaf de vloer tot aan het zichtbare plafond. Daarin dient tenminste aanwezig te zijn een wastafel of een douche of een bad. Voor een gecombineerde bad-/douche- en toiletruimte geldt, vanwege de oppervlakteeis voor toilet- ruimten, een minimale oppervlakte van 0,64 m2 . Indien een douche- of badruimte, eventueel gecombineerd met een toilet, niet een vrije hoogte heeft van 2,00 m, dan wordt de ruimte gewaardeerd als overige ruimte.  

~~[^25]: Zie hoofdstuk 3 van dit beleidsboek voor de peildatum per procedure ten aanzien van de woningwaardering.~~

~~Er kunnen extra kwaliteitspunten worden toegekend tot maximaal het aantal punten dat reeds voor de douche en/of bad is bepaald. Anders gezegd: maximaal een verdubbeling van de toegekende kwaliteitspunten voor douche en/of bad kan plaatsvinden.~~

#### ~~Voorzieningen die extra kwaliteitspunten opleveren~~

~~De Huurcommissie heeft een aantal voorzieningen aangewezen die extra kwaliteitspunten opleveren, aangezien hiermee het kwaliteitsniveau van het sanitair en/of de afwerking van de bad- of doucheruimte het gangbare bij sociale huurwoningen overstijgt. De onderhoudstoestand van de desbetreffende voorziening of apparatuur is niet relevant of extra kwaliteitspunten worden toegekend.~~

| Voorziening                                               | Aantal punten           |
|-----------------------------------------------------------|-------------------------|
| extra wandbetegeling                                      | 0,25 (per 2 m2)         |
| kastje, waarin ingebouwd een wastafel                     | 0,25                    |
| toiletkastje met ingebouwde verlichting                   | 0,25                    |
| extra voor een bubbelbad (whirlpool)                      | 2                       |
| luxe mengkraan (bv. éénhandsbediening)                    | 0,25                    |
| thermostatische watermengkraan                            | 0,5                     |
| douchewand of douchecabine (glas of kunststof)            | 1                       |
| wandcloset/ zwevend toilet (met inbouwreservoir)          | 0,5                     |
| design-/handdoekradiator                                  | 0,25                    |

~~Een algehele luxe uitvoering van de bad- of doucheruimte (luxe plafondafwerking, vloer- of wandafwerking van reliëf- of natuursteen, ingebouwde verlichting, etc.) levert ten hoogste twee punten op.~~

~~Indien een (pantry) keukenblok van <1 m, met inbouwapparatuur, als wastafel is gewaardeerd dan levert dit maximaal vier extra kwaliteitspunten op.~~
