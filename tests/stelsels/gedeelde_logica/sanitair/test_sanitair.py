from decimal import Decimal

from woningwaardering.stelsels.gedeelde_logica.sanitair.sanitair import (
    _puntenwinst_wastafel_maximering,
)


def test_puntenwinst_wastafel_maximering() -> None:
    # 3 wastafels: (3-1)*1 = 2, gedeeld door 8.
    assert _puntenwinst_wastafel_maximering(3, 0, 8) == Decimal("0.25")
    # 2 meerpersoonswastafels: (2-1)*1,5 = 1,5, gedeeld door 8.
    assert _puntenwinst_wastafel_maximering(0, 2, 8) == Decimal("1.5") / Decimal("8")
    # 2 wastafels + 2 meerpersoonswastafels: 1 + 1,5 = 2,5, gedeeld door 8.
    assert _puntenwinst_wastafel_maximering(2, 2, 8) == Decimal("2.5") / Decimal("8")
    # 4 wastafels winnen van 2+2: 3,0 > 2,5 (puntenwinst, niet ruwe punten).
    assert _puntenwinst_wastafel_maximering(4, 0, 8) > _puntenwinst_wastafel_maximering(
        2, 2, 8
    )
    # Na delen: 2/8 = 0,25 wint van 4/20 = 0,20.
    assert _puntenwinst_wastafel_maximering(3, 0, 8) > _puntenwinst_wastafel_maximering(
        5, 0, 20
    )
    assert _puntenwinst_wastafel_maximering(1, 1, 8) == Decimal("0")
