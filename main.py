import agent
import trainingAgents
import world

if __name__ == '__main__':
	world = world.World(home="http://cdn.mysitemyway.com/etc-mysitemyway/icons/legacy-previews/icons/blue-jelly-icons-symbols-shapes/017873-blue-jelly-icon-symbols-shapes-shapes-circle-frame.png")
	world.initialize()
	agent = trainingAgents.SimpleTrainingAgent(world)
	n = 10
	agent.observe(n)
	world.reset()
	agent.run(n)
