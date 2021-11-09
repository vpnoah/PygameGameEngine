# -*- coding: utf-8 -*-
import pygame
import itemdatabase
import interactiondatabase
"""
Created on Mon Aug 23 22:10:28 2021

@author: Noah
"""

"""
There are multiple types of tiles in the game. The walkable boolean determines
if they are able to be walked on. They also all have names. 
"""

class Tile():
    def __init__(self,x, walk):
        self.name = x
        self.img = pygame.image.load(x)
        self.walkable = walk

"""
Talking tiles have text when you interact with them, and may or may not
be able to be walked on.
"""

class TalkingTile():
    def __init__(self,x, walk):
        self.name = x
        self.img = pygame.image.load(x)
        self.walkable = walk
    
    def defineTalk(self, words):
        self.interactionText = words

"""
Item tiles have images for before and after you take the tile, as well
as the item name and the item icon. There is also a boolean that tracks
if the item has been taken yet.
"""

class ItemTile():
    def __init__(self, before, walk):
        items = itemdatabase.ItemDatabase()
        self.name = before
        self.img = pygame.image.load(before)
        self.walkable = walk
        items.readItems("itemtileguide.txt")
        self.img2 = pygame.image.load(items.afterTiles[self.name])
        self.icon = pygame.image.load(items.itemIcons[self.name])
        self.itemName = items.itemName[before]
        self.taken = False
    def changeTiles(self):
        self.img = self.img2
        self.taken = True

"""
Quest tiles are ones that give the player a quest. They have names, and
the interaction text when you interact with them, before
and after completing the quest. They also have a 
requirement for the item needed.
"""

class QuestTile():
    def __init__(self,x, walk):
        self.qda= interactiondatabase.questDatabase()
        self.qda.readQuests()
        self.name = x
        self.img = pygame.image.load(x)
        self.walkable = walk
        
    def defineTalk(self, words):
        self.interactionText = words
        
    def questReq(self, name):
        name.strip()
        self.item = name
    
    def updateText(self):
        self.defineTalk(self.qda.completedtext[self.name])