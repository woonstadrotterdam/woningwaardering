
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class SIGNALERINGSOORT:

    agressie = Referentiedata(
        code="AGR",
        naam="Agressie",
    )
    # agressie = ("AGR", "Agressie")

    oneigenlijk_gebruik_woning = Referentiedata(
        code="ONE",
        naam="Oneigenlijk gebruik woning",
    )
    # oneigenlijk_gebruik_woning = ("ONE", "Oneigenlijk gebruik woning")

    overlast = Referentiedata(
        code="OVE",
        naam="Overlast",
    )
    # overlast = ("OVE", "Overlast")

    huurschuld = Referentiedata(
        code="SCH",
        naam="Huurschuld",
    )
    # huurschuld = ("SCH", "Huurschuld")
