
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class MAATSCHAPPELIJKLABEL:

    daeb = Referentiedata(
        code="DAE",
        naam="DAEB",
    )
    # daeb = ("DAE", "DAEB")
    """
    Als attribuut van klasse Eenheid: Geeft aan dat de eenheid tot de DAEB-tak behoort.
    Als attribuut van klasse Huurovereenkomst: Geeft aan dat de verhuring als zijnde
    DAEB verantwoord wordt. Dit is gelijk aan een gereguleerd huurovereenkomst. Als
    attribuut van de klasse FinancieelBedrijf: Geeft aan of de bedrijfsactiviteiten als
    DAEB verantwoord worden.
    """

    geconsolideerde_niet_daeb_verbinding = Referentiedata(
        code="GNDV",
        naam="Geconsolideerde NIET-DAEB verbinding",
    )
    # geconsolideerde_niet_daeb_verbinding = ("GNDV", "Geconsolideerde NIET-DAEB verbinding")
    """
    Als attribuut van de klasse FinancieelBedrijf: Geeft aan of het bedrijf een
    consolidatiebedrijf is, waarbinnen NIET-DAEB activiteiten worden verricht.
    """

    niet_daeb = Referentiedata(
        code="NDA",
        naam="NIET-DAEB",
    )
    # niet_daeb = ("NDA", "NIET-DAEB")
    """
    Als attribuut van klasse Eenheid: Geeft aan dat de eenheid tot de niet-DAEB-tak
    behoort. Als attribuut van klasse Huurovereenkomst: Geeft aan dat de verhuring als
    zijnde niet-DAEB verantwoord wordt. Dit is gelijk aan een geliberaliseerde
    huurovereenkomst. Als attribuut van de klasse FinancieelBedrijf: Geeft aan of de
    bedrijfsactiviteiten als NIET-DAEB verantwoord worden.
    """
