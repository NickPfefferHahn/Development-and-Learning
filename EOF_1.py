
# coding: utf-8

# In[2]:


name = input('Enter name: ')
print('Hello ' + name)


# In[6]:


hours = float(input('Hours worked: '))
rate_of_pay = float(input('Income per hour: '))
total = (hours * rate_of_pay)
print(total)


# In[18]:


w = 17
sauce = w//2
type(sauce)


# In[19]:


w = 17
sauce = w/2.0
type(sauce)


# In[20]:


h = 12.0
sauce = h/3
type(sauce)


# In[21]:


h = 1+2*3
type(h)


# In[29]:


celcius = input('Please input degrees in Celcius: ')
fahrenheit = (int(celcius) * 1.8 + 32)
print(fahrenheit)

