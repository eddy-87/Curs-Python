text = input("Introdu valorile separate prin virgula: ")
tupla_elemente = tuple(x.strip() for x in text.split(","))

cautat = input("search for: ")

if cautat in tupla_elemente:
    index = tupla_elemente.index(cautat)
    print(f"{cautat} se regaseste in tupla la indexul {index}.")
else:
    print(f"{cautat} nu se regaseste in tupla.")