while True:
    try:
        print("Introdu un numar: ", end='')
        numar = input()
        if int (numar) < 60:
            print("Nota F")
        elif int (numar) >= 60 and int (numar) <= 69:
            print ("Nota D")
        elif int (numar) >= 70 and int (numar) <= 79:
            print ("Nota C")
        elif int (numar) >= 80 and int (numar) <= 89:
            print ("Nota B")
        elif int (numar) >= 90 and int (numar) <= 100:
            print ("Nota A")
        break

    except ValueError:
        print("Intro un numar, nu o litera")

