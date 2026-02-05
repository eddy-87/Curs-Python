def calculeaza_suma_fisier(nume_fisier):
    suma = 0
    try:
        with open(nume_fisier, 'r') as f:
            for linie in f:
                linie = linie.strip()
                if not linie: continue
                try:
                    numar = float(linie)
                    suma += numar
                except ValueError:
                    print(f"Avertisment: '{linie}' nu este un număr valid.")
        return suma

    except FileNotFoundError:
        print("Eroare: Fișierul nu a fost găsit.")
        return 0
    except IOError:
        print("Eroare: Probleme la citirea fișierului.")
        return 0