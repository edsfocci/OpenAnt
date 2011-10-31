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

#DEBUG

import Globals
from Map import *
from Enums import *
from Coord import *
class Creature():
        
    hp = 100
    pos = Coord((0,0,0))
    dst = Coord((0,0,0))
    underground = False
    action  = Actions.Idle
    item    = Items.Void
    map     = Map() #find a better way to link each creatures to the game map
    def __init__(self):
        pass
    
    def isUnderground(self):
        return self.pos.z > 0
        
    def setPosition(self,cPos):  
        self.pos = Coord(cPos)  #cPos is interpreted as tuple here otherwise. Weird :/
        
    def getPos(self):
        return self.pos
    
    def getDest(self):
        return self.dst

    def setAction(self,cDst,action):
        self.action = action
        self.dst = cDst

    def performAction(self):
        if (self.pos) != (self.dst):
            self.move()
        else:
            pass
            
    def setDestination(self,cDst):
        self.dst = cDst
    
    def move(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")
    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            