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

# Spara bok
# Läs boktitel från textfältet
# Läs status från comboboxen

# Om ingen bok hämtats än (senaste_bok saknas):
    # Visa "Hämta en bok innan du sparar"
# Annars, om titeln är tom:
    # Visa "Fyll i en titel innan du sparar"
# Annars:
    # Försök:
        # INSERT INTO databasen med titel, författare, år, status
        # (författare och år kommer från senaste_bok, resten från textfält/combobox)
        # Bekräfta ändringen i databasen (commit)
        # Visa "Boken sparad!" i etiketten
    # Om databasfel uppstår:
        # Visa felmeddelande i etiketten