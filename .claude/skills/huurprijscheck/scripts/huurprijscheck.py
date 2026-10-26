"""Bedien de huurprijscheck van de Huurcommissie vanaf de command line.

De huurprijscheck is een formulierenwizard zonder API. Dit script houdt een
sessie bij (cookie en huidige pagina) en biedt per stap van de wizard een
commando: de pagina tonen, velden invullen, een link volgen, een adres
opzoeken, naar de volgende stap gaan en het resultaat lezen. Veldnamen en keuzes worden uit de pagina zelf gelezen.

Voorbeeld:
    python huurprijscheck.py start zelfstandig
    python huurprijscheck.py volgende regime=39 wozValue=300000
    python huurprijscheck.py kies Woonkamer
    python huurprijscheck.py vul size=20 heated=Ja
    python huurprijscheck.py kies "Woonkamer Toevoegen"
    python huurprijscheck.py resultaat
"""

import argparse
import html
import json
import re
import sys
import tempfile
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from html.parser import HTMLParser
from http.cookiejar import MozillaCookieJar
from pathlib import Path

BASIS = "https://huurprijscheck.huurcommissie.nl"
STARTPAGINA = {
    "zelfstandig": "/zelfstandige-woonruimte",
    "onzelfstandig": "/onzelfstandige-woonruimte",
}
FORMULIER = "calculator"
ADRESFORMULIER = "postalCodeAndHouseNumber"
KOPPEN = {"h1", "h2", "h3", "h4", "h5", "h6"}
TEKSTELEMENTEN = {"label", "a", "option", "title", "legend", "textarea"} | KOPPEN


@dataclass
class Veld:
    """Een invoerveld of één keuze van een radiogroep of checkbox."""

    naam: str
    soort: str
    waarde: str = ""
    gekozen: bool = False
    id: str = ""
    groep: str = ""
    opties: list[tuple[str, str, bool]] = field(default_factory=list)

    @property
    def kort(self) -> str:
        """De veldnaam zonder het voorvoegsel van de wizard."""
        return re.sub(r"^.*?\[data\]", "", self.naam).strip("[]").replace("][", ".")


class Pagina(HTMLParser):
    """Een pagina van de wizard: formulieren, labels, links en tekst.

    Args:
        bron (str): De HTML van de pagina.
    """

    def __init__(self, bron: str) -> None:
        super().__init__()
        self.bron = bron
        self.acties: dict[str, str] = {}
        self.velden: dict[str, list[Veld]] = {}
        self.labels: dict[str, str] = {}
        self.links: list[tuple[str, str, str]] = []
        self._kop = ""
        self.titel = ""
        self._formulier = ""
        self._legenda = ""
        self._open: list[tuple[str, dict[str, str], list[str]]] = []
        self._select: Veld | None = None
        self.feed(bron)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        """Verwerk een openingstag.

        Args:
            tag (str): De naam van het element.
            attrs (list[tuple[str, str | None]]): De attributen van het element.
        """
        a = {k: v or "" for k, v in attrs}
        if tag == "form":
            self._formulier = a.get("id", "")
            self.acties[self._formulier] = a.get("action", "")
            self.velden[self._formulier] = []
        elif tag == "fieldset":
            self._legenda = ""
        elif tag in ("input", "select", "textarea") and a.get("name"):
            veld = Veld(
                naam=a["name"],
                soort=a.get("type", tag),
                waarde=a.get("value", ""),
                gekozen="checked" in a,
                id=a.get("id", ""),
                groep=a.get("aria-label", "") or self._legenda,
            )
            self.velden.setdefault(self._formulier, []).append(veld)
            if tag == "select":
                self._select = veld
        if tag in TEKSTELEMENTEN:
            self._open.append((tag, a, []))

    def handle_endtag(self, tag: str) -> None:
        """Verwerk een sluittag.

        Args:
            tag (str): De naam van het element.
        """
        if tag == "form":
            self._formulier = ""
        elif tag == "select":
            self._select = None
        if not self._open or self._open[-1][0] != tag:
            return
        _, a, delen = self._open.pop()
        tekst = re.sub(r"\s+", " ", "".join(delen)).strip()
        if tag == "label" and a.get("for"):
            self.labels[a["for"]] = tekst
        elif tag == "a" and a.get("href"):
            self.links.append((self._naam(a) or tekst, a["href"], self._kop))
        elif tag == "option" and self._select is not None:
            waarde = a.get("value", "").strip()
            if waarde and (waarde != tekst or waarde.isdigit()):
                self._select.opties.append((waarde, tekst, "selected" in a))
        elif tag == "title" and not self.titel:
            self.titel = tekst
        elif tag == "legend":
            self._legenda = tekst
        elif tag in KOPPEN:
            self._kop = tekst
        if self._open and tag == "a":
            self._open[-1][2].append(tekst)

    def _naam(self, a: dict[str, str]) -> str:
        """De toegankelijke naam van een link, bv. 'Woonkamer Wijzigen'."""
        delen = []
        for verwijzing in a.get("aria-labelledby", "").split():
            gevonden = re.search(
                rf'id="{re.escape(verwijzing)}"[^>]*>([^<]*)<', self.bron
            )
            if gevonden:
                delen.append(gevonden.group(1))
        return re.sub(r"\s+", " ", html.unescape(" ".join(delen))).strip()

    def vraag(self, veld: Veld) -> str:
        """De vraag of het label dat bij een veld of keuzegroep hoort.

        Args:
            veld (Veld): Het veld.

        Returns:
            str: De tekst, of een lege string als de pagina er geen geeft.
        """
        if veld.groep:
            return veld.groep
        kort = veld.kort
        for kandidaat in (kort, kort.removesuffix(".select"), kort.rsplit(".", 1)[-1]):
            gevonden = re.search(
                rf'<(?:span|legend|p|h\d)[^>]*\bid="{re.escape(kandidaat)}"[^>]*>([^<]+)<',
                self.bron,
            )
            if gevonden and gevonden.group(1).strip():
                return re.sub(r"\s+", " ", html.unescape(gevonden.group(1))).strip()
        plek = self.bron.find(f'name="{veld.naam}"')
        ervoor = self.bron[max(0, plek - 2500) : plek] if plek > 0 else ""
        koppen = re.findall(r"<(?:h[2-6]|label)\b[^>]*>\s*([^<]+?)\s*<", ervoor)
        return re.sub(r"\s+", " ", html.unescape(koppen[-1])) if koppen else ""

    def keuzelinks(self) -> dict[str, tuple[str, str]]:
        """De links binnen de wizard, met een volgnummer bij gelijke namen.

        Returns:
            dict[str, tuple[str, str]]: Het adres en de kop per linknaam.
        """
        uniek: dict[str, tuple[str, str]] = {}
        gehad: set[tuple[str, str]] = set()
        for naam, adres, kop in self.links:
            if not naam or (naam, adres) in gehad:
                continue
            gehad.add((naam, adres))
            if "pricecheck" not in adres and not re.search(r"ruimte/\w", adres):
                continue
            if adres.startswith("/en/"):
                continue
            sleutel, nummer = naam, 1
            while sleutel in uniek:
                nummer += 1
                sleutel = f"{naam} ({nummer})"
            uniek[sleutel] = (adres, kop)
        return uniek

    def handle_data(self, data: str) -> None:
        """Verzamel tekst binnen een open tekstelement.

        Args:
            data (str): De tekst.
        """
        if self._open:
            self._open[-1][2].append(data)

    @property
    def tekst(self) -> str:
        """De zichtbare tekst van de pagina, zonder scripts en opmaak."""
        kaal = re.sub(r"<(script|style)\b.*?</\1>", " ", self.bron, flags=re.S)
        kaal = re.sub(r"<[^>]+>", " ", kaal)
        return re.sub(r"\s+", " ", html.unescape(kaal)).strip()

    @property
    def adreszoeker(self) -> str:
        """Het adres waarmee de wizard postcode en huisnummer opzoekt."""
        gevonden = re.search(r'addressUrl = "([^"]*)"', self.bron)
        return html.unescape(gevonden.group(1)) if gevonden else ""

    @property
    def autosave(self) -> str:
        """Het adres waarnaar de wizard het formulier tussentijds opslaat."""
        gevonden = re.search(r'ajaxUrl = "([^"]*)"', self.bron)
        return html.unescape(gevonden.group(1)) if gevonden else ""

    def resultaat(self) -> str:
        """De puntentelling zoals de wizard die naast het formulier toont.

        Returns:
            str: De regels van de puntentelling, of een lege string.
        """
        gevonden = re.search(
            r"Resultaat Punten (.*?Maximale huurprijs € [\d.,]+)", self.tekst
        )
        if not gevonden:
            return ""
        regels = re.sub(
            r" (Totaal aantal punten|Totaal |Subtotaal categorie |Maximale huurprijs)",
            r"\n\1",
            " " + gevonden.group(1),
        )
        return regels.strip()

    def overzicht(self) -> str:
        """Het volledige resultaat zoals de overzichtspagina van de wizard dat toont.

        Returns:
            str: Meldingen, samenvatting en puntentelling, of een lege string.
        """
        gevonden = re.search(
            r"Resultaat Huurprijscheck (.*?) (?:Opslaan en later verder|Copyright) ",
            self.tekst,
        )
        if not gevonden:
            return ""
        koppen = (
            "Maak de puntentelling compleet|Puntentelling volgens|Samenvatting|"
            "Punten per onderdeel|Goed om te weten|Details van de puntentelling|"
            "Subtotaal categorie|Totaal |Maximale huurprijs|Inclusief opslagen"
        )
        inhoud = re.sub(
            r"Goed om te weten .*?(?=Details van de puntentelling)|Print resultaat$",
            "",
            gevonden.group(1),
        )
        return re.sub(rf" ({koppen})", r"\n\1", " " + inhoud).strip()


class Sessie:
    """De cookie en de huidige pagina van één doorloop van de wizard.

    Args:
        map_ (Path): De map waarin cookie en huidige pagina staan.
    """

    def __init__(self, map_: Path) -> None:
        map_.mkdir(parents=True, exist_ok=True)
        self._status = map_ / "status.json"
        self._cookies = MozillaCookieJar(str(map_ / "cookies.txt"))
        if (map_ / "cookies.txt").exists():
            self._cookies.load(ignore_discard=True)
        self._opener = urllib.request.build_opener(
            urllib.request.HTTPCookieProcessor(self._cookies)
        )
        self._opener.addheaders = [
            ("User-Agent", "woningwaardering-huurprijscheck-skill")
        ]

    @property
    def adres(self) -> str:
        """Het adres van de huidige pagina."""
        if not self._status.exists():
            sys.exit("Geen sessie. Begin met: start zelfstandig|onzelfstandig")
        return str(json.loads(self._status.read_text())["adres"])

    def wis(self) -> None:
        """Begin een nieuwe sessie zonder cookie."""
        self._cookies.clear()

    def haal(self, adres: str, data: list[tuple[str, str]] | None = None) -> Pagina:
        """Vraag een pagina op en onthoud die als huidige pagina.

        Args:
            adres (str): Het adres, absoluut of relatief ten opzichte van de site.
            data (list[tuple[str, str]] | None): Formuliergegevens voor een POST.

        Returns:
            Pagina: De pagina waarop de wizard uitkomt.
        """
        bron, eindadres = self._verzoek(adres, data, "text/html")
        self._status.write_text(json.dumps({"adres": eindadres}))
        return Pagina(bron)

    def bekijk(self, adres: str) -> Pagina:
        """Vraag een pagina op zonder de huidige pagina te verlaten.

        Args:
            adres (str): Het adres, absoluut of relatief ten opzichte van de site.

        Returns:
            Pagina: De opgevraagde pagina.
        """
        return Pagina(self._verzoek(adres, None, "text/html")[0])

    def sla_op(self, adres: str, data: list[tuple[str, str]]) -> str:
        """Sla een formulier tussentijds op, zoals de wizard zelf doet.

        Args:
            adres (str): Het autosave-adres van de pagina.
            data (list[tuple[str, str]]): De formuliergegevens.

        Returns:
            str: Het antwoord van de wizard.
        """
        return self._verzoek(adres, data, "application/json")[0]

    def _verzoek(
        self, adres: str, data: list[tuple[str, str]] | None, soort: str
    ) -> tuple[str, str]:
        volledig = urllib.parse.urljoin(BASIS, adres)
        if not volledig.startswith(BASIS + "/"):
            sys.exit(f"Adres buiten de huurprijscheck: {volledig}")
        body = urllib.parse.urlencode(data).encode() if data is not None else None
        verzoek = urllib.request.Request(volledig, body, {"Accept": soort})
        with self._opener.open(verzoek, timeout=60) as antwoord:
            bron = antwoord.read().decode("utf-8", "replace")
            eindadres = str(antwoord.geturl())
        self._cookies.save(ignore_discard=True)
        return bron, eindadres


def _vertaal(veld: Veld, keuzes: list[tuple[str, str]], waarde: str) -> str:
    """Vertaal een keuze op label naar de waarde die de wizard verwacht."""
    for optiewaarde, label in keuzes:
        if waarde == optiewaarde:
            return waarde
    for optiewaarde, label in keuzes:
        if waarde.casefold() == label.casefold():
            return optiewaarde
    if keuzes:
        mogelijk = ", ".join(f"{w} ({lbl})" for w, lbl in keuzes)
        sys.exit(f"Onbekende keuze '{waarde}' voor {veld.kort}. Kies uit: {mogelijk}")
    return waarde


def formuliergegevens(
    pagina: Pagina, invoer: dict[str, str], formulier: str = FORMULIER
) -> list[tuple[str, str]]:
    """Stel de gegevens samen die het formulier zou versturen.

    Args:
        pagina (Pagina): De pagina met het formulier.
        invoer (dict[str, str]): Nieuwe waarden per korte veldnaam.
        formulier (str): Het id van het formulier.

    Returns:
        list[tuple[str, str]]: Alle velden van het formulier, met de invoer verwerkt.
    """
    velden = pagina.velden.get(formulier, [])
    nieuw: dict[str, str] = {}
    for sleutel, waarde in invoer.items():
        passend = [
            v for v in velden if v.kort == sleutel or v.kort.endswith("." + sleutel)
        ]
        if not passend:
            sys.exit(f"Onbekend veld '{sleutel}'. Bekijk de velden met: toon")
        veld = passend[0]
        if veld.soort in ("radio", "checkbox", "hidden"):
            keuzes = [
                (v.waarde, pagina.labels.get(v.id, ""))
                for v in passend
                if v.soort != "hidden"
            ]
        else:
            keuzes = [(w, lbl) for w, lbl, _ in veld.opties]
        if veld.soort == "number":
            waarde = waarde.replace(",", ".")
        nieuw[veld.naam] = _vertaal(veld, keuzes, waarde)

    data: list[tuple[str, str]] = []
    gehad: set[str] = set()
    for veld in velden:
        if veld.soort == "submit" or veld.naam in gehad:
            continue
        if veld.naam in nieuw:
            data.append((veld.naam, nieuw[veld.naam]))
            gehad.add(veld.naam)
        elif veld.soort in ("radio", "checkbox"):
            if veld.gekozen:
                data.append((veld.naam, veld.waarde))
                gehad.add(veld.naam)
        elif veld.soort == "select":
            gekozen = [w for w, _, actief in veld.opties if actief]
            data.append((veld.naam, gekozen[0] if gekozen else ""))
            gehad.add(veld.naam)
        elif veld.soort == "hidden":
            data.append((veld.naam, veld.waarde))
        else:
            data.append((veld.naam, veld.waarde))
            gehad.add(veld.naam)
    return data


def toon(pagina: Pagina, met_tekst: bool = False) -> None:
    """Druk de huidige pagina af: velden, links en puntentelling.

    Args:
        pagina (Pagina): De pagina.
        met_tekst (bool): Druk ook de volledige tekst van de pagina af.
    """
    print(f"# {pagina.titel}")
    velden = pagina.velden.get(FORMULIER, [])
    print("\nVelden (naam | label | huidige waarde of keuzes):")
    gehad: set[str] = set()
    for veld in velden:
        if veld.soort in ("hidden", "submit") or veld.naam in gehad:
            continue
        gehad.add(veld.naam)
        label = pagina.labels.get(veld.id, "")
        if veld.soort in ("radio", "checkbox"):
            groep = [v for v in velden if v.naam == veld.naam and v.soort != "hidden"]
            keuzes = ", ".join(
                dict.fromkeys(
                    f"{'*' if v.gekozen else ''}{v.waarde}={pagina.labels.get(v.id, '')}"
                    for v in groep
                )
            )
            print(f"  {veld.kort} | {pagina.vraag(veld)} | {keuzes}")
        elif veld.soort == "select":
            keuzes = ", ".join(
                f"{'*' if actief else ''}{w}={lbl}" for w, lbl, actief in veld.opties
            )
            if len(veld.opties) > 1 and all(w == lbl for w, lbl, _ in veld.opties):
                gekozen = [w for w, _, actief in veld.opties if actief]
                keuzes = f"{veld.opties[0][0]} t/m {veld.opties[-1][0]}" + (
                    f" (*{gekozen[0]})" if gekozen else ""
                )
            print(f"  {veld.kort} | {pagina.vraag(veld) or label} | {keuzes}")
        else:
            print(f"  {veld.kort} | {label or pagina.vraag(veld)} | {veld.waarde!r}")
    knoppen = [v.waarde for v in velden if v.soort == "submit"]
    if knoppen:
        print(f"\nKnop voor `volgende`: {', '.join(knoppen)}")
    print("\nLinks voor `kies`:")
    kop = None
    for naam, (_, onder) in pagina.keuzelinks().items():
        if onder != kop:
            kop = onder
            print(f"  [{kop}]")
        print(f"    {naam}")
    resultaat = pagina.resultaat()
    if resultaat:
        print("\nPuntentelling tot nu toe:\n" + resultaat)
    if met_tekst:
        print("\nTekst van de pagina:\n" + pagina.tekst)


def main() -> None:
    """Voer één commando van de wizard uit."""
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument(
        "--sessie",
        type=Path,
        default=Path(tempfile.gettempdir()) / "huurprijscheck-sessie",
        help="map voor cookie en huidige pagina",
    )
    commandos = parser.add_subparsers(dest="commando", required=True)
    start = commandos.add_parser("start", help="begin een nieuwe huurprijscheck")
    start.add_argument("stelsel", choices=sorted(STARTPAGINA))
    tonen = commandos.add_parser("toon", help="toon de huidige pagina")
    tonen.add_argument("--tekst", action="store_true", help="ook de volledige tekst")
    vullen = commandos.add_parser("vul", help="vul velden in en sla op")
    vullen.add_argument("invoer", nargs="+", metavar="veld=waarde")
    volgende = commandos.add_parser("volgende", help="ga naar de volgende stap")
    volgende.add_argument("invoer", nargs="*", metavar="veld=waarde")
    kiezen = commandos.add_parser("kies", help="volg een link, bv. een ruimte")
    kiezen.add_argument("link")
    adres = commandos.add_parser("adres", help="zoek een adres op (stap 1)")
    adres.add_argument("postcode")
    adres.add_argument("huisnummer", help="huisnummer met eventuele toevoeging")
    commandos.add_parser("resultaat", help="toon het volledige resultaat")
    args = parser.parse_args()

    sessie = Sessie(args.sessie)
    if args.commando == "start":
        sessie.wis()
        toon(sessie.haal(STARTPAGINA[args.stelsel]))
        return

    if args.commando == "resultaat":
        stelsel = urllib.parse.urlparse(sessie.adres).path.split("/")[1]
        detail = sessie.bekijk(f"/{stelsel}/detail")
        print(detail.overzicht() or detail.resultaat() or "Nog geen puntentelling.")
        return

    pagina = sessie.haal(sessie.adres)
    invoer = dict(i.split("=", 1) for i in getattr(args, "invoer", []))
    if args.commando == "toon":
        toon(pagina, args.tekst)
    elif args.commando == "adres":
        if not pagina.adreszoeker or ADRESFORMULIER not in pagina.velden:
            sys.exit("Een adres opzoeken kan alleen op stap 1.")
        data = formuliergegevens(
            pagina,
            {"postalCode": args.postcode, "houseNumber": args.huisnummer},
            ADRESFORMULIER,
        )
        print(
            "Antwoord van de adreszoeker:\n" + sessie.sla_op(pagina.adreszoeker, data)
        )
        sessie.sla_op(pagina.autosave, formuliergegevens(pagina, {}))
        toon(sessie.haal(sessie.adres))
    elif args.commando == "vul":
        if not pagina.autosave:
            sys.exit("Deze pagina slaat niet tussentijds op; gebruik `volgende`.")
        sessie.sla_op(pagina.autosave, formuliergegevens(pagina, invoer))
        toon(sessie.haal(sessie.adres))
    elif args.commando == "volgende":
        knoppen = [v for v in pagina.velden.get(FORMULIER, []) if v.soort == "submit"]
        if not knoppen:
            sys.exit("Deze pagina heeft geen knop naar een volgende stap.")
        data = formuliergegevens(pagina, invoer)
        data.append((knoppen[0].naam, knoppen[0].waarde))
        vorige = sessie.adres
        nieuw = sessie.haal(pagina.acties[FORMULIER], data)
        if FORMULIER not in nieuw.velden:
            sessie.haal(vorige)
            sys.exit(
                "De huurprijscheck gaf geen volgende stap terug; controleer de invoer."
            )
        toon(nieuw)
    elif args.commando == "kies":
        gezocht = args.link.casefold()
        passend = [
            adres
            for naam, (adres, _) in pagina.keuzelinks().items()
            if naam.casefold() == gezocht
        ]
        if not passend:
            sys.exit(f"Geen link '{args.link}'. Bekijk de links met: toon")
        toon(sessie.haal(passend[0]))


if __name__ == "__main__":
    main()
