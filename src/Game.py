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
from Enums import *
from Map import *
from random import *
from Debug import *
from Ant import *
from YellowAnt import *
from Coord import *
class Game:
    
    
    def __init__(self):
        self.map = Map()
        self.map.generateMap()
        self.creatureList = []
        self.spawnAnt((5,5,0),Ants.Yellow)
        self.d = Debug()
        Globals.underground = False
        #self.d.enterNest()
        
        
    def getMap(self):
        return self.map
    
    def getCreatureList(self):
        return self.creatureList
    
    def getSpawnLocation(self):
        c = Coord()
        c.x = randint(0, 10)
        c.y = randint(0, 10)
        c.z = 0
        while not self.tiles[c.x][c.y].isPassable() and not self.tiles[c.x][c.y].isEmpty() :
            c.x = randint(0, 10)
            c.y = randint(0, 10)
        return c
    
    def getYellowAnt(self):
        for a in self.creatureList:
            if  isinstance(a,YellowAnt):
                return a
        return -1
        
    def update(self):
        #update existing scents
        self.map.updateScents()
        for c in self.creatureList: 
            #move and perform action for each creature
            c.performAction()
            if isinstance(c,YellowAnt): 
                if c.item == Items.Food:
                    self.map.refreshScentYellow(c.getPos(),Scents.Trail)
                if c.markAlarmScent == True:
                    self.map.refreshScentYellow(c.getPos(),Scents.Alarm)
            else:
                #refresh or create new scents
                if c.item == Items.Food:
                    self.map.refreshScent(c.getPos(),Scents.Trail)
            
    def singleClick(self,c):   
        self.moveAnt(c)
        
    def rightClick(self,c):
        if self.getYellowAnt().pos.z == 1:
            self.getYellowAnt().setAction(c,Actions.BuildNest)
        
    def doubleClick(self,c):
        if self.getYellowAnt().underground:
            self.getYellowAnt().setAction(c,Actions.DigThrough)
        elif  self.map.tiles[c.x][c.y].isEmpty():   #could be changed to interface function map.isTileEmpty((x,y))
            self.getYellowAnt().setAction(c,Actions.DropItem)
        else:
            self.getYellowAnt().setAction(c,Actions.GrabItem)
            
    def spawnFoodAtRandom(self):        
        c.x = randint(0, Globals.mapWidth  - 1)
        c.y = randint(0, Globals.mapHeight - 1)
        c.z = 0
        self.spawnFood(c)
    
    def setAction(self,c,action):
        self.getYellowAnt().setAction(c,action)
        
    def moveAnt(self,c):
        self.getYellowAnt().setAction(c,Actions.Move)   
        
    def spawnFood(self,c):        
        self.map.putItem(c,Items.Food);

    def spawnAnt(self,c,antType):
        if antType == Ants.Yellow:
            a = YellowAnt()
        else:
            a = Ant()
        a.map = self.map
        a.setPosition(c)
        self.creatureList.append(a)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
