from ._anvil_designer import BuecherTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Buecher(BuecherTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    sql = """SELECT 
    Buch.titel AS titel,
    Buch.isbn AS isbn,
    Verlag.name AS verlag,
    Buch.erscheinungsjahr AS erscheinungsjahr 
    FROM Buch 
    JOIN Verlag 
    ON Buch.fkverlagid = Verlag.VerlagID"""

    data = anvil.server.call('query_database_dict', f'{sql}')

    print(data)
    self.repeating_panel_1.items = data