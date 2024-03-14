from vera import referentiedata
from vera.bvg.models import EenhedenRuimte, EenhedenEenheid
from vera.referentiedata.models import Referentiedata

ref1 = Referentiedata(
    code="IRF",
    naam="Inkomensregistratieformuliers",
)
ref2 = referentiedata.Dossier.AUTHENTIEKGEGEVENBRON.inkomensregistratieformulier
print(ref1 == ref2)


def dummy_function() -> None:
    eenheid = EenhedenEenheid()
    eenheid.ruimten = [
        EenhedenRuimte(
            oppervlakte=25,
            soort=referentiedata.Dossier.AUTHENTIEKGEGEVENBRON.inkomensregistratieformulier,
        )
    ]
    print(eenheid.to_json())


dummy_function()
