# Voor En Na

Een issue (onder **Huidig en voorgesteld gedrag**) en een PR (onder **Samenvatting**) tonen per situatie de punten voor en na de wijziging:

- Verandert per situatie één getal en past de situatie in een paar woorden, maak dan één tabel met per situatie één rij: een letter, de situatie, voor en na. Zet de tests in een lijst onder de tabel, elk met de letter van zijn situatie.
- Verandert per situatie meer dan één getal, of moet de lezer de rekenstappen kennen om de uitkomst te begrijpen, geef dan elke situatie een eigen blok: een vette kop die de situatie noemt, de rekenstappen in een paar korte zinnen, een tabel met de rijen Voor en Na en een kolom per getal dat verandert, en de test. Zet situaties zonder wijziging daaronder in een lijst, elk met de uitkomst en de test.
- Zet in elke cel één getal. Zet een gewijzigd getal vet.
- Zet per situatie de uitkomst van de huurprijscheck (skill `huurprijscheck`) in de tabel: in één tabel een kolom Huurprijscheck, in een blok een rij Huurprijscheck onder Voor en Na. Schrijf per cel "gelijk", het getal van de huurprijscheck, of "niet te toetsen" als de huurprijscheck de input niet kan uitdrukken. Licht alleen een getal of "niet te toetsen" toe, in één of twee zinnen: onder de tabel van het blok, of bij de test in de lijst. In de lijst met situaties zonder wijziging is de uitkomst een korte zin. Noem boven het overzicht de datum en het tijdvak van de meting.
- Noem de huurprijs alleen als de wijziging de huurprijs zelf raakt: de huurprijstabel of een opslag. In andere gevallen volgt de huurprijs uit het puntentotaal.
- Een issue heeft nog geen test: noem dan de input (zie [`issue-tracker.md`](issue-tracker.md)).

Een blok uit een PR, met een uitkomst die gelijk is aan de huurprijscheck en dus zonder toelichting:

```markdown
**B. Woonkamer van 20 m² en een `PUP` van 12,5 m² bij vier adressen**

Vóór deze PR telt onderdeel II alleen de woonkamer: 20 m². Na deze PR telt de plek mee met deler 4: 20 + (12,5 / 4) = 23,125, afgerond 23 m².

|                | m² in onderdeel II | WOZ-punten |
| -------------- | ------------------ | ---------- |
| Voor           | 20                 | 73,75      |
| Na             | **23**             | **66,25**  |
| Huurprijscheck | gelijk             | gelijk     |

- Test: `test_parkeerplek_in_een_uitpandige_afgesloten_parkeergarage_telt_mee_in_onderdeel_ii`
```
