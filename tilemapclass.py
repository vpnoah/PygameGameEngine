# -*- coding: utf-8 -*-
import pygame
import tiledatabase
import tile

"""
Created on Thu Aug 26 22:49:59 2021

@author: Noah
"""

class Map:

    def __init__(self, tiles, intArray, width, height):
    
        self.width=width #maps have width and height
        self.height=height
        
        self.tiles = tiles #this is an array of tile data gotten 
                            #when the constructor is called
        
        ##make a 2d array with info from 
        
        self.tileArray = []
        
        self.tileWalk = [] #checks walkable status
        
        self.tileValues = [] #stores the int array
        
        #this loop takes all the ints from the intarray (ints of tiles in a map)
        #and turns them into rows. It then adds the row to the tileValues array.
        for x in range(height):
            row = []
            row.append(intArray[((x+1)*width)-width:(x+1)*width])
            self.tileValues.append(row)
            
        tda = tiledatabase.tiledatabase() #makes a tiledatabase
        tda.readTiles("tiledata.txt")
        
        
        #Below is a nested for loop. It will take the int value from
        #the int array of tiles, and get the corresponding tile by
        #calling the tile database. It then adds that tile to a row,
        #and that row is added to the 2d array of tiles
        
        for y in range(height):
             row = []
             for x in range(width):
                 val = int(intArray[x + y*width])
                 t = tda.getTile(val)
                 row.append(t)
             self.tileArray.append(row)
         
        """
        The code below makes a array of booleans, tracking whether
        each tile value is a walkable tile or not.
        """
        counter = 0
        
        for x in tiles:
            if tiles[counter].walkable == True:
                self.tileWalk.append(True)
            else:
                self.tileWalk.append(False)
            counter +=1
        
        
        """
        The code below takes a 2d array of images based on
        the tile Int values, and the tile database information
        """
        
        self.images = []
    
        for y in range(height):
            row = []
            for x in range(width):
                val = int(self.tileValues[x][0][y])
                row.append(tiles[val].img)
            self.images.append(row)


    #checks if you can walk on a certain tile
    def walkableCheck(self, y, x):
        val = int(self.tileValues[y][0][x])
        boolean = self.tileWalk[val]
        return boolean
     
    #returns a tile in the array
    def getTile(self, x, y):
        t = self.tileArray[x][y]
        return t
    
    #updates the images because tiles can change their image
    def updateImages(self):
        
        self.images = []
    
        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append(self.getTile(x,y).img)
            self.images.append(row)
    
    #takes in a screen object, and puts all the tiles into the screen.
    #it puts each image in a 50x50 box like a grid
    def render(self, screen):
        
        self.updateImages()
        
        screen.fill((255,255,255))
        
        posx=0
        posy=0 
        
        for y in self.tileValues:
            for x in y:
                for z in x:
                    
                    screen.blit(self.images[posx][posy], (posx*50, posy*50))
                
                    posx+=1
                posy+=1
                posx=0
        
        return screen
        