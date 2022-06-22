# StarWarsScriptProject

This is my CSIT505 Python project. I am using the Star Wars script from Episode V. I obtained this script from Kaggle.

Refer to the link: https://www.kaggle.com/datasets/xvivancos/star-wars-movie-scripts?select=SW_EpisodeV.txt

This program will turn the unstructured script into a structured and organized script. By using the line number, character name, and dialogue, important information can be retrieved. 

        Refer to the StarWars_Dataset.ipynb to view the entire structured dataset used for this project.

Some important goals of this project:
- Create a dictionary of all character names and the number of script lines they have.
- Find the most active character (the character that speaks the most/has the most lines in this episode).
- Find the top three most active characters.
- Create a pie chart comparing the top three most active characters.
- Create a bar chart comparing the characters and the number of script lines each character has.

- Create a dictionary of the 20 most common words spoken throughout this episode.
- Create a bar chart comparing the 20 most common words and how many times each was spoken.

- Create an interactive Python file. The user will download the Star Wars Episode V file off of Kaggle. The program will ask the user to input the file name. Then the program will ask the user to input a character name. Whichever character name is inputted, the user will retreieve all the lines for that specific character.

      Follow the instructions on the Interactive Star Wars.py file.

Install required packages:

    pip install numpy
    
    pip install nltk
    
    pip install matplotlib

Import required:

    import numpy as np
    
    import nltk

    from collections import Counter
  
    import matplotlib.pyplot as plt
 
Download necessary files from the National Language Toolkit (nltk): (downloaded most popular)

        nltk.download()


When the file opens, the first line is skipped, as this line is not necessay for analysis. All letters in the file will be lowercased and then split. Each line will be organized by line number, character name, and dialogue, and stored in a dictionary. This dictionary will then be stored in a list. 

Create a numpy.ndarray of all the character names in the episode. These names will be stored in a list. Using Counter from collections, the number of lines each character speaks throughout the episode is stored in a dictionary.

Define a function to find the character that speaks the most frequent, meaning they have the most lines in this episode and they are the most active.

Find the top 3 most active characters using the numpy.ndarray created for the names of the characters. Using Counter, the number of lines the top three character speaks will be stored in a list. This list is converted into a dictionary. Splitting the dictionary into keys and values, a pie chart can be created comparing the top 3 most active characters.
- Title of chart is "Top 3 Most Active Characters"
- Colors: Orange, Magenta, and Cyan
- Labels: Character names
- Add percentage values
- Use a shadow for a more defined look
- Use explode to show the most active character
- Legend: shows the character names and their corresponding colors


Split the dictionary that contains all character names and number of lines they have in the script into the keys and values. The keys are the character names and the values are the number of lines they have in the script.

Using the keys and values, create a bar chart to compare the number of times each character speaks. The title of this bar chart is "Character Lines in SW Episode V". Using matplotlib, the character names (x-axis) and frequency (y-axis) will be plotted and can easily be analyzed. Due to the length of some of the character names, the x-axis tick marks (the character names) were rotated vertically and made a size 6 font for better readability. After adjusting the x-axis characer names, the x-axis title (Characters) was pushed down out of view, but by setting the labelpad to -10, the title is more easily readable. The y-axis is set to a font size of 8 for a more organized look.


Create a numpy.array of all the dialogue spoken throughout this episode. The dialogue will be stored in a list. Using this list, remove all punctuation. First, to import string, removing all punctuation from the outside. Then, the rest of the punctuation must be removed.


After removing all punctuation, remove all stopwords from the list. These stopwords are words that do not add much meaning to this analysis.

    from nltk.tokenize import word_tokenize
    from nltk.corpus import stopwords

If needed, download the stopwords from the Natual Language ToolKit

    nltk.download('stopwords')

Then all stopwords will be removed from the dialgoue, storing the result in a list.

Create a list of the 20 most common words used throughout the episode using Counter. Convert the list into a dictionary to retreieve the keys and values. The keys are the words and the values are how often the word occurs. 

Using the keys and values, creatae a bar chart comparing the 20 most commmon words used throughout the episode and how often they occur. The title of this bar chart is "Twenty Most Common Words Spoken in SW EPisode V". Using matplotlib, the words (x-axis) and frequency (y-axis) will be plotted and can be easily analyzed. For better readability and organization, the x-axis is rotated 75 degrees and has a fontsize of 8. The labelpad is set to -4 so that the x-axis label is in view. The y-axis is set to a font size of 10 for a more organized look.
