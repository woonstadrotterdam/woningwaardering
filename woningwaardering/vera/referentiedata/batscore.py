from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class BatscoreReferentiedata(Referentiedata):
    pass


class Batscore(Referentiedatasoort):
    nultrapswoning = BatscoreReferentiedata(
        code="BAT1",
        naam="Nultrapswoning",
    )
    """
    De entree, de woonkamer, het toiletkeuken, de slaapkamer en de doucheruimte bevinden
    zich op de begane grond of zijn met een lift of een stoeltjeslift bereikbaar. Er
    kunnen hoge drempels en smalle doorgangen zijn.
    """

    rollator_bezoekbaar = BatscoreReferentiedata(
        code="BAT2",
        naam="Rollator bezoekbaar",
    )
    """
    Bezoekbaar wil zeggen dat iemand met een rollator in de woonkamer en bij de
    toiletdeur kan komen. De woonkamer en het toilet bevinden zich op de begane
    grond of zijn met een lift of een stoeltjeslift bereikbaar. Drempels zijn
    maximaal 20 mm hoog en hellingen zijn flauw. De vrije doorgang is nooit smaller
    dan 800 mm.
    """

    rolstoel_bezoekbaar = BatscoreReferentiedata(
        code="BAT3",
        naam="Rolstoel bezoekbaar",
    )
    """
    Bezoekbaar wil zeggen dat iemand met een rolstoel in de woonkamer en bij de
    toiletdeur kan komen. De woonkamer en het toilet bevinden zich op de begane
    grond of zijn met een lift of een plateaulift (geschikt voor rolstoel)
    bereikbaar. Drempels zijn maximaal 20 mm hoog en hellingen zijn flauw. De vrije
    doorgang is nooit smaller dan 800 mm. Eventuele bochten om in de woonkamer of
    bij het toilet te komen voldoen (X+Y is groter dan 1950 mm).
    """

    rolstoel_woonbaar = BatscoreReferentiedata(
        code="BAT4",
        naam="Rolstoel woonbaar",
    )
    """
    Rolstoel woonbaar wil zeggen dat de woning bewoonbaar is voor iemand met een
    rolstoel. Deze persoon kan de voordeur van de woning zelfstandig bereiken, kan
    de voordeur zelfstandig openen en passeren, kan de woonkamer, het toilet, de
    doucheruimte, de keuken  en een slaapkamer bereiken en gebruiken. De woonkamer,
    het toilet, de doucheruimte, de keuken  en een slaapkamer bevinden zich op de
    begane grond of zijn met een lift of een plateaulift (geschikt voor rolstoel)
    bereikbaar. Drempels zijn maximaal 20 mm hoog en hellingen zijn flauw. De vrije
    doorgang is nooit smaller dan 800 mm. Eventuele bochten om in de woonkamer of
    bij het toilet te komen voldoen (X+Y is groter dan 1950 mm).
    """

    zorg = BatscoreReferentiedata(
        code="BAT5",
        naam="Zorg",
    )
    """
    In de slaapkamer en in de doucheruimte is ruimte voor het geven van hulp. Naast het
    bed is 1,3 m ruimte voor een tillift en voor een douche- toiletrolstoel.
    """
