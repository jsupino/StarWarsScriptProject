# StarWarsScriptProject
StarWarsProject101

This is my CSIT505 project. I am using the Star Wars script from Episode V. I obtained this script from Kaggle.

Refer to the link: https://www.kaggle.com/datasets/xvivancos/star-wars-movie-scripts?select=SW_EpisodeV.txt

This program will turn the unstructured data into structured data. By utilizing the line number, character name and dialogue, important information can be retrieved. Finding the character that talks the most, meaning that they have the most script lines in this episode. Creating a bar chart of the characters, comparing the number of script lines between each character.

Install required packages:


    pip install numpy

    pip install matplotlib



Import required:


    import numpy as np

    from collections import Counter
  
    import matplotlib.pyplot as plt



Open the file and split the data, storing it in a list. Organized the information in each line by line number, name of the character, and the dialogue.

Create a numpy.ndarray and retrieve all the character names used. Create a list of the names.

By creating this list of character names, find the number of times each character speaks.

Find the character that speaks the most throughout the episode.

Split the list of characters data into the keys (character names) and values (number of lines they have in the script)find the character that speaks the most.

By finding this data, a bar chart can be created utilzing matplotlib to compare the number of times each character speaks.
