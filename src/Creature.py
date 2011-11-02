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
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PUR__posE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Open Ant.  If not, see <http://www.gnu.org/licenses/>.

#DEBUG

import Globals
from Map import *
from Enums import *
from Coord import *
from Underground import *
class Creature():
        

    def __init__(self,team):
        self.pos = Coord((0,0))
        self.team = team
        self.hp = 100
        self.dst = Coord((0,0))
        self.underground = False
        self.action  = Actions.Idle
        self.item    = Items.Void
        self.map     = None #find a better way to link each creatures to the game map
        pass
    
    def isUnderground(self):
        return isinstance(self.map, Underground)
        
    def setPosition(self,cPos):  
        self.pos.set(Coord(cPos))

    def getPos(self):
        return self.pos
    
    def getDst(self):
        return self.dst

    def setAction(self,cDst,action):
        self.action = action
        self.dst.set(cDst)

    def performAction(self):
        if self.pos != self.dst:
            self.move()
        else:
            pass
            
    def setDestination(self,cDst):
        self.dst.set(cDst)
    
    def move(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")
    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            