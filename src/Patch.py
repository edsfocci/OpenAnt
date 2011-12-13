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

import Globals
from const.constants import *
from Enums import *
from Underground import *
from Aboveground import *
from Coord import *
from Nest import  *

class Patch():
    def __init__(self):
        self.above = Aboveground()
        self.unders= []
        self.unders.append(Underground(self.above))
        self.unders.append(Underground(self.above))
        self.generateInitialNest()
    
    def generateInitialNest(self):
        self.buildNest(Coord((Globals.mapWidth/2,0)),self.unders[0])
        self.buildNest(Coord((Globals.mapWidth/2,0)),self.unders[1])
    

    def buildNest(self,coord,underground):
        while True:
            cExit = Coord((randint(0,Globals.mapWidth-1),randint(0,Globals.mapHeight-1)))
            if self.above.tiles[cExit .x][cExit .y].type != TileType.Nest:
                break

        self.above.tiles[cExit.x][cExit.y] = Nest(TileType.Nest)
        self.above.tiles[cExit.x][cExit.y].init(underground)
        self.above.tiles[cExit.x][cExit.y].inside.set(coord)
        
        underground.tiles[coord.x][coord.y] = Nest(TileType.Nest)
        underground.tiles[coord.x][coord.y].init()
        underground.tiles[coord.x][coord.y].outside.set(cExit)
    def goThroughNest(self,ant):
        if ant.isUnderground():
            ant.pos = ant.map.getTileAt(ant.pos).outside
            ant.map = self.above
        else:
            ant.map = ant.map.getTileAt(ant.pos).underground
            ant.pos = self.above.getTileAt(ant.pos).inside
