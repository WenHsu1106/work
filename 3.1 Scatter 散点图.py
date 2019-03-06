#!/usr/bin/env python
# coding: utf-8

# In[13]:


#https://morvanzhou.github.io/tutorials/data-manipulation/plt/3-1-scatter/
import matplotlib.pyplot as plt 
import numpy as np

n= 1024
X=np.random.normal(0,1,n) #產生标准正态分布的二维数据组 平均數是0，方差為1，生成n個數
Y=np.random.normal(0,1,n)
T = np.arctan2(Y,X) #for color value
plt.scatter(X, #location x
            Y, #location y
            s=10, #size
            c=T, #color值，他會對上一個color map
            alpha=2#透明度
           )

plt.xlim((-1.5,1.5))
plt.ylim((-1.5,1.5))

plt.xticks(()) #隱藏 x軸ticks
plt.yticks(()) #隱藏 y軸ticks
plt.show()


# In[6]:


plt.scatter(np.arange(5),np.arange(5))
plt.xticks(()) #隱藏 x軸ticks
plt.yticks(()) #隱藏 y軸ticks
plt.show()


# In[ ]:




