# test_parkeerplek_kleiner_dan_12_m2_krijgt_geen_punten

Een parkeerplek met een oppervlakte onder 12 m² krijgt geen punten.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 10: "Een parkeerplek
is een afgebakend vak en heeft een oppervlakte van minimaal 12 m² waar een
gangbare personenauto in zijn geheel op past."

Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
overeenkomstige toepassing is."

Bron: beleidsboek onzelfstandige woonruimten, 2.10.3: "Een parkeerplek is
een afgebakend vak en heeft een oppervlakte van minimaal 12 m² waarin een
gangbare personenauto in zijn geheel past."

## Rapport

Geen waarderingen voor Gemeenschappelijke parkeerruimten.

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "parkeerplek_buiten_behorend_bij_complex",
      "soort": {
        "code": "GEM",
        "naam": "Gemeenschappelijke ruimten en voorzieningen"
      },
      "detailSoort": {
        "code": "PBC",
        "naam": "Parkeerplek buiten behorend bij complex"
      },
      "naam": "Parkeerplek buiten behorend bij complex",
      "oppervlakte": 11.0,
      "gedeeldMetAantalAdressen": 10,
      "aantal": 2,
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
      "code": "GPA",
      "naam": "Gemeenschappelijke parkeerruimten"
    }
  },
  "punten": 0.0,
  "woningwaarderingen": []
}
```
