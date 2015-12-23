import time
import world



class Agent(object):

	def __init__(self, world, delay=1):
		self.delay = delay
		self.world = world
		self.time = 0

	def _reward(self, state):
		pass

	def _getStateFeatures(self, state):
		return state

	def _getNextAction(self, stateFeatures):
		pass

	def _step(self):
		currentState = self.world.getState()
		self._reward(currentState)

		currentStateFeats = self._getStateFeatures(currentState)
		nextAction = self._getNextAction(currentStateFeats)
		self.world.takeAction(nextAction, self)
		self.time += 1

	def run(self, numSteps=1):
		for _ in range(numSteps):
			self._step()
			time.sleep(self.delay)



class HelloWorldAgent(Agent):
	def _getNextAction(self, stateFeatures):
		return world.TypeWrite("Hello, world!")



class ClickFirstLinkAgent(Agent):
	def _getNextAction(self, stateFeatures):
		msg = "Hello, World!"

		if self.time == 0:
			action = world.TypeWrite(msg)

		elif self.time == 1:
			action = world.TypeWrite(['enter'])

		else:
			action = world.Click(163, 296)

		return action



