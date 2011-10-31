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

from Creature import *
from algo.astar import *
import collections
class Ant(Creature):
    def __init__(self):
        pass
    
    def performAction(self):
            if self.action == Actions.Move:
                if self.map.getTileType(self.getPos()) == TileType.Nest:
                    self.goThroughNest()
                else:
                    self.move()
                    return
            elif self.action == Actions.GrabItem:    
                self.grabItem()
                if(self.hp<30):
                    self.eat()
            elif self.action == Actions.DropItem:
                self.dropItem()
            elif self.action == Actions.Eat:
                self.eat()
            elif self.action == Actions.Dig:
                self.dig()
                return
                
            self.action = Actions.Idle
    def dig(self):
        pass
        
    def grabItem(self):
        self.action = Actions.Idle
        if self.item == Items.Void:
            self.item = self.map.takeItem(self.getPos())
            
    def dropItem(self):
        self.action = Actions.Idle
        if self.item != Items.Void:
           self.map.putItem(self.getPos(),self.item)
           self.item = Items.Void
        
    def eat(self):
        if(self.item == Items.Food):
            self.item = Items.Void
            self.hp = 100
            
    def goThroughNest(self):
        self.map.goThroughNest(self)
        self.dest = self.pos 
    
    def move(self):
        pass
        
 