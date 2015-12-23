import pyautogui
import time
import webbrowser



class World(object):
	"""Interfaces with pyautogui."""
	def __init__(self, home="http://google.com"):
		self.home = home

	def initialize(self):
		"""Open the browser and go to home."""
		webbrowser.open_new(self.home)
		# this should be fixed
		time.sleep(2)


	def getState(self):
		"""Returns a screenshot (PIL image)"""
		return pyautogui.screenshot()

	def takeAction(self, action, agent):
		"""action is of class Action"""
		action.execute()

	def reset(self):
		self.initialize()



# ACTIONS

class Action(object):
	def execute(self):
		pass



class Backspaces(Action):
	def __init__(self, n):
		self.n = n

	def execute(self):
		pyautogui.typewrite(['backspace' for _ in range(self.n)])



class Click(Action):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def execute(self):
		pyautogui.click(x=self.x, y=self.y)



class MoveMouse(Action):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def execute(self):
		pyautogui.moveTo(x=self.x, y=self.y)



class MultiAction(Action):
	def __init__(self, actionList):
		self.actionList = actionList

	def execute(self):
		for action in actionList:
			action.execute()



class TypeWrite(Action):
	def __init__(self, keys):
		self.keys = keys

	def execute(self):
		pyautogui.typewrite(self.keys)
