# -*- coding: utf-8 -*-

import tilemapclass
import pygame
import tile
import tiledatabase
"""
Created on Thu Aug 26 21:58:13 2021

@author: Noah

sample text file for a map file

10 - Length of array
10 - With of array 
0000000001 - each int/character corresponds to a tile
0000000002
0000000003
0000000004
0000000005
0000000006
0000000007
0000000000
0000000000
0000cba980

"""
def createMap(mapName): #This method creates a map object
    
    corresponding = {} #Creates a dictionary of characters with tile files.
    
    file = open("tileimagecorresponding.txt") #this text file links certain
                                        #tiles to characters on the map
    
    """
    In the tileimagecorresponding file, the tiles are associated with the
    order in the tiledatabase. The first tile in the tiledatabse is ice
    so 0 on the map would be ice, the second is water so 1 would be water.
    Past 10, I use letters in order to mantain one character each.
    """
   
    count = file.readline() #this is the number of tiles to be read
        
    for x in range(int(count)): #This code reads the tile corresponding text file
        name = file.readline() #takes the character read
        text = file.readline() #this is the number of tile in the database
        name = name[0: len(name)-1]
        text = text[0: len(text)-1]
        corresponding[name] = text
    
    td = tiledatabase.tiledatabase() #opens a tile database
    td.readTiles("tiledata.txt") #gives the tile database data from the file
     
    file = open(mapName) #opens the map
     
    ints = [] #this will be an array of ints of the data in the map
              #this will be transfered to the map constructor in order
              #to determine what tiles are in the map
    
    width = int(file.readline()) #takes the width and height of the map
    height = int(file.readline())
    
    num = width*height*2 #multiplies by two to account for random spaces
                        #in the map files
    
    for x in range(num): #goes through the map files
       y = file.read(1) 
       if y != " " and y!= "\n" and y != '': #if the character read is not a space
           z = corresponding[y]
           ints.append(z)
    
    #creates a map, inputting the array of tiles from the database, the
    #array of int values of the map, and the width and height of the map
    map = tilemapclass.Map(td.tiles, ints, width, height)    
    
    file.close()
    
    return map #returns a map object





