def live_silver_price(api_key):
    if not api_key.strip():
        raise ValueError("Enter your GoldAPI key.")

    response = requests.get(
        "https://www.goldapi.io/api/price/XAG/USD",
        headers={
            "x-access-token": api_key.strip()
        },
        timeout=15,
        allow_redirects=False
    )

    if response.status_code != 200:
        raise ValueError(
            "GoldAPI error: " + str(response.status_code)
        )

    data = response.json()
    ounce_price = number(data["price"], "Silver price")

    if ounce_price <= 0:
        raise ValueError("Silver price must be greater than zero.")

    return ounce_price


def get_exchange_rate():
    response = requests.get(
        "https://api.frankfurter.dev/v2/rate/usd/thb",
        timeout=15
    )

    response.raise_for_status()

    data = response.json()
    exchange_rate = number(data["rate"], "Exchange rate")

    if exchange_rate <= 0:
        raise ValueError("Exchange rate must be greater than zero.")

    return exchange_rate, data["date"]
