# -*- coding: utf-8 -*-
#
# This file is part of Open Ant.
#
# Open Ant is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Open Ant.  If not, see <http://www.gnu.org/licenses/>.
#
# Map Class

import Globals
import os
from time import time
from Game import *
from threading import Timer
class TEMP:
    
    def __init__(self,game):
        self.g = game
        Globals.glwidget.mouseMove.connect(self.moveCamera)

        #Waiting for mouse move signal
        Globals.glwidget.mousePress.connect(self.getCoords)
        
        #Double Click?
        self.lastButton = 0
        self.lastClick = 0
        
        self.lastX = -1
        self.lastY = -1

        
    def getCoords(self, button, x, y):
        '''
        On click, move ant.
        '''
        x = (x/Globals.pixelSize)#*Globals.pixelSize
        y = (y/Globals.pixelSize)#*Globals.pixelSize
         
        if button == 1:
        
            if self.lastButton == button and time()-self.lastClick < 0.5 and x == self.lastX and y == self.lastY:   #double click
                self.g.doubleClick((x,y))
            else:
                self.g.moveAnt((x,y))
            #else:
            #    # Choose a tile that is passable and next to the tile clicked on.
            #    while not self.tiles[x/32][y/32].isPassable():
            #        if self.yellowAnt.pos[0] < x:
            #            x -= 32
            #        elif self.yellowAnt.pos[0] > x:
            #            x += 32
            #        if self.yellowAnt.pos[1] < y:
            #            y -= 32
            #        elif self.yellowAnt.pos[1] > y:
            #            y += 32
            #    self.yellowAnt.newPos = [x, y]
            #    if self.yellowAnt.moveAlongPath in self.yellowAnt.queue: #User decided to perform a different action sequence
            #        print 'remove queue'
            #        self.yellowAnt.queue.clear() #Clear queued actions
            #        self.yellowAnt.path.clear() #Clear path so ant can move to new location
            #    self.yellowAnt.queue.append(self.yellowAnt.findPath)
        self.lastX = x
        self.lastY = y
       
        self.lastButton = button
        self.lastClick = time()
        #print self.g.getYellowAnt().positionX
        #print self.g.getYellowAnt().positionY
        
    def moveCamera(self,x,y):
        try: # We try and cancel any previous camera movements.
            self.t.cancel()
        except:
            pass

        w = Globals.glwidget.w #viewport width
        h = Globals.glwidget.h #viewport height

        shiftX = 0
        shiftY = 0
        loop = False

        if x<=(0.1*w) and Globals.glwidget.camera[0] + 16 <= Globals.leftBound:
            shiftX = 16
            loop = True
        if x>=(w - 0.1*w) and Globals.glwidget.camera[0] - 16 >= Globals.rightBound +w:
            shiftX = -16
            loop = True
        if y<=(0.1*h) and Globals.glwidget.camera[1] + 16 <= Globals.upBound:
            shiftY = 16
            loop = True
        if y>=(h - 0.1*h) and Globals.glwidget.camera[1] - 16 >= Globals.downBound +h:
            shiftY = -16
            loop = True
     
 
        Globals.glwidget.camera[0] += shiftX
        Globals.glwidget.camera[1] += shiftY

        if loop == True:
            self.t = Timer(0.05, self.moveCamera, (x, y))
            self.t.start()
