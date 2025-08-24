from ._anvil_designer import scenarioattackTemplate
from anvil import *
import anvil.server


class scenarioattack(scenarioattackTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
