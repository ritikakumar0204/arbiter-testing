"""Checkout totals, built on top of the money helpers.

Keeps cart math in one place so callers get consistent, cents-based totals.
"""

from __future__ import annotations

from dataclasses import dataclass

from money import apply_percentage_discount, format_money


@dataclass(frozen=True)
class LineItem:
    """A single cart line: a product at a unit price, times a quantity."""

    name: str
    unit_price_cents: int
    quantity: int


def subtotal(items: list[LineItem]) -> int:
    """Sum every line item, returning the subtotal in cents."""
    return sum(item.unit_price_cents * item.quantity for item in items)


def order_total(items: list[LineItem], discount_percent: float = 0.0) -> int:
    """Subtotal reduced by an optional order-level percentage discount (in cents)."""
    return apply_percentage_discount(subtotal(items), discount_percent)


def receipt(items: list[LineItem], discount_percent: float = 0.0) -> str:
    """Render a human-readable total line, e.g. 'Total: 42.00'."""
    return f"Total: {format_money(order_total(items, discount_percent))}"

COUPONS = {"SAVE10": 10, "SAVE20": 20}

def apply_coupon(cents: int, code: str) -> int:
    """Apply coupon `code` to `cents`, returning the discounted price in cents."""
    return apply_percentage_discount(cents, COUPONS.get(code, 0))


