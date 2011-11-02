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
from Team import *
from Patch import *
class Game:
    
    
    def __init__(self):
        self.patch = Patch()
        self.creatureList = []
        #actually the patch class should contain the teams
        self.teams = []
        self.teams.append(Team(Teams.Blue))
        self.teams.append(Team(Teams.Red))

        self.teams[0].addCreature(self.spawnCreature((5,5),Ants.Yellow,Teams.Blue))
        self.teams[0].playerType = PlayerType.Human

        self.teams[1].addCreature(self.spawnCreature((7,7),Ants.Yellow,Teams.Red))
        self.teams[1].playerType = PlayerType.Computer
        Globals.underground = False
        
    def getPatch(self):
        return self.patch
    
    def getCreatureList(self):
        return self.creatureList
    
   #Not used -> to be deleted ?
   # def getSpawnLocation(self):
   #     c = Coord()
   #     c.x = randint(0, 10)
   #     c.y = randint(0, 10)
   #     while not self.tiles[c.x][c.y].isPassable() and not self.tiles[c.x][c.y].isEmpty() :
   #         c.x = randint(0, 10)
   #         c.y = randint(0, 10)
   #     return c
   # 

    def update(self):
        #update existing scents
        self.patch.above.updateScents()
        self.teams[1].makeDecisions()
        for c in self.creatureList: 
            if c.map.getTileType(c.getPos()) == TileType.Nest and c.action == Actions.GoThroughNest:
                self.patch.goThroughNest(c)
            #move and perform action for each creature
            c.performAction()
            if isinstance(c,YellowAnt): 
                if c.item == Items.Food:
                    self.patch.above.refreshScentYellow(c.getPos(),Scents.Trail)
                if c.markAlarmScent == True:
                    self.patch.above.refreshScentYellow(c.getPos(),Scents.Alarm)
            else:
                #refresh or create new scents
                if c.item == Items.Food:
                    self.patch.above.refreshScent(c.getPos(),Scents.Trail)
            
    def singleClick(self,c):   
        self.teams[0].moveYellowAnt(c)
        
    def rightClick(self,c):
        pass

    def doubleClick(self,c):
        self.teams[0].doubleClick(c)

    def spawnFoodAtRandom(self):        
        c.x = randint(0, Globals.mapWidth  - 1)
        c.y = randint(0, Globals.mapHeight - 1)
        self.spawnFood(c)
    
    def spawnFood(self,c):        
        self.patch.above.putItem(c,Items.Food);

    def spawnCreature(self,coord,creature,team):
        
        if creature == Ants.Yellow:
            a = YellowAnt(team)
        else:
            a = Ant(team)
        a.map = self.patch.above
        a.setPosition(coord)
        self.creatureList.append(a)
        return a

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
