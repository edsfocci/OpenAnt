# -*- coding: utf-8 -*-
#
# This file is part of Open Ant.
#
# Open Ant is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Open Ant.  If not, see <http://www.gnu.org/licenses/>.
#
# Map Class

from Enums import *
class Tile:
 
    def __init__(self, type):
        self.type = type
        self.items=[]
        self.ants =[]
    
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
            try:#if the index() raises a exception, then the item isn't in the list
                self.items.index(i) 
                return True
            except: 
                return False

    def isPassable(self):
        if self.type == TileType.Rock or self.containsItem(Items.Peeble):
            return False;
        else:
            return True;
        
