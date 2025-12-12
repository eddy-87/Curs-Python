while True:
        cuvant_initial = str(input())

        if not cuvant_initial.isalpha():
            print("Sunt doar aceptate litere, nu numere")
            continue

        cuvant_mic = cuvant_initial.lower()

        cuvant_final = str
        if str(cuvant_final) == cuvant_mic[::-1]:
            print("TRUE")