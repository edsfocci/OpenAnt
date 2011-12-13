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

from Scent import *
from Enums import *
from Coord import *
class Tile:
 
    def __init__(self, type):
        self.type = type
        self.items=[]
        self.ants =[]   #not currently used
        self.scents=[]
       
    def addItem(self,i):
        self.items.append(i)
        
    def removeItem(self):
        return self.items.pop()
        
    def isEmpty(self):
        if self.items:
            return False
        return True
        
    def containsItem(self,i):
        if self.items:
            try:
                self.items.index(i) 
                return True
            except: 
                return False
                
    def containsScent(self,type):
        if self.scents:
                for s in self.scents:
                    if s.type == type:
                        return True    
        return False
        
    def getScentStrength(self,type):
        if self.scents:
                for s in self.scents:
                    if s.type == type:
                        return s.strength
        return -1
        
    def refreshScent(self,type):
         for s in self.scents:
            if s.type == type:
                if s.strength < SCENT_INIT_STRENGTH:
                    s.setStrength(SCENT_INIT_STRENGTH)
          
    def refreshScentYellow(self,type):
         for s in self.scents:
            if s.type == type:
                if s.strength > 0:
                    s.setStrength(SCENT_MAX_STRENGTH)
                
                
    def isPassable(self):
        if self.type == TileType.Rock or self.type == TileType.Earth :
            return False;
        else:
            return True;
        
