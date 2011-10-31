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
from algo.astar import *
from Map import *
from Enums import *
from Coord import *
import collections
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
        
    def setPosition(self,cPos):  
        self.pos = Coord(cPos)  #cPos is interpreted as tuple here otherwise. Weird :/
        self.dst = self.pos 
        
        if self.pos.y == 0:
            self.underground = True
        
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
    
    def move(self):
        self.map.generateAStarMap(self.pos,self.dst)   #generate the AStar map for every move. Not an optimal solution if you ask me. Should be changed to a AStarMap buffer to which the start and target tiles are set for each creature. This would also make the generateAStarMap funciton cleaner
        a = AStar(self.map.AStarMap, MANHATTAN)
        q = collections.deque()
        a.step(q)
        if a.path and self.map.tiles[a.path[1][0]][a.path[1][1]].isPassable():  #Move unit
            self.pos.x = a.path[1][0]
            self.pos.y = a.path[1][1]
            
        if len(a.path) == 2 and not self.map.tiles[a.path[1][0]][a.path[1][1]].isPassable():    #if the dest tile is not passable and len(a.path)==2 then we are on the adjacent tile of the unpassable target -> movement done
            self.dst.x = self.pos.x 
            self.dst.y = self.pos.y
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            