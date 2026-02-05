text = input("Introdu numerele separate prin virgula: ")
lista_string = text.split(",")
lista_numere = []

for element in lista_string:
    lista_numere.append(int(element.strip()))

print("Maximul:", max(lista_numere))
print("Minimul:", min(lista_numere))