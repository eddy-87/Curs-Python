text = input("Introdu numerele separate prin virgula: ")
lista_initiala = [x.strip() for x in text.split(",")]
lista_unica = []

for x in lista_initiala:
    if x not in lista_unica:
        lista_unica.append(x)

print(", ".join(lista_unica))