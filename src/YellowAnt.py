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
   
    markAlarmScent = False
   
    #def __init__(self):
    #    pass
        
    def dig(self):
        if(abs(self.dst.y - self.pos.y)>abs((self.dst.x - self.pos.x))):
            if (self.dst.y - self.pos.y) < 0:
                    self.pos.y-=1
            elif (self.dst.y - self.pos.y) > 0:
                    self.pos.y+=1
        else:
            if (self.dst.x - self.pos.x) < 0:
                self.pos.x-=1
            elif (self.dst.x - self.pos.x) > 0:
                self.pos.x+=1
        self.map.digTile(self.getPos())
        
    def move(self):
        if self.pos == self.dst:
            if self.map.getTileType(self.pos)==TileType.Nest:
                self.action = Actions.GoThroughNest
            else:
                self.action = Actions.Idle
            return
        if self.isUnderground() and self.action == Actions.Dig:
            self.dig()
        else:         
            self.map.generateAStarMap(self.getPos(),self.getDst())  
            a = AStar(self.map.AStarMap, MANHATTAN)
            q = collections.deque()
            
            a.step(q)
            if a.path:
                nextX = a.path[1][0]
                nextY = a.path[1][1]
                if self.map.tiles[nextX][nextY].isPassable():  
                    self.pos.x = nextX
                    self.pos.y = nextY
