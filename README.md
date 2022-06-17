# StarWarsScriptProject

This is my CSIT505 Python project. I am using the Star Wars script from Episode V. I obtained this script from Kaggle.

Refer to the link: https://www.kaggle.com/datasets/xvivancos/star-wars-movie-scripts?select=SW_EpisodeV.txt

This program will turn the unstructured data into structured data. By utilizing the line number, character name and dialogue, important information can be retrieved. Finding the character that talks the most, meaning that they have the most script lines in this episode. Creating a bar chart of the characters, comparing the number of script lines between each character.

Install required packages:

    pip install numpy

    pip install matplotlib

Import required:

    import numpy as np

    from collections import Counter
  
    import matplotlib.pyplot as plt

When opening the file, skip the first line, as this line is not necessay for analysis. All letters in the file will be lowercased and then split. Each line will be organized by line number, character name, and dialogue, and stored in a dictionary. This dictionary will then be stored in a list. 

Create a numpy.ndarray and retrieve all the character names used. These names will be stored in a list. Using Counter from collections, the number of lines each character speaks throughout the episode is stored in a dictionary.

Define a function to find the character that speaks the most frequent, meaning they have the most lines in this episode.

Split the dictionary that contains all character names and number of lines they have in the script into the keys and values. The keys are the character names and the values are the number of lines they have in the script.

Using the keys and values, create a bar chart to compare the number of times each character speaks. Using matplotlib, the character names (x-axis) and frequency (y-axis) will be plotted and can easily be analyzed. Due to the length of some of the character names, the x-axis tick marks (the character names) were rotated vertically and made a size 6 font for better readability. After adjusting the x-axis characer names, the x-axis title (Characters) was pushed down out of view. Setting labelpad to -10, the title is more easily readable. The y-axk marks were set to a font size of 8 for a more organized look.
