# test_vertrek_dat_niet_met_een_ander_adres_wordt_gedeeld_krijgt_geen_punten

Een gemeenschappelijk vertrek dat niet met een ander adres wordt gedeeld, krijgt in deze rubriek geen punten.

De slaapkamers worden met 2 onzelfstandige woonruimten op hetzelfde adres
gedeeld en hebben geen `gedeeld_met_aantal_adressen`. Pas vanaf twee
adressen hoort een ruimte in rubriek 9.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 9:
"Gemeenschappelijke vertrekken en overige ruimten zijn tot het woongebouw
behorende binnenruimten waar de bewoners van tenminste twee adressen in het
woongebouw krachtens de huurovereenkomst exclusieve toegang en
gebruiksrecht toe hebben."

Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
overeenkomstige toepassing is."

Bron: beleidsboek onzelfstandige woonruimten, 2.2: "Gemeenschappelijke
ruimten die worden gedeeld met twee of meer adressen worden gewaardeerd
onder rubriek 9."

Bron: implementatietoelichting, datamodel-uitbreidingen, "Gedeeld met aantal
adressen": "Het attribuut `gedeeld_met_aantal_adressen` geeft het aantal
adressen weer waarmee een bepaalde ruimte wordt gedeeld."

## Rapport

Geen waarderingen voor Gemeenschappelijke binnenruimten gedeeld met meerdere adressen.

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "slaapkamer1",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer1",
      "oppervlakte": 10.0,
      "verwarmd": true,
      "verkoeld": true,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
    },
    {
      "id": "slaapkamer2",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer2",
      "oppervlakte": 10.0,
      "verwarmd": true,
      "verkoeld": true,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
    }
  ]
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
      "code": "GBA",
      "naam": "Gemeenschappelijke binnenruimten gedeeld met meerdere adressen"
    }
  },
  "punten": 0.0,
  "woningwaarderingen": []
}
```
