while True:
    valoare = input("Introdu suma initiala: ")
    try:
        principal = float(valoare)
        break
    except ValueError:
        print("Eroare: te rog introdu un numar valid\n")

while True:
    valoare = input("Introdu rata anuala a dobanzii (%): ")
    try:
        rate = float(valoare)
        break
    except ValueError:
        print("Eroare: te rog introdu un numar valid\n")

while True:
    valoare = input("Introdu timpul in ani: ")
    try:
        time = float(valoare)
        break
    except ValueError:
        print("Eroare: te rog introdu un numar valid\n")

interest = (principal * rate * time) / 100

print("\nDobanda este:", interest)
