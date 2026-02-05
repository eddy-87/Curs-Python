import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

oras = input("Introdu numele orasului: ")
url = f"https://wttr.in/{oras}?format=%C\n%t\n%w"

try:
    response = requests.get(url, verify=False)

    if response.status_code == 200:
        linii = response.text.strip().split('\n')
        if len(linii) >= 3:
            print(f"Conditii: {linii[0]}")
            print(f"Temperatura: {linii[1]}")
            print(f"Vant: {linii[2]}")
        else:
            print("Datele nu au putut fi interpretate.")
    else:
        print("Orasul nu a fost gasit sau eroare API.")

except requests.exceptions.RequestException as e:
    print(f"Eroare la conectare: {e}")