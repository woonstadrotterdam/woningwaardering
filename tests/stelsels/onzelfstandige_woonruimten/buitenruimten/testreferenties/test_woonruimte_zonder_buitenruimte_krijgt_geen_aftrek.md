# test_woonruimte_zonder_buitenruimte_krijgt_geen_aftrek

Een onzelfstandige woonruimte zonder buitenruimte krijgt geen aftrek.

De test legt het huidige gedrag van de package vast. De tabel voor
onzelfstandige woonruimten noemt in rubriek 8 geen aftrek, de tabel voor
zelfstandige woonruimten wel. De toelichting onder A noemt de aftrek ook
en is voor onzelfstandige woonruimten van overeenkomstige toepassing,
tenzij ervan wordt afgeweken. De package kent de aftrek niet toe; die
keuze staat in geen implementatietoelichting.

Bron: wettekst, Bijlage I onder B, rubriek 8: "Maximaal 15 punten te
behalen", "Privé buitenruimte(n)", "Gemeenschappelijke buitenruimte(n) op
hetzelfde adres" en "Gemeenschappelijke buitenruimten gedeeld met meerdere
adressen".

Bron: wettekst, Bijlage I onder A, rubriek 8: "indien in het geheel géén
punten in deze rubriek (geen buitenruimte): af: 5 punten".

Bron: wettekst, Bijlage I onder A, toelichting rubriek 8: "Indien de woning
in het geheel geen privé-buitenruimte, geen gemeenschappelijke buitenruimte
of loggia heeft, wordt een aftrek toegepast van vijf punten."

Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "De toelichting
behorende tot bijlage I, onder A, het waarderingsstelsel voor woonruimte
welke een zelfstandige woning vormt, is voor onzelfstandige woonruimten van
overeenkomstige toepassing, tenzij hiervan wordt afgeweken."

## Rapport

Geen waarderingen voor Buitenruimten.

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": []
}
```

## Output

```json
{
  "criteriumGroep": {
    "stelsel": {
      "code": "ONZ",
      "naam": "Onzelfstandige woonruimten"
    },
    "stelselgroep": {
      "code": "BUI",
      "naam": "Buitenruimten"
    }
  },
  "punten": 0.0,
  "woningwaarderingen": []
}
```
