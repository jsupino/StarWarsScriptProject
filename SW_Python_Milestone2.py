#import required:
import numpy as np

import matplotlib.pyplot as plt

from collections import Counter

#create list: separated by each line: line number, character  name, and dialogue
sw_dic = []
with open("C:/Users/supin/Desktop/starwars/SW_EpisodeV.txt", "r") as text:
    text = text.readlines()[1:]  #skip first line in file
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

#create a list of all the names, line by line
arr = np.array(sw_dic)
name_column = [row['name'] for row in arr]
# create  a dictionary of how many lines each character has
c = dict(Counter(name_column))
print(c)

#find the character that speaks the most frequent
def most_frequent(name_column):
    counter = 0
    num = name_column[0]
    for i in name_column:
        freq = name_column.count(i)
        if(freq>counter):
            counter = freq
            num = i
    return num
#print the character with the most lines
print("The character with the most lines in this episode is:",most_frequent(name_column))

#print only the character names
d = c.keys()
print(d)

#print only the values of how many lines each character has
e = c.values()
print(e)

#create a bar chart comparing characters and the number of lines they have
Character = d
Frequency = e
plt.bar(Character, Frequency, color=['purple'])
plt.title('Character Lines in SW Episode V')
plt.xlabel('Character', labelpad= -10)
plt.xticks(rotation = 'vertical')
plt.xticks(fontsize= 6)
plt.ylabel('Frequency')
plt.yticks(fontsize = 8)
plt.show()



