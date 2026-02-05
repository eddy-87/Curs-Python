import os

nume_folder = "fisiere_test"

if not os.path.exists(nume_folder):
    os.makedirs(nume_folder)
    open(os.path.join(nume_folder, "document.txt"), "w").close()
    open(os.path.join(nume_folder, "poza.jpg"), "w").close()

for fisier in os.listdir(nume_folder):
    cale_veche = os.path.join(nume_folder, fisier)

    if os.path.isfile(cale_veche) and not fisier.startswith("renamed_"):
        nume_nou = "renamed_" + fisier
        cale_noua = os.path.join(nume_folder, nume_nou)
        os.rename(cale_veche, cale_noua)
        print(f"Redenumit: {fisier} -> {nume_nou}")