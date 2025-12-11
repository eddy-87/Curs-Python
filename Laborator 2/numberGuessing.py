import random

a = 1
b = 20
nr_aleator = random.choices(range(a,b))


while True:
    try:
        print("Ghiceste numarul: ", end='')
        nr_ghicit = input()

        if int (nr_ghicit) < int (nr_aleator[0]):
            print("Prea mic")

        if int (nr_ghicit) > int (nr_aleator[0]):
            print("Prea mare")

        if int (nr_ghicit) == int (nr_aleator[0]):
            print("Ai ghicit numarul!")
            break

    except ValueError:
        print("Introdu un numar, nu o litera")