def calculate_bean_cost(bag_price: float, bags: int) -> float:
    return bag_price * bags

def get_bulk_discount(bags: int, partner: bool = False) -> float:
    if bags < 20: 
        discount = 0.0
    elif 20 <= bags <= 79:
        discount = 0.09
    else:
        discount = 0.14

        if partner and bags >= 20:
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

def largest_shipment(shipments: list) -> str:
    largest_total = float('-inf')
    largest_buyer = ""

    for shipment in shipments:
        shipment_total = calculate_shipment_total(
            shipment["bag_price"],
            shipment["bags"],
            shipment.get("partner", False)
        )

        if shipment_total > largest_total:
            largest_total = shipment_total
            largest_buyer = shipment["buyer"]

    return largest_buyer

def format_shipment_line(
    buyer: str, total: float, prepayment: bool, pallet: bool) -> str:
    prepayment_text = "yes" if prepayment else "no"
    pallet_text = "yes" if pallet else "no"

    return (
        f"{buyer}: ${total:.2f} | "
        f"prepayment: {prepayment_text} | "
        f"pallet: {pallet_text}"
    )





    
