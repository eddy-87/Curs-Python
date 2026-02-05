import requests

try:
    moneda_sursa = input("Moneda de provenienta (ex: USD, EUR, RON): ").upper()
    moneda_destinatie = input("Moneda de destinatie (ex: EUR, USD, RON): ").upper()
    suma = float(input("Suma de convertit: "))

    url = f"https://open.er-api.com/v6/latest/{moneda_sursa}"
    response = requests.get(url)
    data = response.json()

    if moneda_destinatie in data['rates']:
        rata = data['rates'][moneda_destinatie]
        rezultat = suma * rata
        print(f"\nRezultat: {suma} {moneda_sursa} = {rezultat:.2f} {moneda_destinatie}")
        print(f"Curs de schimb: 1 {moneda_sursa} = {rata} {moneda_destinatie}")
    else:
        print("Moneda invalida.")

except Exception as e:
    print(f"A aparut o eroare: {e}")