# Bugbot-regels — VERA

Deze regels gelden bij wijzigingen onder `woningwaardering/vera/` (Bugbot laadt dit bestand bij reviews van bestanden in of onder deze map).

Volg daarnaast altijd de repo-brede regels uit de root-`/.cursor/BUGBOT.md`, met name voor `README.md`, `CONTEXT.md`, `docs/voor-ontwikkelaars/index.md` en de bronvolgorde bij domeinwijzigingen.

Betrek bij wijzigingen onder `woningwaardering/vera/` bovendien expliciet:

- `docs/implementatietoelichtingen/datamodel-uitbreidingen.md` voor lokale uitbreidingen op VERA-modellen en referentiedata;
- relevante pagina's onder `docs/implementatietoelichtingen/` wanneer een VERA-beperking of modelkeuze direct doorwerkt in stelselgedrag;
- `CONTEXT.md` voor terminologie rond VERA, referentiedata en modeluitbreidingen.

## Gegenereerde code

Behandel gegenereerde VERA-code terughoudend.

- Signaleer handmatige edits in gegenereerde bestanden zoals `woningwaardering/vera/bvg/generated.py`, tenzij de PR aantoont dat regeneratie via scripts is gedaan.
- Gebruik de bestaande scripts, met name:
  - `scripts/genereer_vera_bvg_modellen.py`
  - `scripts/genereer_vera_referentiedata.py`
  - `scripts/uitbreiden_vera_modellen.py`
- Goed: modelregeneratie via die scripts, met eventuele modeluitbreidingen via het vastgelegde uitbreidingspad.
- Fout: directe handmatige wijzigingen in `generated.py` “even snel” voor één attribuut, zonder script of expliciete taak.

## Modeluitbreidingen en referentiedata

- Lokale uitbreidingen op VERA-modellen horen toegelicht in `docs/implementatietoelichtingen/datamodel-uitbreidingen.md`, of in dezelfde PR te worden toegevoegd.
- Wijzigingen in `woningwaardering/vera/referentiedata` of `referentiedata_uitbreiding.csv` moeten consistent blijven met de VERA-enums en bestaande naamgevingsconventies.
- Test geen gegenereerde VERA-code alleen om coverage te verhogen.
