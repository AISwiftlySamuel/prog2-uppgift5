# Importera tkinter, requests, sqlite3

# Skapa tabell
# Anslut till databasen
# Skapa tabell om den inte redan finns
# Definiera kolumner: id, titel, författare, år, status

# Hämta bok
# Läs boktitel från textfältet
# Gör anrop till API
# Om anropet lyckas (status 200):
    # Om det finns minst en träff:
        # Hämta ut författare och år från första träffen
        # Visa i etiketten
    # Annars (ingen träff):
        # Visa "Ingen bok hittades, prova en annan titel"
# Annars (anropet misslyckades):
    # Visa felmeddelande
