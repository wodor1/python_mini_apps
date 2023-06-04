from forex_python.converter import CurrencyRates

def main():
    # Létrehozunk egy CurrencyRates objektumot
    cr = CurrencyRates()

    # Bekérjük a felhasználótól a szükséges információkat
    amount = float(input("Add meg az összeget: "))
    from_currency = input("Add meg a pénznemet (pl. USD, EUR, HUF, stb.): ").upper()
    to_currency = input("Melyik pénznembe szeretnéd átváltani (pl. USD, EUR, HUF, stb.): ").upper()

    # Meghívjuk a convert metódust az átváltáshoz
    result = cr.convert(from_currency, to_currency, amount)

    # Kiírjuk a végeredményt
    print(f"{amount} {from_currency} = {result} {to_currency}")

if __name__ == "__main__":
    main()
