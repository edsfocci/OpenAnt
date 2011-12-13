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

class Aboveground(Map):
    def __init__(self):
        self.tiles = []            #the actual map
        self.scentTiles = []       #List of tiles containing scent
        self.generate()

    def generate(self):
    
    #1. Create tiles list
        for i in range(Globals.mapWidth):
            myList = []
            for j in range(Globals.mapHeight):
                myList.append(Tile(TileType.Void))
            self.tiles.append(myList)
            
    #2. set tile type and content
        for x in range(Globals.mapWidth):
            for y in range(Globals.mapHeight):
                if randint(0,10) >= 1:
                    self.tiles[x][y].type = TileType.Ground;
                    if randint(0,10) > 9:
                        self.tiles[x][y].items.append(Items.Pebble)
                else:
                    self.tiles[x][y].type = TileType.Rock;
                    
    #3. Put some food in there
        for i in range(50):
            c = self.getSpawnLocationDistribution()
            self.putItem(c,Items.Food)