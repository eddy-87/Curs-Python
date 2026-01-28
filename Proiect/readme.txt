Calculator de Trasee si Distante (OpenStreetMap / OSRM)

Acest proiect este o aplicatie GUI realizata cu Python si Tkinter, care permite utilizatorilor sa calculeze distanta intre doua locatii si sa vizualizeze traseul pe o harta interactiva generata cu Folium. Pentru obtinerea rutelor auto (driving) foloseste OSRM (Open Source Routing Machine) bazat pe OpenStreetMap, fara Google Maps API si fara Billing, deci nu este necesara nicio cheie API.

Caracteristici:
- Introducerea a doua locatii pentru calculul distantei.
- Obtinerea coordonatelor GPS ale locatiilor folosind Geopy (Nominatim / OpenStreetMap).
- Calculul distantei "in linie dreapta" dintre locatii folosind geodesic.
- Obtinerea rutelor auto (driving) si a alternativelor folosind OSRM (gratuit).
- Generarea unei harti interactive cu Folium.
- Afisarea rutelor alternative pe harta cu culori diferite.
- Interfata prietenoasa cu Tkinter si fundal personalizat (optional) cu harta_fundal.jpg.

Instalare pachete:
pip install requests geopy folium pillow

Configurare:
1) Cloneaza sau descarca proiectul pe PC.
2) (Optional) Pune o imagine de fundal numita "harta_fundal.jpg" in acelasi folder cu scriptul.
   Daca fisierul nu exista, aplicatia porneste fara fundal (nu da crash).
3) Nu este necesara nicio cheie API deoarece proiectul nu foloseste Google Maps.

Utilizare:
1) Ruleaza scriptul Python (exemplu):
   python ProiectDistanta.py
2) Introdu locatiile dorite (ex: "Sibiu, Romania" si "Cluj-Napoca, Romania").
3) Apasa butonul "Calculeaza Traseul si Distanta".
4) Harta interactiva se va salva ca "trasee_detaliate.html" si se va deschide automat in browser.

Note:
- Geocodarea foloseste Nominatim (OpenStreetMap). Daca o locatie nu este gasita, incearca o forma mai completa (oras + tara).
- Rutele sunt obtinute prin serviciul public OSRM (router.project-osrm.org). Pentru utilizare intensa, se recomanda rularea unui server OSRM propriu.