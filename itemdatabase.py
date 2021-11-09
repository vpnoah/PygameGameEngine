# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 09:26:33 2021

@author: Noah
"""

"""
Below is an example item database file
5 - Number of items to be read
appleblock.png - The image before the item is picked up
iceblock.png - The image after the item is picked up
appleicon.png - The icon of the image that will appear when picked up
Apple - The name of the item
hatblock.png
iceblock.png
haticon.png
Hat
sodablock2.png
iceblock.png
sodaicon.png
Soda
mapblock.png
iceblock.png
mapicon.png
Map
keyblock2.png
iceblock.png
keyicon.png
Key
"""

class ItemDatabase():
    def __init__(self):

        self.afterTiles = {} #Three dictionaries that hold the data
        self.itemIcons = {}
        self.itemName = {}

    def readItems(self,fileName):
        file = open(fileName) #Opens the file and figures out how many items
        times = file.readline() #will be read
        
        for x in range(int(times)): #loops through the file
        
            """
            Below the code takes in data for the before image,
            the after image, the item name, and the icon image.
            This data is put into the dictionaries.
            """
        
            before = file.readline() #name of the image
            before = before[0: len(before)-1]
            before.strip()
            
            after = file.readline() #after image
            after = after[0: len(after)-1]
            
            icon = file.readline()
            icon = icon[0: len(icon)-1]
            
            name = file.readline()
            name.strip()
            
            self.afterTiles[before] = after
            self.itemIcons[before] = icon
            self.itemName[before] = name
            
            
       