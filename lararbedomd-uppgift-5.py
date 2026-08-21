"""
lararbedomd-uppgift-5.py

Mitt Bibliotek - ett program för att söka bokinformation via Open Library API,
spara valda böcker lokalt i en SQLite-databas, och visa/söka/ta bort sparade
böcker via ett grafiskt gränssnitt (tkinter).

Lärarbedömd uppgift 5, Programmering nivå 2, Python
Samuel Augsburger, augusti 2026
"""

import tkinter as tk
from tkinter import ttk # Combobox = rullgardinsmeny-widget
import requests
import sqlite3

# Anslut till databasen (skapar filen om den inte redan finns)
conn = sqlite3.connect("bibliotek.db")
cursor = conn.cursor()

# Skapa SQL-tabellen om den inte redan finns, med kolumner: id, titel, författare, år, status
cursor.execute("""
CREATE TABLE IF NOT EXISTS bocker (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titel TEXT,
    forfattare TEXT,
    ar INTEGER,
    status TEXT
)
""")
conn.commit()

# Global variabel som håller senaste hämtade bok (författare, år)
senaste_bok = None

def hamta_bok():
    """Hämtar bokinformation (titel, författare, år) från Open Library API
    baserat på titeln i textfältet, och visar resultatet i etiketten."""

    global senaste_bok
    titel = titel_faltet.get()

    try:
        svar = requests.get(f"https://openlibrary.org/search.json?q={titel}")
        if svar.status_code == 200:
            data = svar.json()
            if data["numFound"] > 0:
                forsta_traff = data["docs"][0]
                riktig_titel = forsta_traff.get("title", titel)
                forfattare = forsta_traff.get("author_name", ["Okänd"])[0]
                ar = forsta_traff.get("first_publish_year", "Okänt")
                senaste_bok = (riktig_titel, forfattare, ar)
                resultat_etikett.config(text=f"{riktig_titel} av {forfattare} ({ar})")
            else:
                resultat_etikett.config(text="Ingen bok hittades, prova en annan titel")
        else:
            resultat_etikett.config(text="Kunde inte kontakta API:et")
    except requests.exceptions.RequestException:
        resultat_etikett.config(text="Nätverksfel — kontrollera din uppkoppling")

def spara_bok():
    """Sparar senast hämtade bok (titel, författare, år, status) i databasen,
    efter kontroll att en bok hämtats."""

    global senaste_bok
    status = status_combobox.get()

    if senaste_bok is None:
        resultat_etikett.config(text="Hämta en bok innan du sparar")
    else:
        try:
            riktig_titel, forfattare, ar = senaste_bok
            cursor.execute(
                "INSERT INTO bocker (titel, forfattare, ar, status) VALUES (?, ?, ?, ?)",
                (riktig_titel, forfattare, ar, status)
            )
            conn.commit()
            resultat_etikett.config(text="Boken sparad!")
        except sqlite3.Error as e:
            resultat_etikett.config(text=f"Databasfel: {e}")

def visa_bocker(sokord=""):
    """Visar sparade böcker från databasen. Om sokord anges filtreras
    träffar på titel, annars visas alla sparade böcker."""

    if sokord == "":
        cursor.execute("SELECT * FROM bocker")
    else:
        cursor.execute("SELECT * FROM bocker WHERE titel LIKE ?", (f"%{sokord}%",))

    rader = cursor.fetchall()

    if rader:
        text = ""
        for rad in rader:
            text += f"ID {rad[0]}: {rad[1]} av {rad[2]} ({rad[3]}) - {rad[4]}\n"
        resultat_lista.config(text=text)
    else:
        resultat_lista.config(text="Inga böcker hittades")

def ta_bort_bok():
    """Tar bort en bok från databasen, baserat på id angivet i textfältet."""

    id_falt_text = id_faltet.get()

    if id_falt_text.strip() == "":
        resultat_lista.config(text="Skriv in id för boken du vill ta bort")
    elif not id_falt_text.isdigit():
        resultat_lista.config(text="Id måste vara ett nummer")
    else:
        try:
            cursor.execute("DELETE FROM bocker WHERE id = ?", (id_falt_text,))
            conn.commit()
            resultat_lista.config(text="Boken borttagen!")
        except sqlite3.Error as e:
            resultat_lista.config(text=f"Databasfel: {e}")

# --- Huvudprogram: bygger GUI:t och kopplar widgets till funktionerna ovan ---
root = tk.Tk()
root.title("Mitt Bibliotek")
root.resizable(True, True)
root.minsize(350, 400)
root.columnconfigure(0, weight=1)

# Sökning/hämtning från API
titel_faltet = tk.Entry(root)
titel_faltet.grid(row=0, column=0, sticky="ew", padx=10, pady=5)

hamta_knapp = tk.Button(root, text="Hämta bok", command=hamta_bok)
hamta_knapp.grid(row=1, column=0, sticky="ew", padx=10, pady=5)

resultat_etikett = tk.Label(root, text="")
resultat_etikett.grid(row=2, column=0, sticky="ew", padx=10, pady=5)

# Status och spara
status_combobox = ttk.Combobox(root, values=["Vill läsa", "Läser", "Läst", "Äger", "Vill köpa"], state="readonly")
status_combobox.grid(row=3, column=0, sticky="ew", padx=10, pady=5)

spara_knapp = tk.Button(root, text="Spara bok", command=spara_bok)
spara_knapp.grid(row=4, column=0, sticky="ew", padx=10, pady=5)

# Visa/sök bland sparade böcker
sok_faltet = tk.Entry(root)
sok_faltet.grid(row=5, column=0, sticky="ew", padx=10, pady=5)

visa_knapp = tk.Button(root, text="Visa böcker", command=lambda: visa_bocker(sok_faltet.get()))
visa_knapp.grid(row=6, column=0, sticky="ew", padx=10, pady=5)

resultat_lista = tk.Label(root, text="", justify="left")
resultat_lista.grid(row=7, column=0, sticky="ew", padx=10, pady=5)

# Ta bort bok
id_faltet = tk.Entry(root)
id_faltet.grid(row=8, column=0, sticky="ew", padx=10, pady=5)

ta_bort_knapp = tk.Button(root, text="Ta bort bok", command=ta_bort_bok)
ta_bort_knapp.grid(row=9, column=0, sticky="ew", padx=10, pady=5)

# Starta programmet
root.mainloop()