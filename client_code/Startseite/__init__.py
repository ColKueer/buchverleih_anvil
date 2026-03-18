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
    self.add_event_handler('show', self.form_show)

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
    
  @handle("button_verlag", "click")
  def button_verlag_click(self, **event_args):
    open_form('Startseite.Verlage')

  def form_show(self, **event_args):
    verliehen, nicht_verliehen = anvil.server.call('get_daten')
    fig = go.Figure(data=[go.Pie(
      labels=['Verliehen', 'Nicht verliehen'],
      values=[verliehen, nicht_verliehen],
      hole=0.3
    )])
    self.lade_verspaetungs_diagramm()
    fig.update_layout(title="Bücherstatus")
    self.plot_kreisdiagramm.figure = fig
    
  def lade_verspaetungs_diagramm(self, **event_args):
    verspaetet, nicht_verspaetet = anvil.server.call('get_verspaetung_daten')
    fig = go.Figure(data=[
      go.Bar(
        x=['Verspätet', 'Nicht verspätet'],
        y=[verspaetet, nicht_verspaetet],
        marker_color=['red', 'green']
      )
    ])
    fig.update_layout(
      title="Verspätete Rückgaben",
      xaxis_title="Status",
      yaxis_title="Anzahl"
    )
    self.plot_balkendiagramm.figure = fig


