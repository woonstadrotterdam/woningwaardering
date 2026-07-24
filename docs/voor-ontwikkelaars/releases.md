# Releasemanagement

## Versienummering

Voor de versienummering gebruiken we [SemVer](https://semver.org/lang/nl/) in de vorm `MAJOR.MINOR.PATCH`. De `MINOR`-versie heeft het formaat `YYYYMM`:

- `MAJOR` wordt verhoogd bij incompatibele wijzigingen in de publieke Python-API of de outputstructuur.
- `MINOR` geeft de versie van het beleidsboek aan en bestaat uit het ingangsjaar en de ingangsmaand in het formaat `YYYYMM`. Nieuwe functionaliteit wordt gekoppeld aan een nieuwe beleidsboekversie en leidt daarom tot een verhoging van `MINOR`.
- `PATCH` wordt verhoogd bij compatibele bugfixes en onderhoudsupdates binnen dezelfde beleidsboekversie.

Een verhoging van `MINOR` is compatibel met de publieke Python-API en outputstructuur.

Bij een wijziging van `MAJOR` of `MINOR` wordt `PATCH` teruggezet naar `0`.
Versie `5.202607.0` bevat bijvoorbeeld een incompatibele wijziging, implementeert het beleidsboek dat in juli 2026 ingaat en is de eerste release binnen die combinatie.

Pre-releaselabels geven de implementatiestatus van een beleidsboekversie aan:

- `-alpha`: de implementatie is nog niet compleet;
- `-beta`: de implementatie is compleet, maar de validatie loopt nog;
- `-rc`: de implementatie en validatie zijn compleet en de versie is kandidaat voor de definitieve release;
- zonder label: de versie is definitief.

Zo kan `5.202701.0-alpha` naast compatibele updates zoals `5.202607.1` worden gepubliceerd. Installatietools selecteren pre-releases alleen wanneer de gebruiker daar expliciet om vraagt.

### Overgang vanaf versie 5.202607.0

Vanaf versie `5.202607.0` gebruiken we een nieuwe manier van versienummering. Tot en met versie `4.3.4` stond `MINOR` voor nieuwe functionaliteit die compatibel was met eerdere versies, en `PATCH` voor compatibele bugfixes.

Vanaf versie `5.202607.0` geeft `MINOR` de versie van het beleidsboek aan in het formaat `YYYYMM`. `PATCH` geeft vervolgens het volgnummer van de compatibele releases binnen die beleidsboekversie aan.

De verhoging van `MAJOR` naar `5` markeert een incompatibele wijziging in de outputstructuur van deze release.

## Releaseproces

Om een nieuwe release te starten, moet er een Git tag aangemaakt worden volgens het format `v<versienummer>`. De prefix `v` geeft aan dat de tag een versiepunt markeert.

Bijvoorbeeld:

```bash
git tag v5.202607.0
git push --tags
```

Hiermee start het releaseproces, gedefinieerd in een GitHub workflow: [.github/workflows/publish-to-pypi.yml](https://github.com/woonstadrotterdam/woningwaardering/blob/main/.github/workflows/publish-to-pypi.yml)

In dit proces wordt een package aangemaakt met een Python-versienummer dat is afgeleid van de tag. Een pre-releasetag zoals `v5.202701.0-alpha` wordt daarbij genormaliseerd naar `5.202701.0a0`.

De package wordt eerst gepubliceerd op [TestPyPi](https://test.pypi.org/project/woningwaardering/). Na goedkeuring wordt de package naar [PyPi](https://pypi.org/project/woningwaardering/) gepubliceerd. Daarna wordt er een release aangemaakt in GitHub, met een changelog met de titel en link naar alle pull requests die deel uitmaken van deze release.
