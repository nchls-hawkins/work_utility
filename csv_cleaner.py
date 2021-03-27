
# coding: utf-8

# In[12]:


Hot_list = input('hot_list')
new_list = Hot_list.split()
unit_numbers = []
for i,x in enumerate(new_list):
    if i %2 == 0:
        unit_numbers.append(x)
clean_numbers = []
for i in unit_numbers:
    if len(i) == 6:
        clean_numbers.append(int(i))
    else:
        clean_numbers.append(int(i[4:10]))
print(str(clean_numbers[0:20]).replace(' ',''))
print(str(clean_numbers[20:40]).replace(' ',''))
print(str(clean_numbers[40:60]).replace(' ',''))
print(str(clean_numbers[60:80]).replace(' ',''))

