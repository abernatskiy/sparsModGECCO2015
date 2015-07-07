#!/usr/bin/python2

import numpy as np
import matplotlib.pyplot as plt
import os
import fnmatch

xlimit = 2000
#colors = ['red', 'green', 'blue', 'violet', 'yellow']
methodColors = {'clune_random':'red', 'clune_sparse':'blue', 'afpo_sparse':'green'}

def plotTS(ax, filename, plotColor, plotStd=True, label='nolabel', linestyle='-'):
	global xlimit
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
				plotTS(ax, file, methodColors[method], plotStd=True, label='fgsfds')

def forceAspect(ax,aspect=1):
    im = ax.get_images()
    extent =  im[0].get_extent()
    ax.set_aspect(abs((extent[1]-extent[0])/(extent[3]-extent[2]))/aspect)

def shrinkYAxis(ax, strength):
  bb = ax.get_position()
  axwidth = bb.x1 - bb.x0
  axheight = bb.y1 - bb.y0
  bb.y0 += strength*axwidth
  bb.y1 -= strength*axwidth
  ax.set_position(bb)

  ax.yaxis.set_major_locator(plt.MaxNLocator(3))
  ax.xaxis.set_major_locator(plt.MaxNLocator(3))

plt.figure(figsize=(10.24, 5.02))
yshrink=0.5

ax = plt.subplot(2,3,1)
plotAllTS(ax, 'mvg15', 'fitness')
ax.set_ylim(0, 1)
ax.set_xlim(0, 60)
#ax.set_xticks([0,15,30,45,60])
ax.set_xticks([0,30,60])
ax.set_ylabel('Fitness')
ax.set_title('K=15')
ax.set_xticklabels([])
shrinkYAxis(ax, yshrink)

ax = plt.subplot(2,3,2)
plotAllTS(ax, 'mvg100', 'fitness')
ax.set_ylim(0, 1)
ax.set_xlim(0, 400)
#ax.set_xticks([0,100,200,300,400])
ax.set_xticks([0,200,400])
ax.set_title('K=100')
ax.set_xticklabels([])
ax.set_yticklabels([])
shrinkYAxis(ax, yshrink)

ax = plt.subplot(2,3,3)
plotAllTS(ax, 'mvg500', 'fitness')
ax.set_ylim(0, 1)
ax.set_xlim(0, 2000)
#ax.set_xticks([0,500,1000,1500,2000])
ax.set_xticks([0,1000,2000])
ax.set_title('K=500')
ax.set_xticklabels([])
ax.set_yticklabels([])
shrinkYAxis(ax, yshrink)

ax = plt.subplot(2,3,4)
plotAllTS(ax, 'mvg15', 'qvalue')
plotTS(ax, 'vanilla_afpo_sparse_expl0.5_insdel1.0.qvalue', 'black', plotStd=False, linestyle='--')
ax.set_ylim(0, 1)
ax.set_xlim(0, 60)
#ax.set_xticks([0,15,30,45,60])
ax.set_xticks([0,30,60])
ax.set_ylabel('Q')
ax.set_xlabel('Generation')
shrinkYAxis(ax, yshrink)

ax = plt.subplot(2,3,5)
plotAllTS(ax, 'mvg100', 'qvalue')
plotTS(ax, 'vanilla_afpo_sparse_expl0.5_insdel1.0.qvalue', 'black', plotStd=False, linestyle='--')
ax.set_ylim(0, 1)
ax.set_xlim(0, 400)
#ax.set_xticks([0,100,200,300,400])
ax.set_xticks([0,200,400])
ax.set_xlabel('Generation')
ax.set_yticklabels([])
shrinkYAxis(ax, yshrink)

ax = plt.subplot(2,3,6)
plotAllTS(ax, 'mvg500', 'qvalue')
plotTS(ax, 'vanilla_afpo_sparse_expl0.5_insdel1.0.qvalue', 'black', plotStd=False, linestyle='--')
ax.set_ylim(0, 1)
ax.set_xlim(0, 2000)
#ax.set_xticks([0,500,1000,1500,2000])
ax.set_xticks([0,1000,2000])
ax.set_xlabel('Generation')
ax.set_yticklabels([])
shrinkYAxis(ax, yshrink)

#plt.tight_layout()
plt.subplots_adjust(left=0.06, right=0.98, wspace=0.06, hspace=0.05, bottom=0.15, top=0.90)

plt.savefig('figure2.png', dpi=600)
plt.close()
