# Anteckningar till reflektion — Lärarbedömd uppgift 5

Löpande anteckningar under utvecklingen, för att göra README/reflektion snabbare att skriva på fredag.

## Kända begränsningar i programmet

- **Titelfält vs. hämtad data:** Om användaren ändrar texten i titelfältet *efter* att ha klickat "Hämta bok", men *innan* "Spara bok", sparas den nya titeln ihop med författare/år från den **förra** hämtningen (eftersom `senaste_bok` bara uppdateras vid lyckad hämtning, inte vid varje tecken som skrivs).
  - **Förbättringsförslag:** bara tillåta "Spara bok" direkt efter en lyckad hämtning, t.ex. genom att nollställa `senaste_bok` så fort titelfältet ändras.

## Koppling till tidigare feedback (Peter, uppgift 4)

Peters kommentar på uppgift 4: kontrollera att titel/författare inte lämnas tomma innan sparande.

I uppgift 5 är detta löst på två sätt, eftersom författare hämtas automatiskt istället för att skrivas in manuellt:
- **Titel:** explicit tomkontroll i `spara_bok()` — `if titel.strip() == "": ...`
- **Författare:** hämtas från Open Library API i `hamta_bok()`, med fallback-värde `"Okänd"` om fältet saknas i API-svaret (`forsta_traff.get("author_name", ["Okänd"])[0]`) — kan alltså aldrig bli en tom sträng i databasen.

Detta visar medveten vidareutveckling baserat på tidigare lärarfeedback.

## Idéer för vidareutveckling (efter kursen)

- **KB/Libris API** som alternativ eller komplement till Open Library — sök i ~600 svenska bibliotek. Bedömdes för komplext (JSON-LD/MARC-format) att hinna med under tidspress inför 21 aug-deadline, men intressant att utforska vidare, särskilt kopplat till AI Swiftly.
- Möjlig utökning: ISBN som fält för unik identifiering av böcker.
- Möjlig utökning: `Listbox`/`Treeview`-widget istället för etikett, för att visa flera sökträffar att välja mellan (istället för bara första träffen).

## Testresultat (löpande)

- ✅ Resizable GUI fungerar (grid + weight + resizable), minsize satt till att förhindra för litet fönster
- ✅ Tomt titelfält vid spara → korrekt felmeddelande, ingen krasch
- ✅ Ta bort bok via id → fungerar, listan uppdateras korrekt vid ny sökning
- ⚠️ Se känd begränsning ovan (titelfält vs. hämtad data)
