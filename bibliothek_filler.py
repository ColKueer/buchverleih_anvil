import sqlite3

conn = sqlite3.connect("bibliothek.db")
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")

# -------------------------------------------------
# Kunde
# -------------------------------------------------
kunden = [
    (1, "max.mustermann@mail.de", "Musterstraße 1", "0123456789", "Max", "Mustermann"),
    (2, "anna.schmidt@mail.de", "Hauptstraße 5", "0987654321", "Anna", "Schmidt"),
    (3, "lukas.meier@mail.de", "Bahnhofstraße 10", "01701234567", "Lukas", "Meier")
]

cursor.executemany("""
INSERT OR IGNORE INTO Kunde
VALUES (?, ?, ?, ?, ?, ?);
""", kunden)


# -------------------------------------------------
# Verlag
# -------------------------------------------------
verlage = [
    (1, "Springer Verlag", "kontakt@springer.de", "Berlin"),
    (2, "Penguin Random House", "info@penguin.de", "München"),
    (3, "O'Reilly Media", "support@oreilly.com", "Köln")
]

cursor.executemany("""
INSERT OR IGNORE INTO Verlag
VALUES (?, ?, ?, ?);
""", verlage)


# -------------------------------------------------
# Buch
# -------------------------------------------------
buecher = [
    ("9781234567890", "Datenbanken Grundlagen", 2020, 1),
    ("9781234567891", "Python Programmierung", 2021, 3),
    ("9781234567892", "Software Engineering", 2019, 2)
]

cursor.executemany("""
INSERT OR IGNORE INTO Buch
VALUES (?, ?, ?, ?);
""", buecher)


# -------------------------------------------------
# Autor
# -------------------------------------------------
autoren = [
    (1, "Thomas", "Müller", 1975),
    (2, "Sabine", "Keller", 1980),
    (3, "Michael", "Braun", 1968)
]

cursor.executemany("""
INSERT OR IGNORE INTO Autor
VALUES (?, ?, ?, ?);
""", autoren)


# -------------------------------------------------
# geschrieben (m:n Beziehung)
# -------------------------------------------------
geschrieben = [
    ("9781234567890", 1),
    ("9781234567891", 2),
    ("9781234567892", 3),
    ("9781234567892", 1)  # Buch mit zwei Autoren
]

cursor.executemany("""
INSERT OR IGNORE INTO geschrieben
VALUES (?, ?);
""", geschrieben)


# -------------------------------------------------
# Leihe
# -------------------------------------------------
leihen = [
    (1, "2026-01-10", "2026-01-24", "2026-01-22", "9781234567890", 1),
    (2, "2026-02-01", "2026-02-15", None, "9781234567891", 2),
    (3, "2026-02-20", "2026-03-06", None, "9781234567892", 3)
]

cursor.executemany("""
INSERT OR IGNORE INTO Leihe
VALUES (?, ?, ?, ?, ?, ?);
""", leihen)


conn.commit()
conn.close()