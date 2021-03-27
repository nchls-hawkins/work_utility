
# coding: utf-8

# In[8]:


import urllib.request, urllib.parse, urllib.error
import ssl
import json


# In[9]:


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# In[10]:


url = input('url?')
data= urllib.request.urlopen(url, context=ctx)
data = json.loads(data)
print(data)

