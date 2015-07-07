#!/usr/bin/python2

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)

fig = plt.figure()
ax = plt.subplot(111)

ax.plot(x, 1 * x, label='P&CC-sparse', color='blue')
ax.plot(x, 2 * x, label='P&CC-random', color='red')
ax.plot(x, 3 * x, label='P&TSM-sparse', color='green')

# Shrink current axis's height by 10% on the bottom
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])

# Put a legend below current axis
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=False, shadow=False, ncol=3)

plt.savefig('legend.png', dpi=600)
