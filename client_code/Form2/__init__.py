from ._anvil_designer import Form2Template
from anvil import *
import anvil.server
import anvil.js
import webbrowser

class Form2(Form2Template):
  def __init__(self, **properties):
    self.init_components(**properties)

  def gradientexp_click(self, **event_args):
    from .gradientattack import gradientattack
    gabox = alert(
      title = 'Gradient Attacks',
      content = gradientattack(),
      large = True,
      buttons = [
        ("Try it Yourself", "YES"),
        ("Exit", "NO")
      ]
    )
    if gabox == "YES":
      url = 'https://huggingface.co/spaces/exbert-project/exbert'
      webbrowser.open_new_tab(url)

  def finetuningexp_click(self, **event_args):
    from .finetuningattack import finetuningattack
    ftbox = alert(
      title = 'Fine Tuning Based Attacks',
      content = finetuningattack(),
      large = True,
      buttons = [
        ("Exit", "NO")
      ]
    )

  def logitexp_click(self, **event_args):
    from .logitattack import logitattack
    lebox = alert(
      title = 'Logit Based Attacks',
      content = logitattack(),
      large = True,
      buttons = [
        ("Try it Yourself", "YES"),
        ("Exit", "NO")
      ]
    )
    if lebox == "YES":
      url = 'https://poloclub.github.io/transformer-explainer/'
      webbrowser.open_new_tab(url)

  def contextexp_click(self, **event_args):
    from .scenarioattack import scenarioattack
    cobox = alert(
      title = 'Scenario Nesting',
      content = scenarioattack(),
      large = True,
      buttons = [
        ("Try it Yourself", "YES"),
        ("Exit", "NO")
      ]
    )
    if cobox == "YES":
      url = 'https://huggingface.co/spaces/exbert-project/exbert'
      webbrowser.open_new_tab(url)

  def injectionexp_click(self, **event_args):
    from .codeinjection import codeinjection
    ijbox = alert(
      title = 'Code Injection',
      content = codeinjection(),
      large = True,
      buttons = [
        ("Exit", "NO")
      ]
    )

  def languageexp_click(self, **event_args):
    from .lowreslangattack import lowreslangattack
    ijbox = alert(
      title = 'Low Resource Languages',
      content = lowreslangattack(),
      large = True,
      buttons = [
        ("Exit", "NO")
      ]
    )

  def geneticexp_click(self, **event_args):
    from .geneticattack import geneticattack
    gebox = alert(
      title = 'Genetic Algorithm Attacks',
      content = geneticattack(),
      large = True,
      buttons = [
        ("Exit", "NO")
      ]
    )

  def generationexp_click(self, **event_args):
    from .generationattack import generationattack
    genbox = alert(
      title = 'LLM Based Generation Attacks',
      content = generationattack(),
      large = True,
      buttons = [
        ("Exit", "NO")
      ]
    )

  def detectionexp_click(self, **event_args):
    from .promptdetection import promptdetection
    detbox = alert(
      title = 'Prompt Detection',
      content = promptdetection(),
      large = True,
      buttons = [
        ("Exit", "NO")
      ]
    )

  def perturbationexp_click(self, **event_args):
    from .promptperturbation import promptperturbation
    perbox = alert(
      title = 'Prompt Perturbation',
      content = promptperturbation(),
      large = True,
      buttons = [
        ("Exit", "NO")
      ]
    )

  def safeguardexp_click(self, **event_args):
    from .promptsafeguard import promptsafeguard
    safbox = alert(
      title = 'System Prompt Safeguards',
      content = promptsafeguard(),
      large = True,
      buttons = [
        ("Exit", "NO")
      ]
    )

  def sftexp_click(self, **event_args):
    from .sftmethods import sftmethods
    sftbox = alert(
      title = 'SFT Based Methods',
      content = sftmethods(),
      large = True,
      buttons = [
        ("Exit", "NO")
      ]
    )

  def rlhfexp_click(self, **event_args):
    from .rlhfmethods import rlhfmethods
    rlhfbox = alert(
      title = 'RLHF Based Methods',
      content = rlhfmethods(),
      large = True,
      buttons = [
        ("Exit", "NO")
      ]
    )

  def gradientaexp_click(self, **event_args):
    from .gradientanalysis import gradientanalysis
    glabox = alert(
      title = 'Logit Analysis',
      content = gradientanalysis(),
      large = True,
      buttons = [
        ("Exit", "NO")
      ]
    )
    if glabox == "YES":
      url = 'https://docs.python.org/'
      webbrowser.open_new_tab(url)

  def refinementexp_click(self, **event_args):
    from .refinement import refinement
    refbox = alert(
      title = 'Refinement',
      content = refinement(),
      large = True,
      buttons = [
        ("Exit", "NO")
      ]
    )

  def proxyexp_click(self, **event_args):
    from .proxydefence import proxydefence
    pdbox = alert(
      title = 'Proxy Defence',
      content = proxydefence(),
      large = True,
      buttons = [
        ("Exit", "NO")
      ]
    )

  def cipherexp_click(self, **event_args):
    from .cipherattack import cipherattack
    cibox = alert(
      title = 'Ciphers',
      content = cipherattack(),
      large = True,
      buttons = [
        ("Exit", "NO")
      ]
    )

  def gradientaexp_copy_click(self, **event_args):
    from .gradientanalysisreal import gradientanalysisreal
    garbox = alert(
      title = 'Gradient Analysis',
      content = gradientanalysisreal(),
      large = True,
      buttons = [
        ("Exit", "NO")
      ]
    )

  def geneticexp_copy_click(self, **event_args):
    from .contextattack import contextattack
    cabox = alert(
      title = 'Context Based Attack',
      content = contextattack(),
      large = True,
      buttons = [
        ("Exit", "NO")
      ]
    )

  def link_1_click(self, **event_args):
    url = 'https://platform.openai.com/tokenizer'
    webbrowser.open_new_tab(url)

  def link_1_copy_click(self, **event_args):
    url = 'https://poloclub.github.io/transformer-explainer/'
    webbrowser.open_new_tab(url)
