# -*- coding: utf-8 -*-

import tile
import interactiondatabase
"""
Created on Sat Aug 28 16:56:01 2021

@author: Noah
"""

"""
Below is an example tile data text file.

13 -- The number of tiles to be read
iceblock.png -- The name of the tile
W -- The type of tile it is
waterblock.png 
NW
polarbear2.png 
i
adventurepenguin.png
q
businesspeng.png
q
coolpengui.png
q
ghostpenguin.png
q
orangepengiun.png
q
appleblock.png
IT
hatblock.png
IT
keyblock2.png
IT
mapblock.png
IT
sodablock2.png
IT
"""

class tiledatabase():
    def __init__(self):

        self.tiles = [] 
        self.fileName = ""
        
    def readTiles(self, fileName):
        
        self.fileName = fileName
        
        file = open(fileName) #Opens the file
        
        imagecount = int(file.readline()) #The first line is the 
                                            #number of tiles to be read
        
        #Below opens up the interaction and quest database,
        #for when questtiles, item tiles, and talkable tiles are read
        i = interactiondatabase.interactionDatabase()
        i.readInteractions("interactionguide.txt")
        
        q = interactiondatabase.questDatabase()
        q.readQuests()
        
        for x in range(imagecount): #loops through the text file
                                    #based on the 'imagecount' variable from 
                                    #earlier
                                    
            text = file.readline() #The first line will be the image name
            walk = file.readline() #the next is the type of tile it is
            length = len(text) - 1
            
            walk = walk.strip()
            
            if walk == "W": #If it is W, creates a walkable tile
                t = tile.Tile(text[0 : length], True)
            elif walk == "I": #If it is I, creates a walkable, interactable tile
                t = tile.TalkingTile(text[0:length], True)
                t.defineTalk(i.interactions[t.name.strip()])
            elif walk == "i": #Interactable, non walkable tile
                t = tile.TalkingTile(text[0:length], False)
                t.defineTalk(i.interactions[t.name.strip()])
            elif walk == "IT": #Walkable Item Tile
                t = tile.ItemTile(text[0:length], True)
            elif walk == "q": #Non walkable quest tile
                t = tile.QuestTile(text[0:length], False)
                t.defineTalk(q.questtext[text[0:length]])
                t.questReq(q.questreq[text[0:length]])
            else: #Otherwise, a basic non walkable tile
                t = tile.Tile(text[0 : length], False)
            
            self.tiles.append(t) #adds that tile to the array of tiles
        

    def getTile(self, x): #method that returns a tile in the array
        return self.tiles[x]
    