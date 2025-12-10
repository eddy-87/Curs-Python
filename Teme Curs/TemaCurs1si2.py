while True:
    ch = input("Introdu un caracter: ")

    if ch.isalpha():
        print("Litera:", ch)
    else:
        print("Eroare!")
        break
