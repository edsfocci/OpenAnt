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
from const.constants import *
from Enums import *
from random import *
from View import *
from Tile import *
from Scent import *

class Map:

    
   
    AStarMap = ""    #map of passable/not passable tiles.
    def __init__(self):
        self.tiles = []            #the actual map
        self.scentTiles = []       #List of tiles containing scent
    
    
    def generateMap(self):
    
    #1. Create tiles list
        for i in range(Globals.mapWidth):
            myList = []
            for j in range(Globals.mapHeight):
                myList.append(Tile(TileType.Void))
                myList[-1].setCoordinates(i,j)
            self.tiles.append(myList)
            
    #2. set tile type and content
        for x in range(Globals.mapWidth):
            for y in range(Globals.mapHeight):
                if randint(0,10) >= 1:
                    self.tiles[x][y].type = TileType.Ground;
                    if randint(0,10) > 9:
                        self.tiles[x][y].items.append(Items.Pebble)
                else:
                    self.tiles[x][y].type = TileType.Rock;
    #3. Put some food in there
        for i in range(50):
            x,y = self.getSpawnLocationDistribution()
            self.putItem((x,y),Items.Food)
            

             
    
    def getSpawnLocationDistribution(self, distCenter = (10, 10)):
        '''Used for food spawning''' 
        
        stdDev = 2.7

        x, y = numpy.random.normal(distCenter[0], stdDev), numpy.random.normal(distCenter[1], stdDev)
        failCount = 0
        while True:
            failCount += 1
            x, y = numpy.random.normal(distCenter[0], stdDev), numpy.random.normal(distCenter[1], stdDev)
            x, y = int(x), int(y)
            #check if number is even in map/check if passable and not occupied
            if 0 < x < Globals.mapWidth and 0 < y < Globals.mapHeight:
                if self.tiles[x][y].isPassable():
                    break
        return x, y
        
        
    #Note: Merge refreshScent functions to single function
    def refreshScentYellow(self,(x,y),type):
        if self.tiles[x][y].containsScent(type):
                self.tiles[x][y].refreshScentYellow(type)
        else:
            scent = Scent(type)
            scent.init()
            self.tiles[x][y].scents.append(scent)
            self.scentTiles.append(self.tiles[x][y])
  
    
    def refreshScent(self,(x,y),type):
        if self.tiles[x][y].containsScent(type):
            self.tiles[x][y].refreshScent(type)
        else:
            scent = Scent(type)
            scent.init()
            self.tiles[x][y].scents.append(scent)
            self.scentTiles.append(self.tiles[x][y])
  
    def updateScents(self):
        for tile in self.scentTiles:
            for scent in tile.scents:
                if scent.strength == 0:
                    #erase from tile's scent list
                    tile.scents.remove(scent)
                    if not tile.scents : #if tile's scent list empty, remove from map scentTiles list
                        self.scentTiles.remove(tile)
                else:
                    scent.update()
                if scent.type == Scents.Alarm and scent.propagateDelay % SCENT_PROPAGATE_DELAY == 0 and scent.strength > SCENT_INIT_STRENGTH:
                    x,y = self.getPos(tile)
                    #Alarm scent propagates to nearby tiles (cross propagation like on original game)
                    self.refreshScent((x+1,y),Scents.Alarm)
                    self.refreshScent((x-1,y),Scents.Alarm)
                    self.refreshScent((x,y+1),Scents.Alarm)
                    self.refreshScent((x,y-1),Scents.Alarm)

    def getPos(self,tile):
        for i,row in enumerate(self.tiles):
            try:
                tileIndex = row.index(tile)
                x = i
                y = tileIndex
                return x,y
            except: 
                pass
        Exception('Tile not found in tiles[][]')
        
    def getTiles(self):
        return self.tiles
    
    def takeItem(self,(x,y)):
        self.item = Items.Void
        if self.tiles[x][y].items:
            self.item = self.tiles[x][y].removeItem()
        return self.item
    
    def putItem(self,(x,y),item):
        if self.tiles[x][y].isEmpty():
            self.tiles[x][y].addItem(item)
            return True
        else:
            return False
    
    def getAStarMap(self):
        if self.AStarMap == "":
            self.generateAStarMap()
        return self.AStarMap
        
    def generateAStarMap(self,src,dst): 
        """Generate a string to find the paths with A star"""
        self.AStarMap = "" #clear map
        for x in range(Globals.mapWidth):
            for y in range(Globals.mapHeight):
                if (x,y) == src:
                    self.AStarMap += SOURCE
                elif (x,y) == dst:
                    self.AStarMap += TARGET
                elif self.tiles[x][y].isPassable():     
                    self.AStarMap += NORMAL
                else:
                    self.AStarMap += BLOCKED
            self.AStarMap += "\n"
            
