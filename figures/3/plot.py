#!/usr/bin/python2

import numpy as np
import matplotlib.pyplot as plt
import os
import fnmatch

xlimit = 2000
#colors = ['red', 'green', 'blue', 'violet', 'yellow']
methodColors = {'insdel1.0':'coral', 'insdel0.1':'darkviolet', 'insdel0.01':'teal'}
methodLabels = {'insdel1.0':'$r_{\mathrm{insdel}}=1.0$', \
                'insdel0.1':'$r_{\mathrm{insdel}}=0.1$', \
                'insdel0.01':'$r_{\mathrm{insdel}}=0.01$'}

def plotTS(ax, filename, plotColor, plotStd=True, label='nolabel', linestyle='-'):
	global xlimit, methodColors
	fitnessTS = np.loadtxt(filename)
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
		ax.plot(gens, fitnessMeanTS, color=plotColor, label=label, linestyle=linestyle)

def plotAllTS(ax, prefix, postfix):
	global methodColors
	for method in methodColors:
		for file in os.listdir('.'):
			if fnmatch.fnmatch(file, prefix + '*.' + postfix) and fnmatch.fnmatch(file, '*' + method + '*'):
				plotTS(ax, file, methodColors[method], plotStd=True, label=methodLabels[method])

plt.figure(figsize=(5.02, 4.02))

ax = plt.subplot(2,1,1)

plotAllTS(ax, 'afpo', 'fitness')
#ax.set_ylim(0, 1)
ax.set_xlim(0, 1500)
ax.set_ylabel('Fitness')
ax.legend(loc=4)
ax.set_xticklabels([])
ax.yaxis.set_major_locator(plt.MaxNLocator(3))
ax.xaxis.set_major_locator(plt.MaxNLocator(3))

ax = plt.subplot(2,1,2)

plotAllTS(ax, 'afpo', 'qvalue')
#ax.set_ylim(0, 1)
ax.set_xlim(0, 1500)
ax.set_ylabel('Q')
ax.set_xlabel('Generation')
ax.yaxis.set_major_locator(plt.MaxNLocator(3))
ax.xaxis.set_major_locator(plt.MaxNLocator(3))

plt.subplots_adjust(left=0.13, right=0.95, wspace=0.03, hspace=0.13, bottom=0.12, top=0.98)

plt.savefig('figure3.png', dpi=600)
plt.close()
