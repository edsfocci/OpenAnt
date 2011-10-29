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

import Globals
from algo.astar import *
from Map import *
from Enums import *
import collections
class Creature():
        
    hp = 100
    positionX = 0
    positionY = 0      
    destinationX = 0
    destinationY = 0
    action  = Actions.Idle
    item    = Items.Void
    map     = Map() #find a better way to link each creatures to the game map
    def __init__(self):
        pass
        
#I'd prefer to give those at instanciation and forbid changing it directly afterwards. 
#TODO: check if there's a way to have multiple arguments in the constructor
    def setPosition(self,(x,y)):  
        self.positionX = x 
        self.positionY = y 
        self.destinationX = x
        self.destinationY = y
    
    def pos(self):
        return self.positionX,self.positionY

    def setAction(self,(x,y),action):
        self.action = action
        self.setDestination((x,y))

    def performAction(self):
        if (self.positionX,self.positionY) != (self.destinationX,self.destinationY):
            self.move()
        else:
            pass
            
    def setDestination(self,(x,y)):
        self.destinationX = x
        self.destinationY = y
    
    def move(self):
        self.map.generateAStarMap((self.positionX,self.positionY),(self.destinationX,self.destinationY))   #generate the AStar map for every move. Not an optimal solution if you ask me. Should be changed to a AStarMap buffer to which the start and target tiles are set for each creature. This would also make the generateAStarMap funciton cleaner
        a = AStar(self.map.AStarMap, MANHATTAN)
        q = collections.deque()
        a.step(q)
        if a.path and self.map.tiles[a.path[1][1]][a.path[1][0]].isPassable():
            self.positionX = a.path[1][1]
            self.positionY = a.path[1][0]