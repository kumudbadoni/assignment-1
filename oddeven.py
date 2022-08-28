#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("please enter your seies and do not forget to give space between two numbers")
x = [int(a) for a in input().split()]
b=0
c=0
for i in x:
        if i%2==0:
            b+=1
        else:
            c+=1
print("Number of even numbers:-",b)
print("Number of odd numbers:-",c)


# In[ ]:




