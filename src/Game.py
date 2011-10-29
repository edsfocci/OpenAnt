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

#
# convenience class
#
# By Oipo (kingoipo@gmail.com)
           
import Globals
from Enums import *
from Map import *
from random import *
from Debug import *
from Ant import *
from YellowAnt import *
class Game:
    
    
    def __init__(self):
        self.map = Map()
        self.creatureList = []
        self.map.generateMap()
        self.spawnAnt((5,5),Ants.Yellow)
        self.d = Debug()
        
        
    def getMap(self):
        return self.map
    
    def getCreatureList(self):
        return self.creatureList
    
    def getSpawnLocation(self):
        x = randint(0, 10)
        y = randint(0, 10)
        while not self.tiles[x][y].isPassable() :
            x = randint(0, 10)
            y = randint(0, 10)
        return x, y
    
    def getYellowAnt(self):
        for a in self.creatureList:
            if  isinstance(a,YellowAnt):
                return a
        return -1
        
    def update(self):
        #self.d.debug_printMap(self.map)
        for c in self.creatureList:
            c.performAction()
        
    def doubleClick(self,(x,y)):
        if  self.map.tiles[x][y].isEmpty():   #could be changed to interface function map.isTileEmpty((x,y))
            self.getYellowAnt().setAction((x,y),Actions.DropItem)
        else:
            self.getYellowAnt().setAction((x,y),Actions.GrabItem)
            
    def spawnFoodAtRandom(self):        
        x = randint(0, Globals.mapWidth  - 1)
        y = randint(0, Globals.mapHeight - 1)
        self.spawnFood(x,y)
    
    def setAction(self,(x,y),action):
        self.getYellowAnt().setAction((x,y),action)
        
    def moveAnt(self,(x,y)):
        self.getYellowAnt().setAction((x,y),Actions.Move)
    
    def spawnFood(self,(x,y)):        
        self.map.putItem(x,y,Items.Food);

    def spawnAnt(self,(x,y),antType):
        if antType == Ants.Yellow:
            a = YellowAnt()
        else:
            a = Ant()
        a.map = self.map
        a.setPosition((x,y))
        self.creatureList.append(a)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
