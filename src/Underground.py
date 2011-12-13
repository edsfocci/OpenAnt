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
from Map import *
from Nest import *
class Underground(Map):
    
    def __init__(self,above):
        self.tiles = []
        self.aboveground = above
        self.generate()

    def digTile(self,c):
        if self.tiles[c.x][c.y].type == TileType.Earth:
            if c.y == 0:
                pass
                self.buildNest(c)
            else:
                self.tiles[c.x][c.y].type = TileType.Empty


    def generate(self):
        # Generate underground
        #1. Create tiles list
        for i in range(Globals.undergroundWidth):
            myList = []
            for j in range(Globals.undergroundHeight):
                myList.append(Tile(TileType.Void))
            self.tiles.append(myList)
            
        #2. set tile type and content
        for x in range(Globals.mapWidth):
            for y in range(Globals.mapHeight):
                self.tiles[x][y].type = TileType.Earth;
