from forex_python.converter import CurrencyRates


def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    try:
        rate = c.get_rate(from_currency, to_currency)
        converted_amount = round(amount * rate, 2)
        return converted_amount
    except:
        print(f"Impossible de récupérer le taux de change pour {from_currency} vers {to_currency}. La conversion n'est pas possible.")
        return None

def save_conversion_history(history_entry):
    with open("conversion_history.txt", "a") as file:
        file.write(history_entry + "\n")

def display_conversion_history():
    with open("conversion_history.txt", "r") as file:
        history_entries = file.readlines()
        for entry in history_entries:
            print(entry.strip())

def main():
    amount = float(input("Entrez le montant à convertir : "))
    from_currency = input("Entrez la devise d'origine (ex. USD) : ").upper()
    to_currency = input("Entrez la devise souhaitée (ex. EUR) : ").upper()

    converted_amount = convert_currency(amount, from_currency, to_currency)

    if converted_amount is not None:
        print(f"{amount} {from_currency} équivaut à {converted_amount} {to_currency}")

        history_entry = f"{amount} {from_currency} to {converted_amount} {to_currency}"
        save_conversion_history(history_entry)

        display_conversion_history()

if __name__ == "__main__":
    main()
