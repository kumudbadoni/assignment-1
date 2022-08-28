#!/usr/bin/env python
# coding: utf-8

# In[6]:


a=0
b=1
x=int(input("enter the number:- "))
if x==0:
    print(a)
elif x==1:
    print(b)
else:
    print(a,end=" ")
    print(b,end=" ")
    for i in range(0,x+1):
        n=a+b
        a=b
        b=n
        print(n ,end=" ")


# In[ ]:





# In[ ]:




