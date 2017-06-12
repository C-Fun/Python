# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 23:18:52 2017

@author: Fun
"""
import numpy as np
import matplotlib.pyplot as plt
plt.subplot(3,3,5)
plt.plot([0,2,4,6,8],[3,1,4,5,2])
plt.ylabel("grade")
#plt.savefig('D:/test',dpi=600)
plt.axis([-1,10,0,6])
plt.show()

a = np.arange(10)
plt.plot(a,a*1.5,'go-', a,a*2.5,'rx', a,a*3.5, '*',a,a*4.5, 'b-.')
plt.show()