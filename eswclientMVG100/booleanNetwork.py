import numpy as np

class BooleanNetwork(object):
	def __init__(self, connections, state):
		self.con = connections
		self.setState(state)
		self.span = 0

	def setState(self, state):
		self.sta = state

	def forward(self):
		newSta = np.dot(self.con, self.sta)
		sigma = np.vectorize(lambda x: 1 if x>0 else -1)
		newSta = sigma(newSta)
		if (newSta == self.sta).all():
			self.span += 1
		else:
			self.span = 0
		self.sta = newSta

	def findAttractor(self, attractorMaxTrials=100):
#		attractorMaxTrials = np.power(2, len(self.con)) + 1 # safe bet - number of possible states of the network plus one: no transient can last this long
		for i in xrange(attractorMaxTrials):
			self.forward()
			if self.span > 0:
				self.attractor = self.sta
				return True
		return False
