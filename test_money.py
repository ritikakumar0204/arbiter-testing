"""Tests for the money helpers."""

import pytest

from money import apply_percentage_discount, format_money, to_cents


def test_to_cents_rounds_to_whole_cents():
    assert to_cents(12.99) == 1299
    assert to_cents(0.1 + 0.2) == 30  # would be 0.30000000000000004 as a float


def test_format_money_pads_two_decimals():
    assert format_money(1299) == "12.99"
    assert format_money(5) == "0.05"


def test_apply_percentage_discount_returns_discounted_price():
    assert apply_percentage_discount(1000, 10) == 900
    assert apply_percentage_discount(1000, 0) == 1000
    assert apply_percentage_discount(1000, 100) == 0


def test_apply_percentage_discount_rejects_out_of_range():
    with pytest.raises(ValueError):
        apply_percentage_discount(1000, 150)
    with pytest.raises(ValueError):
        apply_percentage_discount(1000, -5)
