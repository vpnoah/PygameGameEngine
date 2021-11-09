# -*- coding: utf-8 -*-
import pygame

"""
Created on Fri Aug 27 16:37:33 2021

@author: Noah
"""
pygame.init()

"""
The character class has a left, right, up, and down image. As well 
as the image being chosen. The render method puts up the image
accoring the the imageNum value
"""

class Character:
    def __init__(self, left, right, up, down):
             self.left = left
             self.right = right
             self.up = up
             self.down=down
             
             self.imageNum = 1 #1-l, 2-r, 3-u, 4-d

             self.leftimg = pygame.image.load(left)
             self.rightimg = pygame.image.load(right)
             self.upimg = pygame.image.load(up)
             self.downimg = pygame.image.load(down)
             
    def zleft(self):
             self.imageNum=1
    def zright(self):
             self.imageNum=2
    def zup(self):
            self.imageNum=3
    def zdown(self):
            self.imageNum=4
    def render(self, x, y, screen):
        if self.imageNum == 1:
            screen.blit(self.leftimg, (x,y))
        if self.imageNum == 2:
            screen.blit(self.rightimg, (x,y))
        if self.imageNum == 3:
            screen.blit(self.upimg, (x,y))
        if self.imageNum == 4:
            screen.blit(self.downimg, (x,y))
        return screen
        