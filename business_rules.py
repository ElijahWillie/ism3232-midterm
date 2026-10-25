def calculate_bean_cost(bag_price: float, bags: int) -> float:
    return bag_price * bags

def get_bulk_discount(bags: int, partner: bool = False) -> float:
    if bags < 20: 
        discount = 0.0
    elif bags < 80:
        discount = 0.09
    else:
        discount = 0.14

        if partner and bags >=20:
            discount += 0.04

        return discount 


def calculate_shipment_total(
    bag_price: float, bags: int, partner: bool = False) -> float:
    bean_cost = calculate_bean_cost(bag_price, bags)
    discount = get_bulk_discount(bags, partner)

    discounted_cost = bean_cost * (1 - discount)

    if discounted_cost < 250: 
        return discounted_cost + 35

    return discounted_cost

def requires_prepayment(total: float) -> bool:
    return total >= 1500

def needs_pallet(bags: int, total: float) -> bool:
    return bags > 60 and total > 700

def total_shipped(shipments: list) -> float:
    total = 0.0

    for shipment in shipments:
        shipment_total = calculate_shipment_total(
            shipment["bag_price"],
            shipment["bags"],
            shipment.get("partner", False),
        )
        total += shipment_total

    return total






    
