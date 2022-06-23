# StarWarsScriptProject

This is my CSIT505 Python project. I am using the Star Wars script from Episode V. I obtained this script from Kaggle.

Refer to the link: https://www.kaggle.com/datasets/xvivancos/star-wars-movie-scripts?select=SW_EpisodeV.txt

This program will turn the unstructured script into a structured and organized dataset. By using the line number, character name, and dialogue, important information can be retrieved. 

        Refer to the StarWars_Dataset.ipynb to view the entire structured printed out dataset.
        
        Refer to the StarWars_Project.ipynb for the Jupyter Notebook of the project.

Important goals of this project:
- Create a dictionary of all character names and the number of script lines they have.
- Find the most active character (the character that speaks the most/has the most lines in this episode).
- Find the top three most active characters.
- Create a pie chart comparing the top three most active characters.
- Create a bar chart comparing the characters and the number of script lines each character has.

- Create a dictionary of the 20 most common words spoken throughout this episode.
- Create a bar chart comparing the 20 most common words and how many times each was spoken.

- Create an interactive Python file. The user will download the Star Wars Episode V file off of Kaggle. The program will ask the user to input the file name. Then the program will ask the user to input a character name. Whichever character name is inputted, the user will retreieve all the lines for that specific character.

      Follow the instructions on the Interactive Star Wars.py file.
      

What was done:
Install required packages:

    pip install numpy
    
    pip install nltk
    
    pip install matplotlib

Import required:

    import numpy as np
    
    import nltk

    from collections import Counter
  
    import matplotlib.pyplot as plt
    
    from nltk.tokenize import word_tokenize
    from nltk.corpus import stopwords
 
Download necessary files from the National Language Toolkit (nltk): (downloaded most popular)

        nltk.download()

If needed, download the stopwords from the Natual Language ToolKit

        nltk.download('stopwords')



When the file opens, the first line is skipped, as this line is not necessay for analysis. All letters in the file will be lowercased and each line in the script will be split. Each line will be organized by line number, character name, and dialogue, and stored in a dictionary. This dictionary will then be stored in a list. 

Create a numpy.ndarray of all the character names in the episode. These names will be stored in a list. Using Counter from collections, the number of lines each character speaks throughout the episode is stored in a dictionary.

Define a function to find the character that speaks the most frequent, meaning they have the most lines in this episode and they are the most active.

Find the top 3 most active characters using the numpy.ndarray created for the names of the characters. Using Counter, the number of lines the top three character speaks will be stored in a list. This list is converted into a dictionary.

Splitting the dictionary into keys and values, use matplotlib to create a pie chart can be created comparing the top 3 most active characters.
- Title of pie chart: "Top 3 Most Active Characters"
- Colors: Orange, Magenta, and Cyan
- Labels: Character names
- Add percentage values
- Use a shadow for a more defined look
- Use explode to show the most active character
- Legend: shows the character names and their corresponding colors


Split the dictionary that contains all character names and number of lines they have in the script into the keys and values. The keys are the character names and the values are the number of lines they have in the script.

Using the keys and values, create a bar chart to compare the number of times each character speaks. Using matplotlib, the character names (x-axis) and frequency (y-axis) will be plotted and can easily be analyzed.
- Title of bar chart: "Character Lines in SW Episode V".
- Rotate x-axis tick marks (character names) vertically, due to the length
- Change x-axis font size to 6 for better readability (reduces overlapping of names)
- Set labelpad to -10: after adjusting the x-axis characer names, the x-axis title (Characters) was pushed down out of view, but by adjusting the labelpad, the title is more easily readable.
- Change y-axis font size to 8 for a more organized look.


Create a numpy.array of all the dialogue spoken throughout this episode. The dialogue will be stored in a list. Using this list, remove all punctuation. First, to import string, removing all punctuation from the outside. Then, the rest of the punctuation must be removed.

After removing all punctuation, remove all stopwords from the list. These stopwords are words that do not add much meaning to this analysis. After removing all stopwords from the dialgoue, the result will be stored in a list.

Create a list of the 20 most common words used throughout the episode using Counter. Convert the list into a dictionary to retreieve the keys and values. The keys are the words and the values are how often the word occurs. 

Using the keys and values, creatae a bar chart comparing the 20 most commmon words used throughout the episode and how often they occur. Using matplotlib, the words (x-axis) and the frequency (y-axis) will be plotted and can be easily analyzed.
- Title of bar chart: "Twenty Most Common Words Spoken in SW EPisode V"
- Rotate x-axis 75 degrees (words) for better readability
- Change x-axis font size to 8 for better readability
- Set labelpad to -4 so that the x-axis label is in view
- Change the y-axis font size to 10 for a more organized look


References:
Xavier. “Star Wars Movie Scripts.” Kaggle, 7 May 2018, https://www.kaggle.com/datasets/xvivancos/star-wars-movie-scripts?select=SW_EpisodeV.txt
