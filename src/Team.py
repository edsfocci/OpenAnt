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
from Coord import *
from YellowAnt import *
class Team():
    
    playerType = -1
    def __init__(self,team):
        self.AIdest = Coord((0,0))
        self.unitList = []
        self.color = team  #color is an value from enum.Teams
    
    def makeDecisions(self): #ai main loop
        if self.getYellowAnt().action == Actions.Idle:
            self.AIdest = Coord((randint(0,32)-1,randint(0,32)-1))
            self.moveYellowAnt(self.AIdest )

    def getYellowAnt(self):
        for a in self.unitList:
            if  isinstance(a,YellowAnt):
                return a
        return -1
        
    def addCreature(self,creature):
        self.unitList.append(creature)

    def moveYellowAnt(self,c):
        self.getYellowAnt().setAction(c,Actions.Move)   
        
    def setAction(self,c,action):
        self.getYellowAnt().setAction(c,action)
    
    def doubleClick(self,c):
        if self.getYellowAnt().isUnderground():
            self.getYellowAnt().setAction(c,Actions.Dig)
        elif  self.getYellowAnt().map.tiles[c.x][c.y].isEmpty():   #could be changed to interface function map.isTileEmpty((x,y))
            self.getYellowAnt().setAction(c,Actions.DropItem)
        else:
            self.getYellowAnt().setAction(c,Actions.GrabItem)
   