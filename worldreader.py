# -*- coding: utf-8 -*-
import tilemapclass
import tilemaptextreader
import tiledatabase

"""
Created on Sat Aug 28 12:54:43 2021

@author: Noah
"""
"""
Below is an example world file
2 - The dimensions of the world
2
map1.txt - These are the files to read from to make the world
map2.txt
map3.txt
map4.txt
end of file

the layout of the above data would be
[map1][map2]
[map3][map4]

"""
class WorldReader:
    
    def __init__(self):
        self.width = 0 #assumes the initial width and height are zero
        self.height = 0
        self.mapArray = [] #makes an array of map
    
    def createMapArray(self,filename):
        
        file = open(filename) #opens file
        
        self.width = int(file.readline()) #reads the width and height of the world
        self.height = int(file.readline())
        
        for y in range(self.height): #does a nested for loop
            row = [] #makes a row of maps
            for x in range(self.width):
                
                mapName = file.readline() #gets the map name
                mapName = mapName[0: len(mapName)-1]
                
                create = tilemaptextreader #creates a map using the tilemap text reader
                mapAdd = create.createMap(mapName)
                
                row.append(mapAdd) #adds that map to the row
                
            self.mapArray.append(row) #adds the row to the array
        
    def getMap(self, y, x): #retuns a map from the array
        return self.mapArray[y][x]

