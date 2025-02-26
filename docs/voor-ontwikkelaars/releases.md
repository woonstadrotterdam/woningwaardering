# Releasemanagement

## Versienummering

Voor versienummering maken we gebruik van [SemVer](https://semver.org/lang/nl/):

Bij SemVer wordt een versienummer in de vorm MAJOR.MINOR.PATCH gebruikt, waarbij elk element als volgt wordt verhoogd:

- `MAJOR` wordt verhoogd bij incompatibele API-wijzigingen,
- `MINOR` wordt verhoogd bij het toevoegen van functionaliteit die compatibel is met de vorige versie, en
- `PATCH` wordt verhoogd bij compatibele bugfixes.

Er zijn aanvullende labels beschikbaar voor pre-release en build-metadata om toe te voegen aan het `MAJOR.MINOR.PATCH`-formaat.

Bijvoorbeeld: stel dat de huidige versie `0.1.3-alpha` is.

- De suffix `-alpha` wordt gebruikt zolang de software nog niet volledig is, bijvoorbeeld zolang nog niet alle beoogde stelselgroepen geïmplementeerd zijn
- Wanneer een nieuwe release alleen compatibele bugfixes of updates van dependencies bevat, wordt de nieuwe versie `0.1.4-alpha`
- Wanneer een nieuwe release ook compatibele nieuwe functionaliteit toevoegt, bijvoorbeeld de implementatie van een nieuwe stelselgroep, dan wordt de nieuwe versie `0.2.0-alpha`.
- Wanneer alle beoogde stelselgroepen geïmplementeerd zijn, wordt de nieuwe versie `1.0.0-beta`. De publieke api mag vanaf dan enkel nog backwards-compatible wijzigen.
- Wanneer de software volledig is en in productie genomen wordt, wordt de nieuwe versie `1.0.0`
- Wanneer er een incompatible wijziging is in de VERA modellen, wordt de nieuwe versie `2.0.0`, eventueel met het `-alpha` of `-beta` label, afhankelijk van de implementatiestatus.

## Releaseproces

Om een nieuwe release te starten, moet er een Git tag aangemaak worden volgens het format `v<versienummer>`. De prefix `v` geeft aan dat de tag een versiepunt markeert.

Bijvoorbeeld:

```bash
$ git tag v0.2.3-alpha
$ git push --tags
```

Hiermee start het releaseproces, gedefinieerd in een GitHub workflow: [.github/workflows/publish-to-pypi.ymls](https://github.com/woonstadrotterdam/woningwaardering/blob/main/.github/workflows/publish-to-pypi.yml)

In dit proces wordt een package aangemaakt met een [Python versienummer](https://packaging.python.org/en/latest/discussions/versioning/), afgeleid van het SemVer nummer in de tag. Bijvoorbeeld: `0.2.3-alpha` wordt `0.2.3a0`

De package wordt eerst gepubliceerd op [TestPyPi](https://test.pypi.org/project/woningwaardering/). Na goedkeuring wordt de package naar [PyPi](https://pypi.org/project/woningwaardering/) gepubliceerd. Daarna wordt er een release aangemaakt in GitHub, met een changelog met de titel en link naar alle pull requests die deel uitmaken van deze release. 