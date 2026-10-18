import math


def number(value, name):
    try:
        value = float(value)
    except (ValueError, TypeError):
        raise ValueError(name + " must be a number.")

    if not math.isfinite(value):
        raise ValueError(name + " must be a finite number.")

    if value < 0 or value > 100000000:
        raise ValueError(name + " must be between 0 and 100000000.")

    return value


def calculate_cost(silver_weight_g, silver_price_oz, wastage_percent,
                   labor_cost, stone_cost, quantity, wholesale_markup,
                   exchange_rate, Tax, shipping_fees):

    silver_price_g = silver_price_oz / 31.1034768 * exchange_rate

    Silver_Cost = silver_weight_g * silver_price_g
    Wastage_Cost = Silver_Cost * wastage_percent / 100

    T_Cost = Silver_Cost + Wastage_Cost + labor_cost + stone_cost

    Wholesale_price = round(T_Cost * (1 + wholesale_markup / 100), 2)
    Raw_Quotation = round(Wholesale_price * quantity, 2)

    Tax_Cost = round(Raw_Quotation * Tax / 100, 2)
    Final_Quotation = round(Raw_Quotation + Tax_Cost + shipping_fees, 2)

    return {
        "silver_price_g": silver_price_g,
        "Silver_Cost": round(Silver_Cost, 2),
        "Wastage_Cost": round(Wastage_Cost, 2),
        "T_Labor_Cost": round(labor_cost, 2),
        "T_Cost": round(T_Cost, 2),
        "Wholesale_price": Wholesale_price,
        "Raw_Quotation": Raw_Quotation,
        "Tax_Cost": Tax_Cost,
        "Final_Quotation": Final_Quotation
    }
