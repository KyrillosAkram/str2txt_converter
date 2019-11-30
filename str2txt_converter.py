#!/usr/bin/env python
# coding: utf-8

# In[88]:


strfile= open(input("enter the str file full path :\n\a"),'r',buffering=1024**2)
txtfile= open("output.txt",'a')


# In[89]:


import regex as re
from bs4 import BeautifulSoup


# In[90]:


niv=BeautifulSoup(strfile,"lxml")


# In[91]:


allText=niv.findAll("font")


# In[92]:


for line in allText :
    txtfile.write(line.get_text()+'\n')
txtfile.close()
strfile.close()

