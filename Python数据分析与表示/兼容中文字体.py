# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 12:34:25 2017

@author: Fun
"""

import numpy as np
from matplotlib.font_manager import FontProperties  
import matplotlib.pyplot as plt  


font = FontProperties(fname=r"c:\windows\fonts\simkai.ttf", size=20)    

a = np.arange(0.0,5.0,0.02)

plt.xlabel(u'横轴：时间',fontproperties='SimHei',fontsize=20)
plt.ylabel(u'纵轴：振幅',fontproperties='SimHei',fontsize=20)


plt.xlabel(u'横轴：时间',fontproperties=font)
plt.ylabel(u'纵轴：振幅',fontproperties=font)
plt.plot(a, np.cos(2*np.pi*a), 'r--')
plt.show()