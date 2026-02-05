inventar = {}

def gestioneaza_inventar():
    while True:
        print("\n1. Adauga produs | 2. Cauta produs | 3. Actualizeaza stoc | 4. Iesire")
        optiune = input("Alege o optiune: ")

        if optiune == "4":
            break

        try:
            if optiune == "1":
                nume = input("Nume produs: ")
                if nume in inventar:
                    raise ValueError("Produsul exista deja.")
                cantitate = int(input("Cantitate: "))
                if cantitate < 0:
                     raise ValueError("Cantitatea nu poate fi negativa.")
                inventar[nume] = cantitate
                print(f"Produsul {nume} a fost adaugat.")

            elif optiune == "2":
                nume = input("Nume produs de cautat: ")
                if nume in inventar:
                    print(f"Stoc {nume}: {inventar[nume]}")
                else:
                    raise KeyError("Produsul nu a fost gasit.")

            elif optiune == "3":
                nume = input("Nume produs: ")
                if nume not in inventar:
                    raise KeyError("Produsul nu exista in inventar.")
                cantitate_noua = int(input("Noua cantitate: "))
                if cantitate_noua < 0:
                    raise ValueError("Cantitatea nu poate fi negativa.")
                inventar[nume] = cantitate_noua
                print("Stoc actualizat.")

            else:
                print("Optiune invalida.")

        except ValueError as e:
            print(f"Eroare de valoare: {e}")
        except KeyError as e:
            print(f"Eroare de produs: {e}")
        except Exception as e:
            print(f"A aparut o eroare neasteptata: {e}")