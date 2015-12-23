import agent
import pyautogui
import time
import world



class SimpleTrainingAgent(agent.Agent):
	def __init__(self, world, delay=0.25):
		super(SimpleTrainingAgent, self).__init__(world, delay)
		self.actions = {} # time ints to action

	def _observationStep(self):
		x, y = pyautogui.position()
		self.actions[self.time] = world.MoveMouse(x, y)
		self.time += 1

	def observe(self, n=1):
		for _ in range(n):
			self._observationStep()
			time.sleep(self.delay)

		self.time = 0


	def _getNextAction(self, stateFeatures):
		if self.time in self.actions:
			return self.actions[self.time]

		return None