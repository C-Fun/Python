# -*- coding: utf-8 -*-
"""
Created on Mon May 01 01:32:11 2017

@author: Fun
"""

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
#fig图表对象
#ax图表对象对应的区域
ax.plot(10*np.random.randn(100), 10*np.random.randn(100), 'o')
ax.set_title('Simple Scatter')

plt.show()