import anvil.email
import anvil.server
import random
from random import shuffle

global ansselected
ansselected = False

@anvil.server.callable

def click_event():
  global ansselected
  ansselected = True

@anvil.server.callable

def returnansselected():
  global ansselected
  return ansselected