# Releasemanagement

## Versienummering

Voor versienummering gebruiken we
[SemVer](https://semver.org/lang/nl/) in de vorm `MAJOR.MINOR.PATCH`. De
`MINOR`-versie wordt weergegeven als `YYYYMM`:

- `MAJOR` wordt verhoogd bij incompatibele wijzigingen in de publieke
  Python-API of de outputstructuur.
- `MINOR` identificeert de geïmplementeerde beleidsboekversie en wordt gevormd
  door het ingangsjaar en de ingangsmaand daarvan in de vorm `YYYYMM`. Nieuwe
  functionaliteit wordt uitgebracht als onderdeel van een nieuwe
  beleidsboekversie en verhoogt daarmee `MINOR`.
- `PATCH` wordt verhoogd bij compatibele bugfixes en onderhoudsupdates binnen
  dezelfde beleidsboekversie.

Een verhoging van `MINOR` is compatibel met de publieke Python-API en
outputstructuur. De berekening en puntuitkomsten kunnen wel wijzigen door de
implementatie van het nieuwe beleidsboek.

Bij een wijziging van `MAJOR` of `MINOR` wordt `PATCH` teruggezet naar `0`.
Versie `5.202607.0` bevat bijvoorbeeld een incompatibele wijziging, implementeert
het beleidsboek dat in juli 2026 ingaat en is de eerste release binnen die
combinatie.

Pre-releaselabels geven de implementatiestatus van een beleidsboekversie aan:

- `-alpha`: de implementatie is nog niet compleet;
- `-beta`: de implementatie is compleet, maar de validatie loopt nog;
- `-rc`: de implementatie en validatie zijn compleet en de versie is kandidaat
  voor de definitieve release;
- zonder label: de versie is definitief.

Zo kan `5.202701.0-alpha` naast compatibele updates zoals `5.202607.1` worden
gepubliceerd. Installatietools selecteren pre-releases alleen wanneer de gebruiker
daar expliciet om vraagt.

### Overgang vanaf versie 5.202607.0

We gebruiken deze versienummering vanaf versie `5.202607.0`. Tot en met versie
`4.3.4` stond `MINOR` voor compatibele nieuwe functionaliteit en `PATCH` voor
compatibele bugfixes. Vanaf versie `5.202607.0` identificeert `MINOR` de
beleidsboekversie als `YYYYMM` en telt `PATCH` de compatibele releases binnen die
beleidsboekversie.

De verhoging van `MAJOR` naar `5` markeert de incompatibele wijzigingen in de
publieke outputstructuur van deze release.

## Releaseproces

Om een nieuwe release te starten, moet er een Git tag aangemaakt worden volgens het format `v<versienummer>`. De prefix `v` geeft aan dat de tag een versiepunt markeert.

Bijvoorbeeld:

```bash
git tag v5.202607.0
git push --tags
```

Hiermee start het releaseproces, gedefinieerd in een GitHub workflow: [.github/workflows/publish-to-pypi.yml](https://github.com/woonstadrotterdam/woningwaardering/blob/main/.github/workflows/publish-to-pypi.yml)

In dit proces wordt een package aangemaakt met een Python-versienummer dat is
afgeleid van de tag. Een pre-releasetag zoals `v5.202701.0-alpha` wordt daarbij
genormaliseerd naar `5.202701.0a0`.

De package wordt eerst gepubliceerd op [TestPyPi](https://test.pypi.org/project/woningwaardering/). Na goedkeuring wordt de package naar [PyPi](https://pypi.org/project/woningwaardering/) gepubliceerd. Daarna wordt er een release aangemaakt in GitHub, met een changelog met de titel en link naar alle pull requests die deel uitmaken van deze release.
