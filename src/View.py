# -*- coding: utf-8 -*-
#
# This file is part of Open Ant.
#
# Open Ant is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Open Ant is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Open Ant.  If not, see <http://www.gnu.org/licenses/>.

import Globals
import numpy
from Enums import *

class View():
    def __init__(self, mapSlice):
       self.map = mapSlice
       self.drawMap()
       
    def updateVisuals(self, unitList):
        self.clearMap()
        self.drawMap()
        for unit in unitList:
            image = Globals.dataDir + 'images/ants/' + 'yellowant.png'
            Globals.glwidget.createImage(image , 2,[0, 32, 32, 32], [unit.positionX*Globals.pixelSize, unit.positionY*Globals.pixelSize, 32, 32])
        
    def drawMap(self):
        self.tiles = self.map 
        self.width = len(self.tiles)
        self.height= len(self.tiles[0])

        Globals.glwidget.reserveVBOSize(self.width*self.height)

 
        for x in range(self.width):
            for y in range(self.height):
                if self.tiles[x][y].type == TileType.Ground:
                    image =  Globals.dataDir + 'images/ground/ground1.png'
                elif self.tiles[x][y].type == TileType.Rock:
                    image =  Globals.dataDir + 'images/foliage/rock1.png'
                Globals.glwidget.createImage(image, 0, [1, 1, -1, -1], [x*Globals.pixelSize, y*Globals.pixelSize, -1, -1], False)
                
        for x in range(self.width):
            for y in range(self.height):              
                if self.tiles[x][y].containsScent(Scents.Trail):
                    s = self.tiles[x][y].getScentStrength(Scents.Trail) 
                    Globals.glwidget.addText( str(s) ,(x*Globals.mapWidth,y*Globals.mapHeight))           
                    
                if self.tiles[x][y].containsScent(Scents.Alarm):
                    s = self.tiles[x][y].getScentStrength(Scents.Alarm) 
                    Globals.glwidget.addText( str(s) ,(x*Globals.mapWidth,y*Globals.mapHeight+Globals.pixelSize/2))
                    
                if self.tiles[x][y].containsItem(Items.Pebble):
                    image =  Globals.dataDir + 'images/foliage/foliage1.png'
                    Globals.glwidget.createImage(image, 0, [1, 1, -1, -1], [x*Globals.pixelSize, y*Globals.pixelSize, -1, -1], False)
                    
                if self.tiles[x][y].containsItem(Items.Food):
                    image =  Globals.dataDir + 'images/food/food.png'
                    Globals.glwidget.createImage(image, 0, [1, 1, -1, -1], [x*Globals.pixelSize, y*Globals.pixelSize, -1, -1], False)
                
                
    
   
    def clearMap(self):
        Globals.glwidget.deleteAllImages()
        Globals.glwidget.deleteAllText()
        


    def ground(self, x=0, y=0):
        Globals.leftBound = 0
        Globals.rightBound = -1 * Globals.mapwidth * Globals.pixelSize
        Globals.upBound = 0
        Globals.downBound = -1 * (Globals.mapheight/2) * Globals.pixelSize
        Globals.glwidget.camera[0] = x
        Globals.glwidget.camera[1] = y       

    def blackNest(self, x=Globals.blackNestX, y=Globals.blackNestY):
        Globals.leftBound = 0
        Globals.rightBound = Globals.redNestX
        Globals.upBound = Globals.blackNestY
        Globals.downBound = -1 * Globals.mapheight * Globals.pixelSize
        Globals.glwidget.camera[0] = x
        Globals.glwidget.camera[1] = y
        
    def redNest(self, x=Globals.redNestX,y=Globals.redNestY):
        Globals.leftBound = Globals.redNestY
        Globals.rightBound = -1 * Globals.mapwidth * Globals.pixelSize
        Globals.upBound = Globals.redNestY
        Globals.downBound = -1 * Globals.mapheight * Globals.pixelSize
        Globals.glwidget.camera[0] = x
        Globals.glwidget.camera[1] = y
