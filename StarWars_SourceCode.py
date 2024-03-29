#import required:
import numpy as np

import nltk

import matplotlib.pyplot as plt

from collections import Counter

#import necessary from nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#download necessary files from the Natural Language Toolkit (downloaded most popular)
nltk.download()
#if needed: download stopwords from nltk
nltk.download('stopwords')


#create a list: separated by each line: line number, character name, and dialogue
sw_dic = []
with open("SW_EpisodeV.txt", "r") as text:
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
# print(sw_dic)



#create a numpy.ndarray of all character names
arr = np.array(sw_dic)

#create a list of all names
name_column = [row['name'] for row in arr]

#use Counter to count how many lines each character has and convert the list into a dictionary 
name_freq = dict(Counter(name_column))
print(name_freq)



#function to find the character that speaks the most frequent
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
print("The most active character in this episode is: ",most_frequent(name_column))



#use Counter to count how many lines each character has and create a list of the top three characters that speak the most
top_char = Counter(name_column)
top_three = top_char.most_common(3)

#convert the list into a dictionary of top three characters
top_three_dic = dict(top_three)
print(top_three_dic)

#using the dictionary top_three_dic, get only the dictionary keys (top 3 character names)
top_three_keys = top_three_dic.keys()

#using the dictionary top_three_dic, get only the dictionary values (how many lines each character has)
top_three_values = top_three_dic.values()

#create a pie chart of the top 3 most active characters using the top_three_dic
mycolors = ["orange", "magenta", "cyan"]
myexplode = (0.1, 0, 0) 
fig = plt.figure(figsize = (10,7))
plt.pie(top_three_values, labels = top_three_keys, autopct='%1.1f%%', shadow = True, colors = mycolors, explode = myexplode)
plt.title("Top 3 Most Active Characters")
plt.legend(title = "Character")
plt.show()



#using the dictionary name_freq, get only the dictionary keys (character names)
char_name_dic = name_freq.keys()

#using the dictionary name_freq, get only the dictionary values (how many lines each character has)
freq_dic = name_freq.values()

#create a bar chart comparing characters and the number of lines they have using the dictionary name_freq
Character = char_name_dic 
Frequency = freq_dic 
plt.bar(Character, Frequency, color=['purple'])
plt.title('Character Lines in SW Episode V')
plt.xlabel('Character', labelpad= -10)
plt.xticks(rotation = 'vertical')
plt.xticks(fontsize= 6)
plt.ylabel('Frequency')
plt.yticks(fontsize = 8)
plt.show()



#create a numpy.ndarray of the dialogue
dialogue_arr = np.array(sw_dic)
#convert it into a list of the dialogue
char_lines = [row['dialogue'] for row in dialogue_arr]

#remove outer punctuation
import string
excluded = set(string.punctuation)
char_lines = ' '.join(ch for ch in char_lines if ch not in excluded)

#remove the inner punctuation
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
no_punc_lines = " "
for char_punc in char_lines:
    if char_punc not in punc:
        no_punc_lines = no_punc_lines + char_punc
no_punc_lines = no_punc_lines

#remove stop words from the dialogue
stopWords = set(stopwords.words('english'))
words = word_tokenize(no_punc_lines)
filtered_dialogue = []
for w in words:
    if w not in stopWords:
        filtered_dialogue.append(w)
# print(filtered_dialogue)

#use Counter to create a list of the 20 most common words spoken
Count_no = Counter(filtered_dialogue)
common_words = Count_no.most_common(20)
#Convert the list into a dictionary of the 20 most common words
common_words_dic = dict(common_words)
print(common_words_dic)

#using the common_words_dic, get only the dictionary keys (words)
most_freq_words_used = common_words_dic.keys()

#using the common_words_dic, get only the dictionary values (how often the word occurs)
most_freq_words_used_values = common_words_dic.values()

#create a bar chart comparing 20 most common words and how often they occur using the common_words_dic
Word = most_freq_words_used
Word_Frequency = most_freq_words_used_values
plt.bar(Word, Word_Frequency, color=['orange'])
plt.title('Twenty Most Common Words Spoken in SW Episode V')
plt.xlabel('Word', labelpad= -4)
plt.xticks(rotation = 75)
plt.xticks(fontsize= 8)
plt.ylabel('Frequency')
plt.yticks(fontsize = 10)
plt.show()
