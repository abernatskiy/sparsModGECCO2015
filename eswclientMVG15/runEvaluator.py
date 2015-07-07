#!/usr/bin/python2

import sys

from evaluator import Evaluator

if len(sys.argv) != 3:
	raise ValueError('Usage: runEvaluator.py infile outfile\n')
fninput = sys.argv[1]
fnoutput = sys.argv[2]

def evaluateBatch():
	global fninput
	global fnoutput
	global evaluator
	genotypes = []
	finput = open(fninput, 'r')
	for line in finput:
		genotypes.append(line)
	finput.close()

	evaluations = []
	for gen in genotypes:
		pureGen = ' '.join(gen.split(' ')[1:])
		id = gen.split(' ')[0]
		score = evaluator.evaluateNetwork(pureGen)
		evaluations.append(id + ' ' + str(score))

	foutput = open(fnoutput, 'w')
	for eval in evaluations:
		foutput.write(eval + '\n')
	foutput.close()

#patterns = [[1, -1, 1, -1, 1]]
#patterns = [[-1, 1, -1, 1, -1, 1, -1, 1, -1, 1],[1, -1, 1, -1, 1, -1, 1, -1, 1, -1]]

#patterns = [[-1, 1, -1, 1, -1, 1, -1, 1, -1, 1,
#             -1, 1, -1, 1, -1, 1, -1, 1, -1, 1,
#             -1, 1, -1, 1, -1, 1, -1, 1, -1, 1,
#             -1, 1, -1, 1, -1, 1, -1, 1, -1, 1,
#             -1, 1, -1, 1, -1, 1, -1, 1, -1, 1,
#             -1, 1, -1, 1, -1, 1, -1, 1, -1, 1,
#             -1, 1, -1, 1, -1, 1, -1, 1, -1, 1,
#             -1, 1, -1, 1, -1, 1, -1, 1, -1, 1,
#             -1, 1, -1, 1, -1, 1, -1, 1, -1, 1,
#             -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]]

patterns = [[-1, 1, -1, 1, -1, 1, -1, 1, -1, 1]]
evaluator = Evaluator(patterns)

spacing = 15

for i in xrange(spacing+1):
	evaluateBatch()

patterns.append([1, -1, 1, -1, 1, 1, -1, 1, -1, 1])
evaluator = Evaluator(patterns)

for i in xrange(spacing):
	evaluateBatch()

patterns.append([-1, 1, -1, 1, -1, -1, 1, -1, 1, -1])
evaluator = Evaluator(patterns)

for i in xrange(spacing):
	evaluateBatch()

patterns.append([1, -1, 1, -1, 1, -1, 1, -1, 1, -1])
evaluator = Evaluator(patterns)

while True:
	evaluateBatch()

#patterns = [[-1, 1, -1, 1, -1, 1, -1, 1, -1, 1],[1, -1, 1, -1, 1, -1, 1, -1, 1, -1]]
#evaluator = Evaluator(patterns)
#for i in xrange(1501):
#	evaluateBatch()
