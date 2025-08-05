from ._anvil_designer import codeinjectionTemplate
from anvil import *
import anvil.server


class codeinjection(codeinjectionTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
