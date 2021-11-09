# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 19:54:43 2021

@author: Noah
"""

"""
Below is an example interaction database text file.

3 - Number of interactions to record
question.png - The image name of the tile to interact with
You stepped on a question block - The interaction text
polarbear2.png
Roar
exclaim.png
You can't step here
"""

class interactionDatabase():
    def __init__(self):
        self.interactions = {} #Creates a dictionary of interactions
        
    def readInteractions(self, fileName):
        
        """
        The below code opens the file then reads the amount of iteractions.
        Looping through the file, it reads the file name then the interaction
        text, and then puts that information in the dictionary.
        """
        
        file = open(fileName)
        times = file.readline()
        
        for x in range(int(times)):
            name = file.readline()
            name = name[0: len(name)-1]
            name.strip()
            text = file.readline()
            self.interactions[name] = text
        
   
"""
Below is an example text file from the quest database text file.

5 - Number of quests to be read
adventurepenguin.png - The image for the tile that has a quest
I lost my map! - The before quest text
Map - The item needed
Thank you! - The after quest text
businesspeng.png
Hey, I lost my key
Key
Yayyyyyy!
coolpengui.png
I lost my soda, can you find it for me
Soda
Wow, thanks
ghostpenguin.png
I've seen to lost my hat 
Hat
Now my head can stay warm 
orangepengiun.png
I lost my apple
Apple
Thank you
end of file
"""

class questDatabase():
    def __init__(self):
        
        self.questtext = {} #Three dictionaries hold information about the quests
        self.questreq = {}
        self.completedtext = {}
        self.completed = False

    def readQuests(self):
        
        """
        The below code opens up the file and loops through. First reading
        the name of the image of the quest tile. It then reads in the
        before and after text, as well as the needed item name. It then
        puts that information into dictionaries.
        """
        
        file = open("questdata.txt")
        times = file.readline()
        
        for x in range(int(times)):
            
            name = file.readline()
            name = name[0: len(name)-1]
            text = file.readline()
            req = file.readline()
            comp= file.readline()
            self.questtext[name] = text
            self.questreq[name] = req
            self.completedtext[name] = comp
        
        
       

