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

from Enums import *

SCENT_INIT_STRENGTH = 5
SCENT_AGING_DELAY = 10
SCENT_MAX_STRENGTH = 8
SCENT_PROPAGATE_DELAY = 7

class Scent:
 
    def __init__(self,type):    
        self.type = type
        pass
    
    def init(self):
        self.strength = SCENT_INIT_STRENGTH
        self.age = 0
        self.propagateDelay = 0

    def setStrength(self,strength):
        self.strength = strength
        self.age = 0

    def update(self):
        self.age+=1
        self.propagateDelay+=1
        if self.age % SCENT_AGING_DELAY == 0:
            self.strength-=1
         
        