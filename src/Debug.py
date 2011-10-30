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
import Map
import Globals
import sys
from Enums import *
class Debug:
    def debug_printMap(self,map):
        for x in range(Globals.mapWidth):
            for y in range(Globals.mapHeight):
                if map.tiles[x][y].type == TileType.Ground: 
                    sys.stdout.write("G")
                elif map.tiles[x][y].type == TileType.Rock:
                    sys.stdout.write("R") 
                elif map.tiles[x][y].containsItem(TileType.Rock):
                    sys.stdout.write("F") 
            sys.stdout.write("\n")
            
            