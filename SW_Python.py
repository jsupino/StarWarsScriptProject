#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import matplotlib.pyplot as plt


# In[3]:


from collections import Counter


# In[4]:


sw_dic = []
with open("C:/Users/supin/Desktop/starwars/SW_EpisodeV.txt", "r") as text:
    text = text.readlines()[1:]  #skip first line
    for line in text:
        line = line.lower().split('"') #lowercase all words and split by quotes
        dialogue = line.pop(5)
        name = line.pop(3)
        line_number = line.pop(1)
        new_obj = {
            "line": line_number,
            "name": name,
            "dialogue": dialogue
        }
        sw_dic.append(new_obj)
#print out each line separately by line number, character name, and dialogue
print(sw_dic)


# In[24]:


arr = np.array(sw_dic)
name_column = [row['name'] for row in arr]
#print out all character names
print(name_column)


# In[25]:


#print out how many times each character speaks
c = dict(Counter(name_column))
print(c)


# In[26]:


def most_frequent(name_column):
    counter = 0
    num = name_column[0]
    for i in name_column:
        freq = name_column.count(i)
        if(freq>counter):
            counter = freq
            num = i
    return num
c = dict(Counter(name_column))

# #print the most frequent character
print("The character with the most lines in this episode is:",most_frequent(name_column))


# In[27]:


#print only the character names
d = c.keys()
print(d)


# In[28]:


# #print only the values of how many times each character speaks
e = c.values()
print(e)


# In[29]:


#create a bar chart
Character = d
Frequency = e

plt.bar(Character, Frequency)
plt.title('Frequency of Character Lines in SW Episode V')
plt.xlabel('Character')
plt.xticks(rotation = 90)
plt.xticks(fontsize= 7.5)
plt.ylabel('Frequency')
plt.show()


# In[ ]:




