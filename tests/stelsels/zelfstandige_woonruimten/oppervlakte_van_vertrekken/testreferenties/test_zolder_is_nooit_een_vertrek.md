# test_zolder_is_nooit_een_vertrek

Een zolderruimte met de detailsoort `zolder` wordt nooit als vertrek gewaardeerd.

De package waarschuwt bij de zolder die als vertrek is aangeleverd: die
wordt als overige ruimte gewaardeerd.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 1: "Zolderruimten
slechts als vertrek gewaardeerd worden, indien deze bereikbaar zijn via een
vaste trap en indien de vloer begaanbaar en het dak beschoten is."

Bron: implementatietoelichting zelfstandige woonruimten, 2.2.2.3: "Alleen
een `zoldervertrek` voldoet aan eis 2"; een `zolder` "voldoet niet aan de
afwerkingseisen" en "wordt daarom nooit als vertrek gewaardeerd".

## Rapport

Geen waarderingen voor Oppervlakte van vertrekken.

## Waarschuwingen

- UserWarning: Ruimte 'Zolder1' (zolder1) is aangeleverd als Vertrek maar wordt gewaardeerd als Overige ruimten.

## Input

```json
{
  "ruimten": [
    {
      "id": "zolder1",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "ZOL",
        "naam": "Zolder"
      },
      "naam": "Zolder1",
      "oppervlakte": 10.0
    },
    {
      "id": "zolder2",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "ZOL",
        "naam": "Zolder"
      },
      "naam": "Zolder2",
      "oppervlakte": 1.0
    }
  ]
}
```

## Output

```json
{
  "criteriumGroep": {
    "stelsel": {
      "code": "ZEL",
      "naam": "Zelfstandige woonruimten"
    },
    "stelselgroep": {
      "code": "OVZ",
      "naam": "Oppervlakte van vertrekken"
    }
  },
  "punten": 0.0,
  "woningwaarderingen": []
}
```
