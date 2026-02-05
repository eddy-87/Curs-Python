import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

try:
    url_crypto = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    response = requests.get(url_crypto)
    response.raise_for_status()
    data = response.json()

    tabel_crypto = [
        ["Bitcoin", f"{data['bitcoin']['usd']} USD"],
        ["Ethereum", f"{data['ethereum']['usd']} USD"]
    ]
    print("Preturi Criptomonede:")
    print(tabulate(tabel_crypto, headers=["Moneda", "Pret"], tablefmt="grid"))

except Exception as e:
    print(f"Eroare API Crypto: {e}")

print("\nStiri recente CoinDesk:")
try:
    url_news = "https://www.coindesk.com/"
    response = requests.get(url_news)
    soup = BeautifulSoup(response.content, 'html.parser')

    stiri = []
    titluri = soup.find_all(['h2', 'h3', 'h4', 'h5', 'h6'], limit=15)

    for titlu in titluri:
        link_tag = titlu.find_parent('a') or titlu.find('a')
        if link_tag and link_tag.get('href'):
            text = titlu.get_text().strip()
            link = link_tag.get('href')
            if not link.startswith('http'):
                link = "https://www.coindesk.com" + link

            if text and len(stiri) < 5:
                stiri.append([text, link])

    print(tabulate(stiri, headers=["Titlu", "Link"], tablefmt="grid"))

except Exception as e:
    print(f"Eroare la scraping: {e}")