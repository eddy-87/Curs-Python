while True:
    try:
        print("Introdu x: ", end = '')
        x = int(input())

        for i in range (1, x, 2):
            print (i)
        break

    except ValueError:
        print("Introdu un numar, nu o litera")