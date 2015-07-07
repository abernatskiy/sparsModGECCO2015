#!/usr/bin/python2

import numpy as np
import matplotlib.pyplot as plt
import os
import fnmatch

xlimit = 2000
#colors = ['red', 'green', 'blue', 'violet', 'yellow']
methodColors = {'clune_random':'red', 'clune_sparse':'blue', 'afpo_sparse':'green'}

def plotTS(ax, filename, plotColor, plotStd=True, label='nolabel', coefficient=1):
	global xlimit
	fitnessTS = np.loadtxt(filename)*coefficient
	fitnessMeanTS = np.mean(fitnessTS, axis=1)
	fitnessStdTS = np.std(fitnessTS, axis=1)*1.96/np.sqrt(float(fitnessTS.shape[1]))

	fitnessLower = fitnessMeanTS - fitnessStdTS
	fitnessUpper = fitnessMeanTS + fitnessStdTS

	gens = np.arange(0,len(fitnessMeanTS))

	if xlimit <= 30:
		ax.errorbar(gens, fitnessMeanTS, color=plotColor, yerr=fitnessStdTS, label=filename)
	else:
		if plotStd:
			ax.plot(gens, fitnessLower, gens, fitnessUpper, color=plotColor, alpha=0.5)
			ax.fill_between(gens, fitnessLower, fitnessUpper, where=fitnessUpper>=fitnessLower, facecolor=plotColor, alpha=0.3, interpolate=True)
		ax.plot(gens, fitnessMeanTS, color=plotColor, label=label)

def plotAllTS(ax, prefix, postfix, coefficient=1):
	global methodColors
	for method in methodColors:
		for file in os.listdir('.'):
			if fnmatch.fnmatch(file, prefix + '*.' + postfix) and fnmatch.fnmatch(file, '*' + method + '*'):
				plotTS(ax, file, methodColors[method], plotStd=True, label='fgsfds', coefficient=coefficient)

def shrinkYAxis(ax, strength):
	bb = ax.get_position()
	axwidth = bb.x1 - bb.x0
	axheight = bb.y1 - bb.y0
	bb.y0 += strength*axwidth
	bb.y1 -= strength*axwidth
	ax.set_position(bb)

	ax.yaxis.set_major_locator(plt.MaxNLocator(3))
	ax.xaxis.set_major_locator(plt.MaxNLocator(3))

genVanilla = 250
genComplex = 1000

yshrink = 0.0

taskBtype = 'medium'

#fig = plt.figure(figsize=[5,5])

print 'Plotting fitness...'

ax = plt.subplot(3,2,1)
plotAllTS(ax, 'vanilla', 'fitness')
ax.set_ylim(-0.1, 1)
ax.set_xlim(0, genVanilla)
ax.set_ylabel('Fitness')
ax.set_title('N=10')
ax.set_xticklabels([])
ax.set_xscale('log')
ax.set_xlim(1, 250)
shrinkYAxis(ax, yshrink)

ax = plt.subplot(3,2,2)
plotAllTS(ax, taskBtype, 'fitness')
ax.set_ylim(-0.1, 1)
ax.set_xlim(0, genComplex)
ax.set_title('N=30')
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_xscale('log')
ax.set_xlim(1, 2225)
shrinkYAxis(ax, yshrink)

print 'Plotting qvalue...'

ax = plt.subplot(3,2,3)
plotAllTS(ax, 'vanilla', 'qvalue')
ax.set_ylim(0, 1)
ax.set_xlim(0, genVanilla)
ax.set_ylabel('Q')
ax.set_xticklabels([])
ax.set_xscale('log')
ax.set_xlim(1, 250)
shrinkYAxis(ax, yshrink)

ax = plt.subplot(3,2,4)
plotAllTS(ax, taskBtype, 'qvalue')
ax.set_ylim(0, 1)
ax.set_xlim(0, genComplex)
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_xscale('log')
ax.set_xlim(1, 2225)
shrinkYAxis(ax, yshrink)

print 'Plotting density...'

ax = plt.subplot(3,2,5)
plotAllTS(ax, 'vanilla', 'density', coefficient=0.01)
ax.set_xlim(0, genVanilla)
ax.set_yscale('log')
ax.set_ylabel('Density')
ax.set_xlabel('Generations')
ax.set_xscale('log')
ax.set_xlim(1, 250)
ax.set_ylim(0.001, 1)

#ax.xaxis.set_major_locator(plt.MaxNLocator(3))

ax = plt.subplot(3,2,6)
plotAllTS(ax, taskBtype, 'density', coefficient=0.0001)
ax.set_xlim(0, genComplex)
ax.set_yscale('log')
ax.set_xlabel('Generations')
ax.set_ylim(0.001, 1)
ax.set_xscale('log')
ax.set_xlim(1, 2225)
ax.set_yticklabels([])

#ax.xaxis.set_major_locator(plt.MaxNLocator(3))

plt.subplots_adjust(left=0.08, right=0.94, wspace=0.05, hspace=0.13, bottom=0.07, top=0.96)

plt.savefig('figure1.png', dpi=300)
#plt.savefig('figure1.eps')
plt.close()

#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
