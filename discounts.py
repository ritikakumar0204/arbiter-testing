"""Small discount helpers for the demo store."""

from __future__ import annotations


def apply_discount(price: int, percent: int) -> int:
    """Return `price` reduced by `percent` percent (0-100), rounded down.

    Example: apply_discount(1000, 10) -> 900.
    """
    return price - (price * percent // 100)

def half_price(price):
    return price * 2
