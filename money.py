"""Monetary helpers for the store.

All money is handled as integer **cents** internally to avoid floating-point
drift (0.1 + 0.2 != 0.3), and only formatted back to a decimal string at the
display boundary. Import these helpers rather than re-deriving the math.
"""

from __future__ import annotations

CENTS_PER_UNIT = 100


def to_cents(amount: float) -> int:
    """Convert a currency amount to integer cents, e.g. 12.99 -> 1299."""
    return round(amount * CENTS_PER_UNIT)


def format_money(cents: int) -> str:
    """Format integer cents as a 2-decimal string, e.g. 1299 -> '12.99'."""
    return f"{cents / CENTS_PER_UNIT:.2f}"


def apply_percentage_discount(cents: int, percent: float) -> int:
    """Return `cents` reduced by `percent` (0–100), rounded to whole cents.

    This is the single source of truth for percentage discounts: it validates
    the range and returns the *discounted price*, not the discount amount.

    Raises:
        ValueError: if `percent` is outside the inclusive range [0, 100].
    """
    if not 0 <= percent <= 100:
        raise ValueError(f"percent must be between 0 and 100, got {percent}")
    discount = round(cents * percent / 100)
    return cents - discount
