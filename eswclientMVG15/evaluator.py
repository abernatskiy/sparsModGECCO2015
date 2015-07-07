from parseStr import *
from booleanNetwork import *

import numpy as np
from copy import copy

def hammingDistance(pat0, pat1):
	return (pat0 != pat1).sum()

class Evaluator(object):
	def __init__(self, patterns):
		self.setPatterns(patterns)
		self.patternMutProb = 0.15
		self.patternEvals = len(patterns[0])
		self.fitnessPower = 5

	def setPatterns(self, patterns):
		self.patterns = map(np.array, patterns)

	def evaluateNetwork(self, genotype):
		networkConnections = parse2d(genotype)
		size = len(networkConnections)
		self.network = BooleanNetwork(networkConnections, np.zeros(size))
		netScore = 0.0
		for pat in self.patterns:
			netScore += self.evaluateNetworkWithPattern(pat)
		netScore /= len(self.patterns)
		return netScore

	def evaluateNetworkWithPattern(self, pattern):
		score = 0.0
		for i in xrange(self.patternEvals):
			testPat = self.perturbedPattern(pattern, i)
			self.network.setState(testPat)
#			print('Evaluated network ' + str(self.network.con) + ' with pattern ' + str(testPat))
			if self.network.findAttractor(attractorMaxTrials=20):
				score += np.power(1.0 - float(hammingDistance(pattern, self.network.attractor))/float(len(pattern)), self.fitnessPower)
#				print('Attractor found (' + str(self.network.attractor)+ '), Hamming distance to ' + str(pattern) + ' is ' + str(hammingDistance(pattern, self.network.attractor)))
		score /= self.patternEvals
#		print('Evaluated network ' + str(self.network.con) + ' with pattern ' + str(pattern) + ' (' + str(self.patternEvals) + ' evaluations made, score ' + str(-1.0*np.expm1(-3.0*score)) + ')')
		return -1.0*np.expm1(-3.0*score)

	def mutatedPattern(self, pattern):
		mutPattern = copy(pattern)
		size = len(pattern)
		for i in xrange(size):
			if np.random.rand() < self.patternMutProb:
				mutPattern[i] = 1 if mutPattern[i] == -1 else -1
		return mutPattern

	def perturbedPattern(self, pattern, position):
		perPattern = copy(pattern)
		perPattern[position] = 1 if perPattern[position] == -1 else -1
		return perPattern
		
