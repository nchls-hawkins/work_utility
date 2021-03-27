
# coding: utf-8

# In[12]:


track_detail = input('track detail')
new_list = track_detail.split()
matches = [x for x in new_list if x == '1']
print(len(matches)-1)


# In[8]:


new_list = track_detail.split()
matches = [x for x in new_list if x == '1']


# In[9]:


print(len(matches))

