from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class PuntenberekeningsoortReferentiedata(Referentiedata):
    pass


class Puntenberekeningsoort(Referentiedatasoort):
    intrekken_gebeurtenis_of_sanctie = PuntenberekeningsoortReferentiedata(
        code="INT",
        naam="Intrekken gebeurtenis of sanctie",
    )

    intrekken_toewijzing = PuntenberekeningsoortReferentiedata(
        code="ITO",
        naam="Intrekken toewijzing",
    )
    """
    Intrekken toewijzing van de eenheid.
    """

    koppelen_inschrijving = PuntenberekeningsoortReferentiedata(
        code="KOP",
        naam="Koppelen inschrijving",
    )

    maandelijkse_herberekening = PuntenberekeningsoortReferentiedata(
        code="MAA",
        naam="Maandelijkse herberekening",
    )

    nieuwe_inschrijving = PuntenberekeningsoortReferentiedata(
        code="NIE",
        naam="Nieuwe inschrijving",
    )
