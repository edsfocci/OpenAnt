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
from Underground import *
from Coord import *
class Map:

    
   
    AStarMap = ""    #map of passable/not passable tiles.
    def __init__(self):
        self.tiles = []            #the actual map
        self.scentTiles = []       #List of tiles containing scent
        self.blueUnderground = []
        
        
    def generateMap(self):
    
    #1. Create tiles list
        for i in range(Globals.mapWidth):
            myList = []
            for j in range(Globals.mapHeight):
                myList.append(Tile(TileType.Void))
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
            c = self.getSpawnLocationDistribution()
            self.putItem(c,Items.Food)
    #3. Generate underground
        #1. Create tiles list
        for i in range(Globals.undergroundWidth):
            myList = []
            for j in range(Globals.undergroundHeight):
                myList.append(Tile(TileType.Void))
            self.blueUnderground.append(myList)
            
        #2. set tile type and content
        for y in range(Globals.mapWidth):
            for z in range(Globals.mapHeight):
                self.blueUnderground[y][z].type = TileType.Earth;

        
    #4. Put nest main entrance at random point
        
        cOut = Coord((randint(0,Globals.mapWidth),randint(0,Globals.mapHeight),0))
        cIn  = Coord((0,randint(0,Globals.undergroundWidth - 1),0))
        
        del self.tiles[cOut.x][cOut.y].items[:]
        self.tiles[cOut.x][cOut.y].type = TileType.Nest
        self.tiles[cOut.x][cOut.y].inside  = cIn    
        
        self.blueUnderground[cIn.y][cIn.z].outside = cOut
        self.blueUnderground[cIn.y][cIn.z].type  = TileType.Nest
        self.blueUnderground[cIn.y][cIn.z+1].type  = TileType.Empty 
        
    
    def goThroughNest(self,ant):
        if ant.pos.z != 0:
            tile = self.blueUnderground[ant.pos.y][ant.pos.z-1]
            ant.pos = tile.outside
            ant.underground = False
        else:
            tile = self.tiles[ant.pos.x][ant.pos.y]
            ant.underground = True
            ant.pos = tile.inside
            ant.pos.z = 1
            
            
    def buildNest(self,c):
            ug = self.blueUnderground
            while True:
                cNestExit = Coord((randint(0,Globals.mapWidth-1),randint(0,Globals.mapHeight-1),0))
                if self.tiles[cNestExit.x][cNestExit.y].type != TileType.Nest:
                    break
            
            ug[c.y][c.z-1].type = TileType.Nest #indoor nest
            ug[c.y][c.z-1].outside = cNestExit
            
            del self.tiles[cNestExit.x][cNestExit.y].items[:]
            self.tiles[cNestExit.x][cNestExit.y].type = TileType.Nest #indoor nest
            self.tiles[cNestExit.x][cNestExit.y].inside = c
            
            
    def digTile(self,c):
        if self.blueUnderground[c.y][c.z-1].type == TileType.Earth:
            if c.z == 1:
                self.buildNest(c)
            else:
                self.blueUnderground[c.y][c.z-1].type = TileType.Empty
        
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
        c = Coord((x,y,0))
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
            
    
    def getPos(self,tile):
    #iterating through each tile may be quicker because it doesnt raise exceptions
        c = Coord((0,0,0))
        for i,row in enumerate(self.tiles):
            try:
                tileIndex = row.index(tile)
                c.x = i
                c.y = tileIndex
                c.z = 0
                return c
            except: 
                pass
        Exception('Tile not found in tiles[][]')
        
    def getTiles(self):
        return self.tiles
    
    def getTile(self,c):
        if c.z!=0 :
            return self.blueUnderground[c.y][c.z-1]
        else:
            return self.tiles[c.x][c.y]
    def getTileType(self,c):
        if c.z != 0:
            return self.blueUnderground[c.y][c.z-1].type
        else:
            return self.tiles[c.x][c.y].type
        
     
        
    def takeItem(self,c):
        self.item = Items.Void
        if c.z == 0:
            if self.tiles[c.x][c.y].items:
                self.item = self.tiles[c.x][c.y].removeItem()
        else:
            if self.undergrounds[c.x].tiles[c.y][c.z-1].items:
                self.item = self.undergrounds[c.x].tiles[c.x][c.y].removeItem()
        return self.item
    
    def putItem(self,c,item):
        if c.z == 0:
            if self.tiles[c.x][c.y].isEmpty():
                self.tiles[c.x][c.y].addItem(item)
                return True
            else:
                return False
        else:
            if self.undergrounds[c.x].tiles[c.y][c.z-1].isEmpty():
                self.undergrounds[c.x].tiles[c.y][c.z-1].addItem(item)
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
        if cSrc.z != 0: #underground
            AStarTiles = self.blueUnderground
            width  = Globals.undergroundWidth
            height = Globals.undergroundHeight
            start = cSrc.y ,cSrc.z-1 
            dest  = cDst.y ,cDst.z-1 
            for x in range(width):      #when underground,m 1 line of blocked tiles is added to avoid problems, as row 0 of underground tiles have index 0 in the list but coordinate Z = 1
                self.AStarMap+=BLOCKED
            self.AStarMap += "\n"
        else:
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
            
            
            
            