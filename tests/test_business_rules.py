from business_rules import (
    calculate_bean_cost,
    get_bulk_discount,
    calculate_shipment_total,
    requires_prepayment,
    needs_pallet,
    total_shipped,
    largest_shipment,
    format_shipment_line,
)


# RULE 1: Calculate bean cost


def test_bean_cost_multiplies_price_by_bags():
    assert round(calculate_bean_cost(14.00, 10), 2) == 140.00


def test_bean_cost_with_decimal_price():
    assert round(calculate_bean_cost(13.25, 4), 2) == 53.00


# RULES 2 AND 3: Bulk and partner discounts


def test_discount_at_19_bags_is_zero():
    assert get_bulk_discount(19) == 0.0


def test_discount_at_20_bags_is_nine_percent():
    assert get_bulk_discount(20) == 0.09


def test_discount_at_79_bags_is_nine_percent():
    assert get_bulk_discount(79) == 0.09


def test_discount_at_80_bags_is_fourteen_percent():
    assert get_bulk_discount(80) == 0.14


def test_partner_below_20_bags_gets_no_extra_discount():
    assert get_bulk_discount(19, True) == 0.0


def test_partner_at_20_bags_gets_thirteen_percent():
    assert get_bulk_discount(20, True) == 0.13


def test_partner_at_80_bags_gets_eighteen_percent():
    assert round(get_bulk_discount(80, True), 2) == 0.18


# RULE 4: Shipment totals and shipping fees


def test_shipping_fee_when_discounted_cost_just_below_250():
    assert round(calculate_shipment_total(249.99, 1), 2) == 284.99


def test_no_shipping_fee_when_discounted_cost_equals_250():
    assert round(calculate_shipment_total(250.00, 1), 2) == 250.00


def test_shipping_fee_uses_discounted_cost_not_original_cost():
    assert round(calculate_shipment_total(12.50, 20), 2) == 262.50


def test_regular_shipment_without_shipping_fee():
    assert round(calculate_shipment_total(10.00, 30), 2) == 273.00


def test_partner_true_changes_yarrow_shipment_total():
    assert round(calculate_shipment_total(12.00, 50), 2) == 546.00
    assert round(calculate_shipment_total(12.00, 50, True), 2) == 522.00


# RULE 5: Prepayment requirements


def test_prepayment_just_below_1500_is_false():
    assert requires_prepayment(1499.99) is False


def test_prepayment_exactly_1500_is_true():
    assert requires_prepayment(1500.00) is True


def test_prepayment_just_above_1500_is_true():
    assert requires_prepayment(1500.01) is True


# RULE 6: Freight pallet requirements


def test_pallet_at_60_bags_with_high_total_is_false():
    assert needs_pallet(60, 701.00) is False


def test_pallet_at_61_bags_with_high_total_is_true():
    assert needs_pallet(61, 701.00) is True


def test_pallet_at_700_total_with_enough_bags_is_false():
    assert needs_pallet(61, 700.00) is False


def test_pallet_above_700_total_with_enough_bags_is_true():
    assert needs_pallet(61, 700.01) is True


# FUNCTION 6: Total shipped


def test_total_shipped_adds_short_list():
    shipments = [
        {"buyer": "A", "bag_price": 14.00, "bags": 10, "partner": False},
        {"buyer": "B", "bag_price": 10.00, "bags": 30, "partner": False},
    ]
    assert round(total_shipped(shipments), 2) == 448.00


def test_total_shipped_includes_partner_discounts():
    shipments = [
        {"buyer": "Vine Cafe", "bag_price": 12.50, "bags": 15, "partner": True},
        {"buyer": "Yarrow Cafe", "bag_price": 12.00, "bags": 50, "partner": True},
    ]
    assert round(total_shipped(shipments), 2) == 744.50


def test_total_shipped_empty_list_is_zero():
    assert round(total_shipped([]), 2) == 0.00


# FUNCTION 7: Largest shipment


def test_largest_shipment_returns_highest_buyer():
    shipments = [
        {"buyer": "First", "bag_price": 14.00, "bags": 10, "partner": False},
        {"buyer": "Second", "bag_price": 10.00, "bags": 30, "partner": False},
    ]
    assert largest_shipment(shipments) == "Second"


def test_largest_shipment_tie_returns_first_buyer():
    shipments = [
        {"buyer": "First", "bag_price": 10.00, "bags": 30, "partner": False},
        {"buyer": "Second", "bag_price": 10.00, "bags": 30, "partner": False},
    ]
    assert largest_shipment(shipments) == "First"


def test_largest_shipment_empty_list_returns_empty_string():
    assert largest_shipment([]) == ""


# FUNCTION 8: Format shipment line


def test_format_shipment_line_with_no_flags():
    assert format_shipment_line("Uptown Bakery", 175.00, False, False) == (
        "Uptown Bakery: $175.00 | prepayment: no | pallet: no"
    )


def test_format_shipment_line_with_both_flags():
    assert format_shipment_line("Cove Market", 1599.00, True, True) == (
        "Cove Market: $1599.00 | prepayment: yes | pallet: yes"
    )


def test_format_shipment_line_with_mixed_flags_and_two_decimals():
    assert format_shipment_line("Sample Shop", 20.50, True, False) == (
        "Sample Shop: $20.50 | prepayment: yes | pallet: no"
    )
