"""Tests for checkout totals and coupon handling."""

from checkout import LineItem, apply_coupon, order_total, subtotal


def _cart() -> list[LineItem]:
    # 1000*2 + 500*1 = 2500 cents
    return [LineItem("widget", 1000, 2), LineItem("gadget", 500, 1)]


def test_subtotal_sums_line_items():
    assert subtotal(_cart()) == 2500


def test_order_total_applies_order_discount():
    assert order_total(_cart(), 10) == 2250


def test_apply_coupon_valid_code_discounts_price():
    assert apply_coupon(1000, "SAVE10") == 900   # 10% off
    assert apply_coupon(1000, "SAVE20") == 800   # 20% off


def test_apply_coupon_unknown_code_gives_no_discount():
    # Invalid / unrecognized code → 0% discount → price unchanged.
    assert apply_coupon(1000, "DOESNOTEXIST") == 1000


def test_apply_coupon_zero_percent_returns_original_price():
    # A code that resolves to a 0% discount must return the exact original cents.
    assert apply_coupon(1299, "") == 1299


def test_apply_coupon_returns_integer_cents():
    result = apply_coupon(999, "SAVE10")  # 999 - round(99.9) = 899
    assert result == 899
    assert isinstance(result, int)


def test_apply_coupon_empty_code_gives_no_discount():
    assert apply_coupon(1000, "") == 1000


def test_apply_coupon_rounds_fractional_cents():
    # 10% of 99 cents = 9.9 → rounds to 10 cents off → 89.
    assert apply_coupon(99, "SAVE10") == 89


def test_apply_coupon_rounds_across_magnitudes():
    # 10% of 12345 = 1234.5 → banker's rounding → 1234 off → 11111.
    assert apply_coupon(12345, "SAVE10") == 11111
