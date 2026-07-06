"""Tests for the discount helpers."""

from discounts import apply_discount


def test_apply_discount_reduces_price():
    assert apply_discount(1000, 10) == 900


def test_apply_discount_zero_percent_is_noop():
    assert apply_discount(1000, 0) == 1000
