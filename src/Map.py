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
from Tile import *
from Scent import *
from Coord import *
import numpy
class Map():

    
   
    AStarMap = ""    #map of passable/not passable tiles.
    def __init__(self):
        self.tiles=[]

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
        c = Coord((x,y))
        return c
        
        
    #Note: Merge refreshScent functions to single function
    def refreshScentYellow(self,c,type):
        if self.tiles[c.x][c.y].containsScent(type):
                self.tiles[c.x][c.y].refreshScentYellow(type)
        else:
            scent = Scent(type)
            scent.init()
            self.tiles[c.x][c.y].scents.append(scent)
            self.scentTiles.append(self.tiles[c.x][c.y])
  
    
    def refreshScent(self,(x,y),type):
        if self.tiles[x][y].containsScent(type):
            self.tiles[x][y].refreshScent(type)
        else:
            scent = Scent(type)
            scent.init()
            self.tiles[x][y].scents.append(scent)
            self.scentTiles.append(self.tiles[x][y])

    #TODO: disable scents underground
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
                    c = self.getPos(tile)
                    self.propagateScent(c,Scents.Alarm)
                    
    def propagateScent(self,c,type):
        #cross propagation like in original game
        if c.x+1<Globals.mapWidth:
            self.refreshScent((c.x+1,c.y),Scents.Alarm)
        if c.x-1>=0:   
            self.refreshScent((c.x-1,c.y),Scents.Alarm)
        if c.y+1<Globals.mapHeight:
            self.refreshScent((c.x,c.y+1),Scents.Alarm)
        if c.y-1>=0:
            self.refreshScent((c.x,c.y-1),Scents.Alarm)
            
    def getTileAt(self,coord):
        return self.tiles[coord.x][coord.y]
    def getPos(self,tile):
    #iterating through each tile may be quicker because it doesnt raise exceptions
        c = Coord((0,0,0))
        for i,row in enumerate(self.tiles):
            try:
                tileIndex = row.index(tile)
                c = self.tiles[tileIndex]
                #c.y = tileIndex
                #c.z = 
                return c
            except: 
                pass
        Exception('Tile not found in tiles[][]')
 
           

    def getTileType(self,c):
            return self.tiles[c.x][c.y].type
        
     
        
    def takeItem(self,c):
        self.item = Items.Void
        if self.tiles[c.x][c.y].items:
            self.item = self.tiles[c.x][c.y].removeItem()
        return self.item
    
    def putItem(self,c,item):
        if self.tiles[c.x][c.y].isEmpty():
            self.tiles[c.x][c.y].addItem(item)
            return True
        else:
            return False

    def getAStarMap(self):
        if self.AStarMap == "":
            self.generateAStarMap()
        return self.AStarMap
        
    def generateAStarMap(self,cSrc,cDst):
        AStarTiles = [] #reference to chunk of map that must be processed
        self.AStarMap = "" #clear map

        AStarTiles = self.tiles
        width  = Globals.mapWidth
        height = Globals.mapHeight
        start = cSrc.x,cSrc.y
        dest  = cDst.x ,cDst.y
        
        for y in range(height):
            for x in range(width):
                if (x,y) == start:
                    self.AStarMap += SOURCE
                elif (x,y) == dest:
                    self.AStarMap += TARGET
                elif AStarTiles[x][y].isPassable():     
                    self.AStarMap += NORMAL
                else:
                    self.AStarMap += BLOCKED
            self.AStarMap += "\n"
            #print self.AStarMap 
            
            
            
            