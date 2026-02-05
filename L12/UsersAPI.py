import requests
from tabulate import tabulate

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url)
    response.raise_for_status()
    users = response.json()

    date_tabel = []
    headers = ["ID", "Nume", "Email", "Oras", "Companie", "Telefon", "Website"]

    for user in users:
        row = [
            user['id'],
            user['name'],
            user['email'],
            user['address']['city'],
            user['company']['name'],
            user['phone'],
            user['website']
        ]
        date_tabel.append(row)

    print("Toti utilizatorii:")
    print(tabulate(date_tabel, headers=headers, tablefmt="grid"))

    oras_filtru = "Gwenborough"
    date_filtrate = [row for row in date_tabel if row[3] == oras_filtru]

    print(f"\nUtilizatori din {oras_filtru}:")
    print(tabulate(date_filtrate, headers=headers, tablefmt="grid"))

except requests.exceptions.RequestException as e:
    print(f"Eroare la conectarea API: {e}")