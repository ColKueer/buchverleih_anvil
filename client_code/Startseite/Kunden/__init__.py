from ._anvil_designer import KundenTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Kunden(KundenTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    sql = """SELECT 
    Kundennummer as kundennummer,
    Email as email,
    Wohnadresse as wohnadresse,
    Telefonnummer as telefonnummer,
    Vorname as vorname,
    Nachname as nachname
    FROM  Kunde
    """

    data = anvil.server.call('query_database_dict', f'{sql}')

    self.repeating_panel_1.items = data

  @handle("button_menue", "click")
  def button_menue_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Startseite')

  @handle("button_buecher", "click")
  def button_buecher_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Startseite.Buecher')

  @handle("button_leihe", "click")
  def button_leihe_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Startseite.leihen')

  @handle("button_verlag", "click")
  def button_verlag_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Startseite.Verlage')
