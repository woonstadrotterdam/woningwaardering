# 2024. Zelfstandige Woonruimten

## 4.2 Oppervlakte van Vertrekken

### 4.2.1 Wat zijn vertrekken?

Het eerste onderdeel van de woningwaardering is de oppervlakte van vertrekken. Onder vertrek-
ken worden woonkamer, andere kamers (hobbykamer, studeerkamer, slaapkamer en eetkamer),
keuken, badkamer of doucheruimte verstaan. De waardering van vertrekken is 1 punt per m2.

Geen vertrekken zijn: schuren, zolderberging, kelders, wasruimten, bijkeukens, garages en bergingen,
gang, (speel)hal en zogenoemde verkeersruimten (bijvoorbeeld overlopen). De oppervlakte van
deze ruimten tellen dus niet mee als vertrekken.
De Huurcommissie geeft op een aantal punten nadere invulling aan de hierboven genoemde
wettelijke begrippen. Dat wordt hierna beschreven.

**Woonkamer of andere kamer**

Een woonkamer of een andere kamer is dus een vertrek in de zin van het
woningwaarderingsstelsel.

Hiervan is alleen sprake als:

- ~~De vloer begaanbaar is.~~
- ~~De muren en wanden uit vast materiaal bestaan.~~
- ~~En de daglichttoetreding, de ventilatiemogelijkheid en het aantal elektrische lichtpunten in overeenstemming zijn met de geldende verkeersopvattingen.~~
- De ruimte een oppervlakte heeft van minimaal 4 m2.
- ~~De ruimte over de volle lengte ten minste 1,50 m breed is.~~
- ~~De ruimte over ten minste 50% van de oppervlakte een vrije hoogte heeft van 2.10 m (gemeten
  vanaf de vloer tot het zichtbare plafond).~~

Alleen als aan al deze eisen is voldaan, wordt de (oppervlakte van de) woonruimte of andere
kamer meegeteld als “vertrek”. Zo niet, dan wordt de oppervlakte meegeteld als “overige ruimte”
(zie paragraaf 4.3.).
Uitzondering hierop geldt voor de keuken: de eisen van minimaal 4 m2 en ~~minimaal 1,50 m
breedte~~ gelden niet voor de keuken en verzetten zich er dus niet tegen om een keuken als “vertrek” aan te merken en overeenkomstig te waarderen.

**Badkamer of doucheruimte**

Een badkamer of doucheruimte is dus een vertrek in de zin van het woningwaarderingsstelsel.

Hiervan is alleen sprake als:

- ~~De vloer begaanbaar is.~~
- ~~De muren en wanden uit vast materiaal bestaan.~~
- ~~En de ventilatiemogelijkheid en het aantal elektrische lichtpunten in overeenstemming zijn met
  de geldende verkeersopvattingen.~~
- ~~De ruimte over ten minste 50% van de oppervlakte een vrije hoogte heeft van 2,00 m. (gemeten vanaf de vloer tot het zichtbare plafond).~~

~~Alleen als aan al deze eisen is voldaan, wordt de (oppervlakte van de) badkamer of doucheruimte
meegeteld als “vertrek”. Zo niet, dan wordt de oppervlakte meegeteld als “overige ruimte” (zie
verderop).~~

> Hoewel de VERA-standaard een onderscheid maakt tussen badkamer, doucheruimte en badkamer/toilet (badkamer met toilet) beschouwen wij ieder van deze ruimtes indien zij een toilet bevatten als een badkamer met toilet, conform hoe de huurcommissie omgaat met deze ruimtes.. Zie ook [dit Github issue](https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/96).

Voor gecombineerde bad-/doucheruimte met toilet geldt een minimale oppervlakte van 0,64 m².

> Elke Badkamer, Badkamer/toilet of Doucheruimte die als vertrek is aangemerkt wordt meegeteld als vertrek, tenzij onder aftrek van 1 m2 voor een in de ruimte geplaatst toilet de oppervlakte kleiner is dan 0,64 m². (Zie punt 5 in 4.2.2).

**Zolderruimte**

Zolderruimten zijn in het algemeen “overige ruimte”. Echter, in geval een zolderruimte een functie
heeft als “vertrek” (dus woonkamer, andere kamers, badkamer of doucheruimte), en ook voldoet
aan de eisen die daarvoor gelden (zie hierboven), dan mag de zolderruimte meetellen als “vertrek”,
mits deze ruimte bereikbaar is via een vaste trap ~~en het dak beschoten is~~.

> In het beleidsboek wordt er onderscheid gemaakt tussen een zolder vertrek met een vaste trap of zolder met een ander soort trap. Wanneer een zolder als vertrek wordt aangemerkt moet deze te bereiken zijn via een vaste trap. Daarom wordt er voor een zolder gekeken of er een vaste trap in de `bouwkundige_elementen` zit. Als dit het geval is dan telt de gehele oppervlakte van de zolder mee voor de punten van Oppervlakte van Vertrekken.

### 4.2.2 Hoe wordt de oppervlakte van vertrekken gemeten?

De wetgever heeft in de toelichting op het woningwaarderingsstelsel een aantal meetinstructies
meegegeven:

1. Meting van de oppervlakte van vertrekken vindt plaats ~~van muur tot muur, op een hoogte van
   1,50 m boven de vloer,~~ inclusief de oppervlakte van alle tot de woning behorende losse en
   vaste kasten (kleiner dan 2m²). ~~Deze meethoogte geldt ook als de oppervlakte afwijkt van die
   op vloerniveau.~~

De Huurcommissie hanteert hierbij de volgende uitgangspunten.

~~Als er sprake is van een pui wordt de binnenzijde van die pui (het kozijn) genomen. Een erker
wordt meegerekend indien deze inwendig een vrije hoogte heeft van ten minste 1,50 m. Indien er
sprake is van een zgn. entresol (tussenverdieping) dan dient de oppervlakte onder en/of boven
deze entresol te worden meegerekend, indien de vrije hoogte ten minste 1,50m bedraagt.~~ Voor
het meten van vertrekken die met elkaar in open verbinding staan, zie verderop.
“Alle tot de woning behorende losse en vaste kasten” lees de Huurcommissie als: “alle tot de
vertrekken behorende kasten”. De plaats van de deur van de kast bepaalt bij welk vertrek de kast
behoort. Dus een kast die in een vertrek uitkomt wordt, ongeacht de afmeting, bij dat vertrek
geteld. Dat geldt ook voor het waarderen van een kastenwand tussen twee vertrekken.

- Van vaste kasten (kleiner dan 2m²) wordt de netto oppervlakte bepaald en bij de oppervlakte
  van het betreffende vertrek opgeteld;
- Een kast, (kleiner dan 2m²) waarvan de deur uitkomt op een verkeersruimte, wordt niet
  gewaardeerd;
- Losse kasten zijn niet van belang bij het meten. De oppervlakte van het vertrek wordt bepaald,
  incl. de oppervlakte die wordt ingenomen door een losse kast;

> Binnen het woningwaarderingsstelsel mag onder bepaalde voorwaarden de oppervlakte van vaste kasten worden opgeteld bij de ruimte waar de deur van de kast zich bevindt. Als hier bij het inmeten geen rekening mee gehouden is, kan het attribuut `verbonden_ruimten` gebruikt worden om de met een ruimte verbonden vaste kasten mee te laten nemen in de waardering. Hiervoor is de VERA referentiedata binnen deze repository uitgebreid met ruimtedetailsoort Kast, code KAS.

2. ~~Als oppervlakte van een vertrek met een (ten dele) hellend of verlaagd plafond geldt dat
   alleen het gedeelte waarboven het plafond ten minste 1,50m hoog is wordt meegeteld bij de
   berekening van de oppervlakte.~~

~~De Huurcommissie eist in geval van een (ten dele) hellend plafond dat de 1,50m-hoogte loopt tot
het dakbeschot of tot het zichtbare dakvlak of plafond. Met gordingen en balken wordt bij de
meting geen rekening gehouden.~~

3. ~~De vloeroppervlakte onder aanrechten, toestellen in de keuken, badkuip, lavet of douchebak,
   moederhaard, c.v.-ketel en boilerinstallatie, wordt meegeteld.~~

~~De Huurcommissie gaat hier als volgt mee om. Indien zich in een vertrek, of in een kast in een
vertrek, een gas- en/of elektrameter bevindt, dan wordt de oppervlakte gewaardeerd onder aftrek
van 30 x 60 cm (minimale afmeting meterkast bestaande bouw).
De vloeroppervlakte onder radiatoren wordt meegeteld.~~

4. ~~De oppervlakte die wordt ingenomen door schoorsteenkanalen, ventilatiekanalen of stand- of
   grondleidingen (tenzij horizontale leidingen, zie hierna) wordt niet meegeteld.~~

~~Bij een schoorsteenmantel en/of rookkanaal (die naar boven of beneden breed kan uitlopen) is de
oppervlakte op 1,50m-hoogte bepalend. De oppervlakte die wordt ingenomen door standleidin-
gen (verticale leidingen) wordt niet meegeteld.
De oppervlakte die wordt ingenomen door grondleidingen (horizontale leidingen), wordt wel
meegeteld.~~

5. Indien een toilet in een badruimte of doucheruimte is geplaatst, wordt de oppervlakte van die
   ruimte met één vierkante meter verminderd.

6. ~~Van de oppervlakte onder een open dan wel gesloten vaste trap geldt dat gedeelte waar de
   ruimte tussen vloer en onderkant trap ten minste 1,50m hoog is.~~

7. Afronding van de oppervlakte op hele vierkante meters vindt plaats na saldering van de
   oppervlakte van alle vertrekken; bij 0,5m² of meer wordt afgerond naar boven, bij minder dan
   0,5m² naar beneden. Waardering in punten vindt na saldering en afronding plaats.

De Huurcommissie licht dit als volgt toe:
Afronding: eerst de oppervlakte per vertrek op 2 decimalen afronden en pas daarna de oppervlak-
te van alle vertrekken salderen en afronden op hele vierkante meters.

**Voorbeeld:**  
kamer : lengte 3,76m x breedte 4,12m = 15,4912 m², afgerond : 15,49 m²  
keuken: lengte 2,95m x breedte 3,81m = 11,2395 m², afgerond : 11,24 m²  
Totaal : 26,73 m² Afronding op hele m² : 27 m².

8. ~~Twee vertrekken die met elkaar in verbinding staan, worden in een bepaald geval als één
   vertrek gewaardeerd. Dit is het geval als zich tussen die twee vertrekken een opening bevindt,
   die breder is dan 50% van de muur, waarin deze opening zich bevindt (zie schets hieronder).
   Het moet hierbij gaan om een niet afsluitbare opening, die doorloopt tot aan de vloer. De muur
   wordt gemeten in het vertrek, waarin de tussenwand het smalst is.~~


### 4.3.2 Hoe wordt de oppervlakte van overige ruimte gemeten?
De wetgever heeft een aantal eisen en meetinstructies meegegeven:
1. ~~De ruimten worden slechts als “overige oppervlakte” gewaardeerd, als de vloer begaanbaar is.~~
   
2. ~~Van de overige ruimten wordt de gehele oppervlakte gemeten, dus zonder aftrek van loop- of
verkeersruimte. De oppervlakte van een trapgat wordt wel in mindering gebracht. De oppervlakte die een uitschuifbare of opvouwbare trap in gesloten toestand inneemt, wordt van de
oppervlakte van de ruimte afgetrokken.~~

3. ~~Meting van de oppervlakte vindt plaats van muur tot muur, op een hoogte van 1,50m boven
de vloer. En ook inclusief de oppervlakte van de moederhaard, CV-ketel en boilerinstallatie.
Maar niet: de oppervlakte die wordt ingenomen door schoorsteenkanalen, ventilatiekanalen of
stand- of grondleidingen.~~

~~De Huurcommissie meet als er sprake is van een pui, vanaf de binnenzijde van die pui (het kozijn).
Ook een erker, die inwendig een vrije hoogte heeft van ten minste 1,50m, telt mee. De oppervlakte
onder en/of boven een zogenaamde entresol (tussenverdieping) wordt meegerekend, indien de
hoogte minstens 1,50m bedraagt.~~

~~De Huurcommissie berekent de hoogte van 1,50 meter door te meten tot het dakbeschot, het
zichtbare dakvlak of plafond (gordingen en balken blijven buiten de meting).~~

4. Ook de oppervlakte van alle tot de woning behorende losse en vaste kasten (kleiner dan 2m²)
wordt meegerekend.

Losse kasten zijn niet van belang bij het meten. De oppervlakte van de overige ruimte wordt
bepaald, incl. de oppervlakte die wordt ingenomen door een losse kast.
Van vaste kasten (kleiner dan 2m²) die uitkomen in een wel gewaardeerde overige ruimte wordt
de netto oppervlakte bepaald en bij de oppervlakte opgeteld.
Een kast, (kleiner dan 2m²) waarvan de deur uitkomt op een verkeersruimte, wordt niet
gewaardeerd.

~~Indien zich in een overige ruimte, of een kast in een overige ruimte, een gas- en/of elektrameter
bevindt, dan wordt de oppervlakte gewaardeerd onder aftrek van 30 x 60 cm (minimale afmeting
meterkast bestaande bouw).~~

5. ~~De Huurcommissie telt de vloeroppervlakte onder radiatoren ook mee.~~  

~~Voor een schoorsteenmantel en/of rookkanaal (die naar boven of beneden breed kan uitlopen)
vindt de Huurcommissie de oppervlakte op 1,50m-hoogte bepalend.~~

6. ~~Van de oppervlakte onder een vaste (open of gesloten) trap, telt mee dat gedeelte waar de
ruimte tussen vloer en onderkant trap ten minste 1,50m hoog is.~~

7. ~~De oppervlakte die door een in ingeschoven toestand liggende inschuifbare of opvouwbare
trap wordt ingenomen, wordt niet meegeteld.~~

8. Betreft het een zolderberging dan wordt ~~, naast de eis van een begaanbare vloer,~~ als voor-
waarde gesteld, ~~dat het dak beschoten is en~~ dat de zolderruimte via een tot de woning
behorende trap bereikbaar is. Indien aan deze voorwaarden niet is voldaan, tellen zolderber-
gingen bij de woningwaardering niet mee.

Indien geen vaste trap aanwezig is, wordt het aantal punten van de vloeroppervlakte van de
zolderruimte met 5 verminderd, doch niet met meer punten dan voor de oppervlakte van de
zolderruimten wordt gegeven.

~~Is er op de zolderverdieping ook nog een vertrek aanwezig dat alleen bereikbaar is via het zolder-
gedeelte dan wordt de oppervlakte van het zoldergedeelte verminderd met de loopruimte om het
vertrek te bereiken. De dan resterende zolderoppervlakte dient minimaal 2 m2 te bedragen en
wordt dan gewaardeerd als overige ruimte.~~

> Wanneer een zolder als overige ruimte wordt beschouwd, kijken we in de `bouwkundige_elementen` van de zolder of de zolder bereikbaar is via een trap. Wanneer deze bereikbaar is via een vaste trap telt de volledige oppervlakte mee voor de punten berekening van Oppervlakte van Overige ruimten.
Wanneer deze wel bereikbaar is, maar niet via een vaste trap, moeten er 5 punten in mindering worden gebracht omdat de ruimte niet bereikt kan worden met een vaste trap. In onze implementatie hebben wij er voor gekozen om te checken of er dan wel een vlizotrap aanwezig is in de `bouwkundige_elementen`, aangezien dit de enige andere soort trap in het VERA model is waarmee een zolder ruimte bereikt zou kunnen worden.
Daarnaast is het onze keuze om de 5 punten in mindering te brengen door de oppervlakte van de zolder te corrigeren. Het beleidsboek
geeft aan dat de punten in mindering gebracht moeten worden
op de punten berekend voor deze ruimte. Maar ook dat punten
pas berekend moeten worden wanneer de totale oppervlakte van een eenheid bekend is en afgerond is.
Dit is tegenstrijdig en daarom kiezen wij de implementatie die volgens ons het beleidsboek zo goed mogelijk benadert.
Let op, door de afronding komt deze berekening niet helemaal juist
uit, maar dit is de benadering waar wij nu voor kiezen.

9. Een overloop is een verkeersruimte en wordt dus niet gewaardeerd. ~~Als er met aftrek van de
verkeersruimte en trap voldoende ruimte overblijft en deze (zolder)overloop kennelijk ook
bedoeld is als bergruimte, dan wordt deze ruimte wel gewaardeerd.~~

10. Gemeenschappelijke bergingen worden gewaardeerd als overige ruimte als:
- ~~zij binnen het woongebouw liggen of tot de onroerende aanhorigheden behoren;~~
- ~~de vergoeding daarvoor in de huurprijs van de woning is begrepen;~~
- de oppervlakte, na deling door het aantal woningen, per woning minstens 2m2 bedraagt.

> Hiervoor is het `EenhedenRuimte` model uitgebreid met het attribuut `gedeeldMetAantalEenheden` (of `gedeeld_met_aantal_eenheden` voor de Python representatie). Om deze berekening correct uit te voeren dient deze waarde gevuld te zijn. Zonder deze waarde wordt de volledige oppervlakte van een ruimte meegeteld.

De toekenning van punten bij een gemeenschappelijke berging is als volgt: totale oppervlakte,
afronden in m2, delen door het aantal woningen en waarderen als “overige ruimte”. Kasten <2m2
en uitkomend in een verkeersruimte worden niet meegeteld.

11.  Afronding van de oppervlakte op hele vierkante meters vindt plaats na saldering van de
oppervlakte van alle afzonderlijke ruimten; bij 0,5m² of meer wordt afgerond naar boven, bij
minder dan 0,5m² naar beneden. Waardering in punten vindt na saldering en afronding plaats.

De Huurcommissie licht dit als volgt toe:
Afronding: eerst de oppervlakte per overige ruimte op 2 decimalen afronden en pas daarna de
oppervlakte van alle overige ruimten salderen en afronden op hele vierkante meters.

**Voorbeeld:**  
Garage : lengte 3,16m x breedte 6,12m = 19,3392 m², afgerond : 19,34 m²  
Bijkeuken: lengte 2,11m x breedte 2,87m = 6,0557 m², afgerond : 6,06 m²  
Totaal : 25,40 m² Afronding op hele m² : 25 m².  

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