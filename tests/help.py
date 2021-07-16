from decimal import Decimal


def float_format(value: float) -> Decimal:
    return Decimal(value).quantize(Decimal("1.00"))
