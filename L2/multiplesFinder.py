while True:
    try:
        print("Introdu x: ", end = '')
        x = int(input())
        print("Introdu y: ", end = '')
        y = int(input())

        if x == 0:
            print("x nu poate fi 0, introdu alt numar")
            continue

        if x < 0:
            print("x trebuie sa fie un numar pozitiv")
            continue

        if y < x or y < 0:
            print("y trebuie sa fie un numar mai mare decat x si pozitiv, introdu un alt numar")
            continue

        print("Multiplii sunt: ")

        for i in range(x, y, x):
            print(i)
        break

    except ValueError:
        print("Introdu un numar, nu o litera")