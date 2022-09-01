#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Print the list of integers from  through  as a string, without spaces.



def print_function(num):
        my_list=[]
        for i in range(num,0,-1):
            my_list.append(str(i))
        return "".join(my_list)
print_function(5)


# In[ ]:




