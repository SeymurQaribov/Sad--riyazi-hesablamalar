#!/usr/bin/env python
# coding: utf-8

# Hansı məbləğin 5/12 hissəsi 100 manatın 3+(3\4) hissəsinə bərabər olacaq.

# In[1]:


import math
from __future__ import division


# In[2]:


p1 = 5/12
p2 = 3 + (3/4)
a = 100


# In[3]:


x = p2*a/p1
print("Tələb olunan məbləğ",x,'AZE')


# 4 əkinçi 30 gündə 40 hektar taxil biçərsə, 18 əkinçi 12 gündə neçə hektar taxəl biçər.

# In[4]:


import math 
from __future__ import division#i don't need it ,just for remember syntaxsis


# In[6]:


N1 = 4
D1 = 30
D2 = 12
W1 = 40
N2 = 18


# In[9]:


W2 = N2*D2*W1/(D1*N1)
print("Hektarlarin sayi",W2)


# Əgər a/a+b = 17/23,bu zaman a+b/a-b nəyə bərabərdir?
# 

# In[10]:


a = 17
aplusb = 23


# In[11]:


b = aplusb - a
natice = aplusb/(a-b)


# In[14]:


print('netice',natice)


# 2 + √2 + 1/(2+√2) + 1/(√2-2) = ?

# In[15]:


a = 2
b = math.sqrt(2)


# In[16]:


c = 1/(a+b)
d = 1/(b-a)
netice = a + b + c +d


# In[18]:


print('netice',round(netice,2))


# Mal ətinin qiyməti 3% artırılırsa, evdar qadın mal ətinin istehlakını neçə faiz azaltmalıdır kiç əlavə xərc çıxmasın?

# In[19]:


a = 3
b = a*100/(a+100)


# In[21]:


print('Istehlakda',round(b,3),'% azalma olmalidi')


# T-test

# In[1]:


import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import scipy.stats as stats
import math


# In[2]:


np.random.seed(6)


populations_age1 = stats.poisson.rvs(loc = 18, mu = 35, size = 150000)

populations_age2 = stats.poisson.rvs(loc = 18, mu = 10, size = 100000)

populations_age =np.concatenate((populations_age1, populations_age2))


minnestona_age1 = stats.poisson.rvs(loc = 18, mu = 30, size= 30)

minnestona_age2 = stats.poisson.rvs(loc = 18, mu = 10, size = 20)

minnestona_age = np.concatenate((minnestona_age1, minnestona_age2))


print(populations_age.mean())
print(minnestona_age.mean())


# In[3]:


stats.ttest_1samp(a = minnestona_age,
                 popmean = populations_age.mean())


# In[ ]:




