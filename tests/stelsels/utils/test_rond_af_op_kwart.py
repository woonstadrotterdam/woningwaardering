from decimal import Decimal

import pytest

from woningwaardering.stelsels.utils import rond_af_op_kwart


def test_rond_af_op_kwart():
    # floats
    assert rond_af_op_kwart(0.125) == Decimal("0.25")
    assert rond_af_op_kwart(0.3) == Decimal("0.25")
    assert rond_af_op_kwart(0.55) == Decimal("0.5")
    assert rond_af_op_kwart(0.6) == Decimal("0.5")
    assert rond_af_op_kwart(0.625) == Decimal("0.75")
    assert rond_af_op_kwart(1.2) == Decimal("1.25")
    assert rond_af_op_kwart(1.875) == Decimal("2.0")

    # Decimals
    assert rond_af_op_kwart(Decimal("0.125")) == Decimal("0.25")
    assert rond_af_op_kwart(Decimal("0.55")) == Decimal("0.5")
    assert rond_af_op_kwart(Decimal("0.625")) == Decimal("0.75")

    # ints
    assert rond_af_op_kwart(1) == Decimal("1.0")
    assert rond_af_op_kwart(2) == Decimal("2.0")

    # Test value error
    with pytest.raises(ValueError):
        rond_af_op_kwart(None)
