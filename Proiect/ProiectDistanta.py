import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import requests
import folium
import webbrowser
from PIL import Image, ImageTk
import os

# Culori trasee
route_colors = ["blue", "red", "green", "purple", "orange", "brown", "pink"]

OSRM_BASE = "https://router.project-osrm.org"  # gratuit (public)

def get_osrm_routes(coords1, coords2):
    """
    coords1/coords2: (lat, lon)
    Returneaza lista de rute, fiecare ruta = lista puncte [(lat, lon), ...]
    """
    lat1, lon1 = coords1
    lat2, lon2 = coords2

    # OSRM vrea lon,lat in URL
    url = (
        f"{OSRM_BASE}/route/v1/driving/"
        f"{lon1},{lat1};{lon2},{lat2}"
        f"?overview=full&geometries=geojson&alternatives=true&steps=false"
    )

    r = requests.get(url, timeout=20, headers={"User-Agent": "route_calculator"})
    r.raise_for_status()
    data = r.json()

    if data.get("code") != "Ok" or not data.get("routes"):
        # OSRM foloseste "code": "Ok"
        raise RuntimeError(f"OSRM error: {data.get('code')}")

    routes_points = []
    for route in data["routes"]:
        # GeoJSON: coordinates = [[lon, lat], [lon, lat], ...]
        coords = route["geometry"]["coordinates"]
        points = [(lat, lon) for lon, lat in coords]
        routes_points.append(points)

    return routes_points

def calculate_route():
    loc1 = entry_location1.get().strip()
    loc2 = entry_location2.get().strip()

    if not loc1 or not loc2:
        messagebox.showerror("Eroare", "Introduceti ambele locatii!")
        return

    geolocator = Nominatim(user_agent="route_calculator_gui", timeout=10)

    try:
        location1 = geolocator.geocode(loc1)
        location2 = geolocator.geocode(loc2)

        if not location1 or not location2:
            messagebox.showerror("Eroare", "Nu s-au gasit locatiile specificate!")
            return

        coords1 = (location1.latitude, location1.longitude)
        coords2 = (location2.latitude, location2.longitude)

        # Distanta "in linie dreapta" (geodesic)
        distance_km = geodesic(coords1, coords2).kilometers

        # Rute reale (driving) via OSRM
        routes_points = get_osrm_routes(coords1, coords2)

        # Creeaza harta
        map_ = folium.Map(location=[location1.latitude, location1.longitude], zoom_start=12)
        folium.Marker(coords1, popup=f"Start: {location1.address}").add_to(map_)
        folium.Marker(coords2, popup=f"Destinatie: {location2.address}").add_to(map_)

        # Deseneaza rutele alternative
        for i, points in enumerate(routes_points):
            color = route_colors[i % len(route_colors)]
            folium.PolyLine(
                points,
                color=color,
                weight=4,
                opacity=0.85,
                tooltip=f"Traseu {i+1}"
            ).add_to(map_)

        label_result.config(
            text=f"Distanța (linie dreapta): {distance_km:.2f} km\n"
                 f"Start: {location1.address}\nDestinatie: {location2.address}\n"
                 f"Trasee gasite: {len(routes_points)}"
        )

        map_file = "trasee_detaliate.html"
        map_.save(map_file)
        webbrowser.open(os.path.abspath(map_file))

    except requests.RequestException as e:
        messagebox.showerror("Eroare", f"Eroare de retea: {e}")
    except Exception as e:
        messagebox.showerror("Eroare", f"A aparut o eroare: {e}")

# ================= GUI =================
root = tk.Tk()
root.title("Calculator de Trasee si Distante (OSM/OSRM)")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = int(screen_width * 0.8)
window_height = int(screen_height * 0.8)

position_x = (screen_width - window_width) // 2
position_y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

# Fundal imagine (daca exista)
bg_image = None
try:
    background_image = Image.open("harta_fundal.jpg")
    background_image = background_image.resize((window_width, window_height), Image.Resampling.LANCZOS)
    bg_image = ImageTk.PhotoImage(background_image)
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)
except Exception:
    root.configure(bg="white")

frame = tk.Frame(root, padx=20, pady=20, bg="white", bd=5)
frame.place(relx=0.5, rely=0.5, anchor="center")

label_location1 = tk.Label(frame, text="Locatia 1:", bg="white", font=("Helvetica", 14))
label_location1.grid(row=0, column=0, sticky="w", pady=5)
entry_location1 = tk.Entry(frame, width=40, font=("Helvetica", 12))
entry_location1.grid(row=0, column=1, pady=5)

label_location2 = tk.Label(frame, text="Locatia 2:", bg="white", font=("Helvetica", 14))
label_location2.grid(row=1, column=0, sticky="w", pady=5)
entry_location2 = tk.Entry(frame, width=40, font=("Helvetica", 12))
entry_location2.grid(row=1, column=1, pady=5)

button_calculate = tk.Button(
    frame,
    text="Calculeaza Traseul si Distanta",
    command=calculate_route,
    bg="#4CAF50",
    fg="white",
    font=("Helvetica", 14, "bold")
)
button_calculate.grid(row=2, columnspan=2, pady=10)

label_result = tk.Label(frame, text="Distanța va fi afisata aici.", bg="white", font=("Helvetica", 12), justify="left")
label_result.grid(row=3, columnspan=2, pady=5)

exit_button = tk.Button(frame, text="Inchide", command=root.quit, bg="red", fg="white", font=("Helvetica", 12, "bold"))
exit_button.grid(row=4, columnspan=2, pady=10)

root.mainloop()
