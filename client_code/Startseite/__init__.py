from ._anvil_designer import StartseiteTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Startseite(StartseiteTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @handle("button_kunde", "click")
  def button_kunden_click(self, **event_args):
    open_form('Startseite.Kunden')

  @handle("button_buecher", "click")
  def button_buecher_click(self, **event_args):
    open_form('Startseite.Buecher')

  @handle("button_leihe", "click")
  def button_leihe_click(self, **event_args):
    open_form('Startseite.leihen')
