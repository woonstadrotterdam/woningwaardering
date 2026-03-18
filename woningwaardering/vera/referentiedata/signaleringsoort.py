from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class SignaleringsoortReferentiedata(Referentiedata):
    pass


class Signaleringsoort(Referentiedatasoort):
    agressie = SignaleringsoortReferentiedata(
        code="AGR",
        naam="Agressie",
    )
    """
    Situaties waarbij sprake is van verbale of fysieke agressie richting personen of
    eigendommen.
    """

    ondersteuningsbehoefte = SignaleringsoortReferentiedata(
        code="ONB",
        naam="Ondersteuningsbehoefte",
    )
    """
    Situaties waarin een relatie hulp ontvangt of nodig heeft die wij als verhuurder
    moeten meenemen in ons contact, beheer of dienstverlening.
    """

    oneigenlijk_gebruik_woning = SignaleringsoortReferentiedata(
        code="ONE",
        naam="Oneigenlijk gebruik woning",
    )
    """
    Het gebruik van een woning in strijd met het huurcontract, zoals onderverhuur of
    zakelijk gebruik.
    """

    overlast = SignaleringsoortReferentiedata(
        code="OVE",
        naam="Overlast",
    )
    """
    Klachten over hinderlijk gedrag zoals geluidsoverlast, vervuiling of intimiderend
    gedrag.
    """

    huurschuld = SignaleringsoortReferentiedata(
        code="SCH",
        naam="Huurschuld",
    )
    """
    Situaties waarin sprake is van een betalingsachterstand in de huur.
    """

    wangedrag_naar_medewerkers = SignaleringsoortReferentiedata(
        code="WAN",
        naam="Wangedrag naar medewerkers",
    )
    """
    Ongewenst gedrag gericht op medewerkers, zoals belediging, bedreiging of
    intimidatie.
    """
