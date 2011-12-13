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

from Coord import *
import Globals
import numpy
from Enums import *
from Underground import *
class View():
    def __init__(self, mapSlice):
       self.map = mapSlice
       self.drawMap()

    def updateMapReference(self,map):
        
        self.map = map

    def updateVisuals(self, unitList):
        self.clearMap()
        self.drawMap()
        image = Globals.dataDir + 'images/ants/' + 'yellowant.png'
        if isinstance(map,Underground):
            for unit in unitList:
                if unit.map == self.map :
                    Globals.glwidget.createImage(image , 2,[0, 32, 32, 32], [unit.getPos().y*Globals.pixelSize, (unit.getPos().z - 1)*Globals.pixelSize, 32, 32])
        else:
            for unit in unitList:
                if unit.map == self.map :
                    Globals.glwidget.createImage(image , 2,[0, 32, 32, 32], [unit.getPos().x*Globals.pixelSize, unit.getPos().y*Globals.pixelSize, 32, 32])
    def drawMap(self):

        self.width = len(self.map.tiles)
        self.height= len(self.map.tiles[0])


        #self.width = Globals.mapWidth
        #self.height= Globals.mapHeight
        Globals.glwidget.reserveVBOSize(self.width*self.height)
        if isinstance(self.map,Underground):
            for x in range(Globals.undergroundWidth):
                for y in range(Globals.undergroundHeight):
                    if self.map.tiles[x][y].type == TileType.Earth:
                        image =  Globals.dataDir + 'images/underground/underground1.png'
                        Globals.glwidget.createImage(image, 0, [1, 1, -1, -1], [x*Globals.pixelSize, y*Globals.pixelSize, -1, -1], False)
                    elif self.map.tiles[x][y].type == TileType.Empty:
                        image =  Globals.dataDir + 'images/underground/underground2.png'
                        Globals.glwidget.createImage(image, 0, [1, 1, -1, -1], [x*Globals.pixelSize, y*Globals.pixelSize, -1, -1], False)

        else:
            for x in range(self.width):
                for y in range(self.height):
                    if self.map.tiles[x][y].type == TileType.Ground:
                        image =  Globals.dataDir + 'images/ground/ground1.png'
                    elif self.map.tiles[x][y].type == TileType.Rock:
                        image =  Globals.dataDir + 'images/foliage/rock1.png'
                    elif self.map.tiles[x][y].type == TileType.Nest:
                        image =  Globals.dataDir + 'images/special/nest.png'
                    Globals.glwidget.createImage(image, 0, [1, 1, -1, -1], [x*Globals.pixelSize, y*Globals.pixelSize, -1, -1], False)

            for x in range(self.width):
                for y in range(self.height):
                    if self.map.tiles[x][y].containsScent(Scents.Trail):
                        s = self.map.tiles[x][y].getScentStrength(Scents.Trail)
                        Globals.glwidget.addText( str(s) ,(x*Globals.mapWidth,y*Globals.mapHeight))

                    if self.map.tiles[x][y].containsScent(Scents.Alarm):
                        s = self.map.tiles[x][y].getScentStrength(Scents.Alarm)
                        Globals.glwidget.addText( str(s) ,(x*Globals.mapWidth,y*Globals.mapHeight+Globals.pixelSize/2))

                    if self.map.tiles[x][y].containsItem(Items.Pebble):
                        image =  Globals.dataDir + 'images/foliage/foliage1.png'
                        Globals.glwidget.createImage(image, 0, [1, 1, -1, -1], [x*Globals.pixelSize, y*Globals.pixelSize, -1, -1], False)

                    if self.map.tiles[x][y].containsItem(Items.Food):
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
