# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 00:15:55 2021

@author: DELL
"""

       
import matplotlib.pyplot as plt
import numpy as np


a=[]
for i in range(-1000,1000):
    a.append(i)

a=np.array(a)
b=np.array(a)
a=a/100

b=a**3+100

plt.plot(a,b)
