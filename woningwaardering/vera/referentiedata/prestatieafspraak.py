from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class PrestatieafspraakReferentiedata(Referentiedata):
    pass


class Prestatieafspraak(Referentiedatasoort):
    huurverhoging_t_b_v_investering = PrestatieafspraakReferentiedata(
        code="HUU",
        naam="Huurverhoging t.b.v. investering",
    )
    """
    Inkomensafhankelijke huurverhoging boven normpercentage waarvoor gemeente,
    corporatie en huurdersorganisatie hebben afgesproken dat zij de meeropbrengsten
    van die hogere huurverhoging gebruiken voor investeringen.
    """
