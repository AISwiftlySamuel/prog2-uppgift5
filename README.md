# Mitt Bibliotek

Ett Python-program med grafiskt gränssnitt för att söka efter böcker via Open Library API, spara bokinformation lokalt i en SQLite-databas samt visa, filtrera och ta bort sparade poster.

Projektet utvecklades inom **Programmering nivå 2** och kombinerar grafiskt gränssnitt, API-kommunikation och databaslagring i en sammanhängande applikation.

## Funktioner

- Söker efter en boktitel via Open Library API.
- Hämtar titel, författare och utgivningsår.
- Låter användaren välja lässtatus, exempelvis *Vill läsa*.
- Sparar bokinformationen i en lokal SQLite-databas.
- Visar alla sparade böcker eller filtrerar resultat efter sökord.
- Tar bort en bok med hjälp av postens id.
- Hanterar saknade API-fält och vanliga fel med tydliga reservvärden och undantagshantering.

## Teknik

- **Python**
- **tkinter** för grafiskt användargränssnitt
- **requests** för API-anrop
- **SQLite / sqlite3** för lokal datalagring
- **Open Library API** för bokdata
- **Visual Studio Code** som utvecklingsmiljö
- **GitHub** för versionshantering och publicering

## Projektstruktur

Programmet är uppdelat i fyra huvudsakliga funktioner:

- `hamta_bok()` hämtar bokinformation från API:t.
- `spara_bok()` sparar senast hämtade bok i databasen.
- `visa_bocker()` visar eller filtrerar sparade böcker.
- `ta_bort_bok()` tar bort en bok utifrån dess id.

Funktionerna har docstrings. API-anrop och databasoperationer omges av `try`/`except` för att hantera nätverksfel, databasfel och ofullständiga API-svar.

## Så körs programmet

### 1. Klona repot

```bash
git clone https://github.com/AISwiftlySamuel/prog2-uppgift5.git
cd prog2-uppgift5
```

### 2. Skapa och aktivera en virtuell miljö

```bash
python -m venv .venv
```

På macOS eller Linux:

```bash
source .venv/bin/activate
```

På Windows:

```powershell
.venv\Scripts\activate
```

### 3. Installera beroendet

```bash
pip install requests
```

### 4. Starta programmet

```bash
python lararbedomd-uppgift-5.py
```

Databasfilen `bibliotek.db` skapas automatiskt första gången programmet körs.

## Användning

1. Skriv en boktitel i sökfältet.
2. Välj **Hämta bok**.
3. Kontrollera titel, författare och utgivningsår.
4. Välj lässtatus.
5. Välj **Spara bok**.
6. Använd **Visa böcker** för att se hela registret eller filtrera med ett sökord.
7. Ange ett bok-id och välj **Ta bort bok** för att radera posten.

## Kvalitet och felhantering

Projektet innehåller flera kontroller för att förbättra stabilitet och datakvalitet:

- `.get()` används för att hantera fält som kan saknas i API-svaret.
- Författare får reservvärdet `Okänd` om uppgiften saknas.
- Titel, författare och år sparas från samma API-hämtning för att undvika felaktiga kombinationer.
- Fönstret har en minsta storlek så att gränssnittet förblir användbart.
- Programmet testades löpande under utvecklingen och fel rättades före färdigställandet.

## Viktiga lärdomar

Projektet gav praktisk erfarenhet av att:

- analysera och bryta ned ett programmeringsproblem,
- arbeta pseudokod-first innan implementering,
- strukturera ett program i tydliga funktioner,
- tolka nästlad JSON från ett externt API,
- koppla ett grafiskt gränssnitt till programlogik,
- lagra och hantera data i SQLite,
- felsöka samband mellan användarinmatning, API-data och databaslagring,
- skriva mer läsbar, testbar och dokumenterad kod.

## Skärmbild

Lägg gärna en skärmbild av applikationen i `docs/images/` och använd följande Markdown:

```markdown
![Mitt Bibliotek, grafiskt gränssnitt för boksökning och lokal lagring](docs/images/mitt-bibliotek.png)
```

## Dataskydd

Applikationen använder offentlig bokinformation från Open Library API. Sparade bokposter lagras lokalt i `bibliotek.db`. Repot ska inte innehålla lösenord, API-nycklar, privata personuppgifter eller andra hemligheter.

## Fortsatt utveckling

Möjliga nästa steg:

- stöd för flera träffar från samma sökning,
- redigering av sparade poster,
- export och import av boklistor,
- förbättrad validering och automatiserade tester,
- jämförelse med Kungliga bibliotekets öppna Libris API,
- paketering av applikationen för enklare installation.

## Bakgrund

Projektet utvecklades som avslutande arbete inom **Programmering nivå 2, 100 poäng**, med Python som programspråk. Fokus låg på objektorienterat och strukturerat utvecklingsarbete, fil- och databashantering, API-kommunikation, grafiskt gränssnitt, testning, felsökning och dokumentation.
