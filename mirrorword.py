#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello, welcome to the word mirror")
x=str(input("enter the word:- "))
i=len(x)
for i in range(len(x),0,-1):
    i=i-1
    print(str(x[i]),end="")


# In[ ]:




