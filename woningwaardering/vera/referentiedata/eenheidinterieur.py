from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class EenheidinterieurReferentiedata(Referentiedata):
    pass


class Eenheidinterieur(Referentiedatasoort):
    gemeubileerd = EenheidinterieurReferentiedata(
        code="GEM",
        naam="Gemeubileerd",
    )

    gestoffeerd = EenheidinterieurReferentiedata(
        code="GES",
        naam="Gestoffeerd",
    )

    houten_vloer = EenheidinterieurReferentiedata(
        code="HOU",
        naam="Houten vloer",
    )

    laminaat = EenheidinterieurReferentiedata(
        code="LAM",
        naam="Laminaat",
    )

    plavuizen = EenheidinterieurReferentiedata(
        code="PLA",
        naam="Plavuizen",
    )
    """
    Plavuizen of tegels
    """

    pvc_vloer = EenheidinterieurReferentiedata(
        code="PVC",
        naam="Pvc vloer",
    )
    """
    Een PVC-vloer is een vloerbedekking gemaakt van polyvinylchloride (PVC), een
    synthetisch materiaal dat bekend staat om zijn duurzaamheid, waterbestendigheid
    en veelzijdigheid.
    """

    vloerbedekking = EenheidinterieurReferentiedata(
        code="VLB",
        naam="Vloerbedekking",
    )

    zelf_inrichten = EenheidinterieurReferentiedata(
        code="ZEL",
        naam="Zelf inrichten",
    )
