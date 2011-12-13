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

class Coord(object):

    def __init__(self,(x,y)):
        self.x = x
        self.y = y

    def set(self,cVal):
        self.x = cVal.x
        self.y = cVal.y

    def rand(self):
        self.x = randint(0,mapWidth)
        self.y = randint(0,mapHeight)

    def __eq__(self,c):
        return (self.x == c.x and self.y == c.y )
            
    
    def __ne__(self,c):
        return not (self.x == c.x and self.y == c.y)
    
    def pr(self):
        print self.x
        print self.y