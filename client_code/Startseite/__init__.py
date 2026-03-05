from ._anvil_designer import StartseiteTemplate
from anvil import *

class Startseite(StartseiteTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @handle("button_kunden", "click")
  def button_kunden_click(self, **event_args):
    open_form('Startseite.GebaeudeSeite',self.item)

  @handle("button_buecher", "click")
  def button_buecher_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  @handle("button_leihe", "click")
  def button_leihe_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
