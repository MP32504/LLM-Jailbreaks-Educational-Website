from ._anvil_designer import HomePageTemplate
from anvil import *
import anvil.server


class HomePage(HomePageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    open_form('Form1')

  def button_2_click(self, **event_args):
    open_form('Form2')
