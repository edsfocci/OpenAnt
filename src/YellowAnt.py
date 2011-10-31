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
from Ant import *
from Creature import *

class YellowAnt(Ant,Creature):
    def __init__(self):
        self.markAlarmScent = False
        pass
        
    def dig(self):
        if(abs(self.dst.z - self.pos.z)>abs((self.dst.y - self.pos.y))):
            if (self.dst.z - self.pos.z) < 0:
                    self.pos.z-=1
            elif (self.dst.z - self.pos.z) > 0:
                    self.pos.z+=1
        else:
            if (self.dst.y - self.pos.y) < 0:
                self.pos.y-=1
            elif (self.dst.y - self.pos.y) > 0:
                self.pos.y+=1
        self.map.digTile(self.getPos())
        
    def move(self):
        if self.pos == self.dst:
            self.action = Actions.Idle
            return
        if self.pos.z>0 and self.action == Actions.Dig:
            self.dig()
        else:         
            self.map.generateAStarMap(self.getPos(),self.getDest())  
            a = AStar(self.map.AStarMap, MANHATTAN)
            q = collections.deque()
            
            a.step(q)
            if a.path:
                print a.path
                nextX = a.path[1][0]
                nextY = a.path[1][1]
                if self.isUnderground()  :
                    if self.map.blueUnderground[nextX][nextY-1].isPassable():
                        self.pos.y = nextX
                        self.pos.z = nextY
                else:
                    if self.map.tiles[nextX][nextY].isPassable():  
                        self.pos.x = nextX
                        self.pos.y = nextY
                    
            
    def goThroughNest(self):
        self.map.goThroughNest(self)
        self.dst = self.pos
        if self.pos.z == 0:
            Globals.underground = False
        else:
            Globals.underground = True