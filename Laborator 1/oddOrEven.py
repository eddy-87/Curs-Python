while True:
    valoare = input("Introdu un numar intreg: ")

    try:
        numar = int(valoare)
        break
    except ValueError:
        print("Eroare: te rog introdu un numar intreg (fara litere, fara virgula)\n")

if numar % 2 == 0:
    print("Numarul", numar, "este par")
else:
    print("Numarul", numar, "este impar")
