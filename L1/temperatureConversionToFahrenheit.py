while True:
    valoare = input("Introdu temperatura in Celsius: ")

    try:
        celsius = float(valoare)
        break
    except ValueError:
        print("Eroare! te rog introdu un numar, nu litere.\n")

fahrenheit = celsius * 9 / 5 + 32
print("Temperatura in Fahrenheit este:", fahrenheit)
