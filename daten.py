from pathlib import Path

DATENDATEI = Path(__file__).with_name("bibliotheksdaten.txt")


def laden():
  
    daten = {
        "medien": {},
        "ausleihen": [],
    }

    if not DATENDATEI.exists():
        return daten

    with open(DATENDATEI, "r", encoding="utf-8") as datei:
        for zeile in datei:
            teile = zeile.rstrip("\n").split("|")
            art = teile[0]

            if art == "MEDIUM":
                # Format: MEDIUM|ISBN|Titel|Autor|Kategorie
                medien_id = teile[1]
                daten["medien"][medien_id] = {
                    "titel": teile[2],
                    "autor": teile[3],
                    "kategorie": teile[4],
                }
            elif art == "AUSLEIHE":
                # Format: AUSLEIHE|ISBN|Ausleiher|Ausleihdatum|Rueckgabedatum
                daten["ausleihen"].append({
                    "medien_id": teile[1],
                    "ausleiher": teile[2],
                    "ausleihdatum": teile[3],
                    "rueckgabedatum": teile[4],
                })

    return daten


def speichern(daten):
    """Speichert den aktuellen Stand der Medien und Ausleihen in die Textdatei."""
    with open(DATENDATEI, "w", encoding="utf-8") as datei:
        # Medien speichern
        for medien_id, m in daten["medien"].items():
            datei.write(f"MEDIUM|{medien_id}|{m['titel']}|{m['autor']}|{m['kategorie']}\n")

        # Ausleihen speichern
        for a in daten["ausleihen"]:
            datei.write(f"AUSLEIHE|{a['medien_id']}|{a['ausleiher']}|{a['ausleihdatum']}|{a['rueckgabedatum']}\n")
