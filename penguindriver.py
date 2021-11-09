# -*- coding: utf-8 -*-
import tilemaptextreader
import character
import tilemapclass
import pygame
import worldreader
import tile
import time
"""
Created on Fri Aug 27 18:33:30 2021

@author: Noah
"""
pygame.init()

posx=0 #this is the player's position
posy=0

inventory = [] #an array of items in the player's inventory and names of those items
inventorynames = []

mapx = 0 #these values hold which map the player is on
mapy = 0

time0 = time.time() #timer to track in game time

quests = 0 #number of quests completed

steps = 0 #number of steps taken

pygame.font.init() #do this to get text on the screen

myfont = pygame.font.SysFont('calibri', 15) #creates a font

world = worldreader.WorldReader() #makes a world reader

world.createMapArray('mapguide.txt') #reads the world

myscreen = pygame.display.set_mode([600,600])

currentmap = world.getMap(0, 0) #starts on the first map

myscreen = currentmap.render(myscreen) #redners the map

pygame.display.update()

pygame.display.set_caption("Penguin Game")

icon = pygame.image.load("penguindown.png")

pygame.display.set_icon(icon)

#makes the character object
penguin = character.Character('penguinleft.png','penguinright.png', 
                              'penguinup.png', 'penguindown.png')

#loads images into the game
statsbox = pygame.image.load("statsbox.png")
statsbox2 = pygame.image.load("statsbox2.png")

myscreen = penguin.render(0, 0, myscreen)

#adds text that shows the x and y map values
mapxtext = myfont.render("Map X: " + str(mapx), True, (0,0,0))
mapytext = myfont.render("Map Y: " + str(mapy), True, (0,0,0))

textboxtext = myfont.render("", True, (0,0,0))

pygame.display.update()

pygame.display.flip()

running = True

"""
The update screen method adds everything into the pygame screen.
First it renders based on the map it is on, then adds the penguin character.
Then it adds the stats boxes, and the in game text. Then it adds
the inventory icons.
"""

def updateScreen():
    global myscreen
    myscreen.fill((255,255,255))
    
    myscreen = currentmap.render(myscreen)
    myscreen = penguin.render(posx*50, posy*50, myscreen)
    
    myscreen.blit(statsbox, (500,0))
    myscreen.blit(statsbox, (500,100))
    myscreen.blit(statsbox, (500,200))
    myscreen.blit(statsbox, (500,300))
    myscreen.blit(statsbox, (500,400))
    
    myscreen.blit(statsbox2, (0,500))
    myscreen.blit(statsbox2, (0,550))
    
    
    mapxtext = myfont.render("Map X: " + str(mapx), True, (0,0,0))
    mapytext = myfont.render("Map Y: " + str(mapy), True, (0,0,0))
    myscreen.blit(mapxtext, (520,50))
    myscreen.blit(mapytext, (520,150))
    myscreen.blit(textboxtext, (100,520))
    questtext = myfont.render("Quests: " + str(quests) + "/10", True, (0,0,0))
    myscreen.blit(questtext, (510,250))
    
    
    steptext = myfont.render("Steps taken: ", True, (0,0,0))
    steptext2 = myfont.render(str(steps), True, (0,0,0))
    myscreen.blit(steptext, (510,350))
    myscreen.blit(steptext2, (540,375))
    
    
    pos = 0
    for x in inventory:
        myscreen.blit(x, (0 + 50*pos,550))
        pos+=1
    
    pygame.display.update()
    

currentmap.lencheck()

#The four methods below change the map whether you go up down left or right,
#and changes the players position to adjust the map shift

def mapChangeUp():
    global currentmap, mapx, mapy, posy
    if mapy > 0:
        currentmap = world.getMap(mapy-1, mapx)
        mapy-=1
        posy=9
        updateScreen()
                    
def mapChangeDown():
    global currentmap, mapx, mapy, posy
    if mapy+1 < world.height:
        currentmap = world.getMap(mapy+1, mapx)
        mapy+=1
        posy=0
        updateScreen()

def mapChangeLeft():
    global currentmap, mapx, mapy, posx
    if mapx > 0:
        currentmap = world.getMap(mapy, mapx-1)
        mapx-=1
        posx=9
        updateScreen()
        
def mapChangeRight():
    global currentmap, mapx, mapy, posx
    if mapx+1 < world.width:
        currentmap = world.getMap(mapy, mapx+1)
        mapx+=1
        posx=0
        updateScreen()


#this method checks if the tile is an interactive tile, if so
#then it displays the interaction text. other wise the
#interaction text is left blank
def interactiveCheck(x,y):
    global currentmap
    t = currentmap.getTile(y,x)
    if isinstance(t, tile.TalkingTile) == True:
        global textboxtext
        textboxtext = myfont.render(t.interactionText, True, (0,0,0))
        updateScreen()
    else:
        textboxtext = myfont.render("", True, (0,0,0))
        updateScreen()

#this method checks if the tile is an item tile. if so, it will take that 
#item and put it into the inventory, and signal the item tile to change

def itemCheck(x,y):
    global currentmap
    t = currentmap.getTile(y,x)
    if isinstance(t, tile.ItemTile) == True:
        if t.taken == False:
            inventory.append(t.icon)
            inventorynames.append(t.itemName)
            t.changeTiles()
        updateScreen()
    else:
        updateScreen()

#this method checks if the tile is a quest tile

def questCheck(x,y):
    global currentmap
    t = currentmap.getTile(y,x)
    
    invenLen = len(inventorynames)
    
    if isinstance(t, tile.QuestTile) == True: #if it is a quest tile
        global textboxtext
        itemNeeded = t.item #records the item needed
        itemNeeded = itemNeeded.strip()
        textboxtext = myfont.render(t.interactionText, True, (0,0,0)) #puts up
                                                                #the quest text
                                            
        counter = 0 #then it will go through the inventory
        for x in range(invenLen):
            z = inventorynames[x].strip()
            if z == itemNeeded: #if the player has the item needed
                t.updateText()
                updateScreen()
                t = inventory[counter]
                z = inventorynames[counter]
                inventorynames.remove(z) #takes out the item
                inventory.remove(t)
                global quests #increases the amount of quests finished
                quests+=1
                break;
            counter+=1
        updateScreen()
    else:
        updateScreen()

#this just calls all the checks
def tileCheck(x,y):
    interactiveCheck(x,y)
    itemCheck(x,y)
    questCheck(x,y)
 
#this method updates the time on the screen
def updateTime():
    time1 = time.time()
    global time0
    global myscreen
    myscreen.blit(statsbox, (500,400))
    
    stri = int(time1 - time0)
    stri2 = str(stri)
    
    timetext = myfont.render(stri2, True, (0,0,0))
    myscreen.blit(timetext, (540,475))
    pygame.display.update()
    
    
 
updateScreen()

while running: #this loops until the game is exited
    
    #updates the time and map x and y
    updateTime()
    mapxtext = myfont.render("Map X: " + str(mapx), True, (0,0,0)) 
    mapytext = myfont.render("Map Y: " + str(mapy), True, (0,0,0))
    
    #this checks if the player has quit and key presses
    #on key presses, does a tile check on the tile the player will move to
    #if the tile is walkable, the player will walk, and things will update
    #if needed, the map will change
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if posy<9:
                    tileCheck(posx, posy+1)
                penguin.zdown()
                if posy<9 and currentmap.walkableCheck(posy+1, posx):
                    posy+=1
                    steps+=1
                    updateScreen()
                elif posy == 9:
                    mapChangeDown()
                    steps+=1
            if event.key == pygame.K_UP:
                if posy>0:
                    tileCheck(posx, posy-1)
                penguin.zup()
                if posy>0 and currentmap.walkableCheck(posy-1, posx):
                    posy-=1
                    steps+=1
                    updateScreen()
                elif posy == 0:
                    mapChangeUp()
                    steps+=1
                    updateScreen()
            if event.key == pygame.K_LEFT:
                if posx>0:
                    tileCheck(posx-1, posy)
                penguin.zleft()
                if posx>0 and currentmap.walkableCheck(posy, posx-1):
                    posx-=1
                    steps+=1
                    updateScreen()
                elif posx == 0:
                    steps+=1
                    mapChangeLeft()
                updateScreen()
            if event.key == pygame.K_RIGHT:
                 if posx<9:
                     tileCheck(posx+1, posy)
                 penguin.zright()
                 if posx<9 and currentmap.walkableCheck(posy, posx+1):
                     posx+=1
                     steps+=1
                     updateScreen()
                 elif posx == 9:
                     mapChangeRight()
                     steps+=1
                     updateScreen()

pygame.quit()
