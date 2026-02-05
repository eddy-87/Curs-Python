def imparte_numere(a, b):
    try:
        rezultat = a / b
        return rezultat
    except ZeroDivisionError:
        return "Eroare: Nu se poate împărți la zero!"

print(imparte_numere(10, 2))
print(imparte_numere(5, 0))