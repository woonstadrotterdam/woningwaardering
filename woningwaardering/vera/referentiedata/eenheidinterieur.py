from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Eenheidinterieur(Referentiedatasoort):
    gemeubileerd = Referentiedata(
        code="GEM",
        naam="Gemeubileerd",
    )

    gestoffeerd = Referentiedata(
        code="GES",
        naam="Gestoffeerd",
    )

    houten_vloer = Referentiedata(
        code="HOU",
        naam="Houten vloer",
    )

    laminaat = Referentiedata(
        code="LAM",
        naam="Laminaat",
    )

    plavuizen = Referentiedata(
        code="PLA",
        naam="Plavuizen",
    )
    """
    Plavuizen of tegels
    """

    pvc_vloer = Referentiedata(
        code="PVC",
        naam="Pvc vloer",
    )
    """
    Een PVC-vloer is een vloerbedekking gemaakt van polyvinylchloride (PVC), een
    synthetisch materiaal dat bekend staat om zijn duurzaamheid, waterbestendigheid
    en veelzijdigheid.
    """

    vloerbedekking = Referentiedata(
        code="VLB",
        naam="Vloerbedekking",
    )

    zelf_inrichten = Referentiedata(
        code="ZEL",
        naam="Zelf inrichten",
    )
