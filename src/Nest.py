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
from Coord import *
from Tile import *
class Nest(Tile):

    #This class serves as inside and outside nest, it's no use creating 2 classes for each case
    def init(self,underground= None):
        self.underground = underground
        self.outside = Coord((0,0)) #coordinate of the nest entrance if tile is nest
        self.inside  = Coord((0,0)) #coordinate of the nest exit if tile is nest
   
       


