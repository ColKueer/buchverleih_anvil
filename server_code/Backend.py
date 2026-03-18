import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import sqlite3

@anvil.server.callable
def query_database(query:str):
  with sqlite3.connect(data_files["bibliothek.db"]) as conn:
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return result


@anvil.server.callable
def query_database_dict(query:str):
  with sqlite3.connect(data_files["bibliothek.db"]) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return [dict(row) for row in result]

def get_daten():
  with sqlite3.connect(data_files["bibliothek.db"]) as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Buch")
    gesamt = cursor.fetchone()[0]
    cursor.execute("""
          SELECT COUNT(DISTINCT FKISBN)
          FROM Leihe
          WHERE tatsaechlichesRueckgabedatum IS NULL
      """)
    verliehen = cursor.fetchone()[0]
    conn.close()
    nicht_verliehen = gesamt - verliehen
  return verliehen, nicht_verliehen