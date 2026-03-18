import sqlite3

# Verbindung zur Datenbank herstellen (Datei wird erstellt, falls sie nicht existiert)
conn = sqlite3.connect("bibliothek.db")
cursor = conn.cursor()

# Fremdschlüssel in SQLite aktivieren
cursor.execute("PRAGMA foreign_keys = ON;")

# -----------------------------
# Tabelle: Kunde
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS Kunde (
    Kundennummer INTEGER PRIMARY KEY,
    Email VARCHAR(100),
    Wohnadresse VARCHAR(100),
    Telefonnummer VARCHAR(30),
    Vorname VARCHAR(15),
    Nachname VARCHAR(15)
);
""")

# -----------------------------
# Tabelle: Verlag
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS Verlag (
    VerlagID INTEGER PRIMARY KEY,
    Name VARCHAR(50),
    Email VARCHAR(30),
    Stadt VARCHAR(100)
);
""")

# -----------------------------
# Tabelle: Buch
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS Buch (
    ISBN VARCHAR(20) PRIMARY KEY,
    Titel VARCHAR(80),
    Erscheinungsjahr INTEGER,
    FKVerlagID INTEGER,
    FOREIGN KEY (FKVerlagID) REFERENCES Verlag(VerlagID)
);
""")

# -----------------------------
# Tabelle: Autor
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS Autor (
    AutorID INTEGER PRIMARY KEY,
    Vorname VARCHAR(15),
    Nachname VARCHAR(15),
    Geburtsjahr INTEGER
);
""")

# -----------------------------
# Tabelle: geschrieben (m:n)
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS geschrieben (
    FKISBN VARCHAR(20),
    FKAutorID INTEGER,
    PRIMARY KEY (FKISBN, FKAutorID),
    FOREIGN KEY (FKISBN) REFERENCES Buch(ISBN),
    FOREIGN KEY (FKAutorID) REFERENCES Autor(AutorID)
);
""")

# -----------------------------
# Tabelle: Leihe
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS Leihe (
    AusleihID INTEGER PRIMARY KEY,
    Ausleihdatum DATE,
    geplantesRueckgabedatum DATE,
    tatsaechlichesRueckgabedatum DATE,
    FKISBN VARCHAR(20),
    FKKundennummer INTEGER,
    FOREIGN KEY (FKISBN) REFERENCES Buch(ISBN),
    FOREIGN KEY (FKKundennummer) REFERENCES Kunde(Kundennummer)
);
""")

# Änderungen speichern und Verbindung schließen
conn.commit()
conn.close()