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
# Ant class
from Creature import *

class Ant(Creature):
    def __init__(self):
        pass
    
    def performAction(self):
        if (self.positionX,self.positionY) != (self.destinationX,self.destinationY):
            self.move()
        else:
            if self.action == Actions.GrabItem:
                self.grabItem()
            elif self.action == Actions.DropItem:
                self.dropItem()
            self.action = Actions.Idle
    
    def grabItem(self):
        self.action = Actions.Idle
        if self.item == Items.Void:
            self.item = self.map.takeItem(self.pos())
            
    def dropItem(self):
        print self.item
        self.action = Actions.Idle
        if self.item != Items.Void:
           self.map.putItem(self.pos(),self.item)
           self.item = Items.Void
        print self.item
            
        
 