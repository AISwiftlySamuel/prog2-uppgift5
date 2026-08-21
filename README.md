Mitt Bibliotek
==============

Python-program med grafiskt gränssnitt (tkinter) för att söka bokinfo via Open
Library API, spara böcker i en lokal SQLite-databas, och visa/söka/ta bort dem.

Lärarbedömd uppgift 5, Programmering nivå 2.
Samuel Augsburger, augusti 2026.

Kod publicerad på GitHub: https://github.com/AISwiftlySamuel/prog2-uppgift5


Syfte
-----

Ett personligt bokregister. Man söker på en titel, programmet hämtar riktig
titel, författare och utgivningsår från Open Library, man väljer en status
(t.ex. "Vill läsa") och sparar boken lokalt.


Funktioner
----------

Hämta bok - söker en boktitel via API, visar titel, författare och år.
Spara bok - sparar senast hämtade bok (titel, författare, år, status) i databasen.
Visa böcker - visar alla sparade böcker, eller filtrerar om man skriver ett sökord.
Ta bort bok - tar bort en sparad bok via dess id.


Hur man kör programmet
-----------------------

1. Aktivera venv, se till att requests är installerat (pip install requests).
2. Kör lararbedomd-uppgift-5.py, t.ex. via VS Codes "Run Python File".
3. Skriv en boktitel, klicka Hämta bok.
4. Välj status i rullgardinen, klicka Spara bok.
5. Klicka Visa böcker för att se sparade böcker (tomt sökfält visar alla).
6. Skriv ett bok-id, klicka Ta bort bok för att ta bort den.

Databasfilen bibliotek.db skapas automatiskt första gången programmet körs.


Teknisk struktur
-----------------

tkinter för gränssnittet, requests för API-anropet, sqlite3 för lagring.

Koden är uppdelad i fyra funktioner (hamta_bok, spara_bok, visa_bocker,
ta_bort_bok), var och en med en docstring. Try/except runt både API-anrop och
databasoperationer.

Open Library svarar med nästlad JSON (en lista av träffar, där varje träff
innehåller listor, t.ex. för författarnamn). I hamta_bok plockas rätt fält ut
med .get(), som skyddar mot att API-svaret saknar ett fält.


Reflektion
----------

Det här var den mest omfattande uppgiften hittills i kursen - första gången
jag kombinerat GUI, API och databas i samma program. Jag körde miniuppgift 5.6
(ett skämtregister) som uppvärmning innan jag satte igång, vilket gjorde att
jag redan kände igen mönstren - global variabel för att skicka data mellan
funktioner, try/except runt API- och databasanrop, koppling mellan knapp och
funktion.

Jag valde att bygga vidare på bibliotekstemat från tidigare uppgifter, men
kopplade det mot Open Library API för riktig bokdata. Jag jobbade med
pseudokod innan Python-kod, en funktion i taget, samma metod som fungerat
genom hela kursen.

Jag testade programmet löpande, inte bara i slutet, och hittade två buggar på
vägen som jag rättade till innan inlämning:

Den första: fönstret gick att krympa till nästan ingenting. Löste det med
root.minsize(350, 400), så det fortfarande är resizable men inte oanvändbart.

Den andra, mer intressant: jag upptäckte att programmet sparade mitt sökord
som titel istället för bokens riktiga titel (t.ex. sökte jag "Linux" sparades
"Linux" i databasen, inte "Linux For Dummies"). Det berodde på att titeln
lästes direkt från textfältet i spara-funktionen, istället för från API-
svaret. Jag åtgärdade det genom att hämta ut det riktiga title-fältet från
API:t och spara det tillsammans med författare och år i samma variabel. Det
löste också ett andra problem jag inte tänkt på från början: om man ändrade
textfältet efter en hämtning men innan man sparade kunde fel författare/år
hamna ihop med fel titel. Efter fixen kommer titel, författare och år alltid
från samma hämtning, så det problemet kan inte längre uppstå.

Kopplat till Peters kommentar på uppgift 4 (kontrollera att titel/författare
inte lämnas tomma): i den här uppgiften hämtas författare automatiskt från
API:t med ett fallback-värde ("Okänd") om det saknas, så det fältet kan
aldrig bli tomt. Titel kommer numera alltid från API-svaret, av samma skäl.

Det jag är mest nöjd med är att jag testade tillräckligt noga för att hitta
titel-buggen själv, istället för att bara lämna in och hoppas att allt
fungerade. Det känns som rätt vana att ta med sig vidare.

Efter kursen är jag nyfiken på att titta på Kungliga bibliotekets (Libris)
öppna API - mer komplext än Open Library (JSON-LD-format), men intressant att
koppla till verkliga användningsfall i mitt företag, AI Swiftly.
