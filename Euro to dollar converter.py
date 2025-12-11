import requests
from dotenv import dotenv_values

#'t Is me niet gelukt om de API token af te schermen van m'n code zonder dat het script crashte, wellicht
# dat we daar even naar kunnen kijken tijdens de les?

def get_exchange_rate(api_key, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/EUR"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        conversion_rates = data.get("conversion_rates", {})

        if target_currency in conversion_rates:
            return conversion_rates[target_currency]
        else:
            print(f"ERROR: {target_currency} exchange rate not found.")
            return None
    else:
        print(f"ERROR {response.status_code} - {response.text}")
        return None


def convert_currency(amount, exchange_rate):
    return amount * exchange_rate


def main():
    values = dotenv_values(".env")
    api_key = values.get("API_KEY", "c3e3f1d2472a0198fdaad29d")

    while True:
        try:
            eur_amount = float(input("Enter amount in EUR: ").strip())
            target_currency = input("Enter target currency (e.g. USD, GBP, JPY): ").strip().upper()
            exchange_rate = get_exchange_rate(api_key, target_currency)

            if exchange_rate:
                converted_amount = convert_currency(eur_amount, exchange_rate)
                print(
                    f"\n{eur_amount:.2f} EUR = {converted_amount:.2f} {target_currency} (exchange rate: {exchange_rate})")
                break
            else:
                print("Invalid currency code. Please try again.\n")
        except ValueError:
            print("Invalid amount. Please enter a numeric value.\n")


if __name__ == "__main__":
    main()
