from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class ContactgegevendetailsoortReferentiedata(Referentiedata):
    pass


class Contactgegevendetailsoort(Referentiedatasoort):
    in_case_of_emergency = ContactgegevendetailsoortReferentiedata(
        code="ICE",
        naam="In case of emergency",
    )

    prive = ContactgegevendetailsoortReferentiedata(
        code="PRI",
        naam="Privé",
    )

    zakelijk = ContactgegevendetailsoortReferentiedata(
        code="ZAK",
        naam="Zakelijk",
    )
