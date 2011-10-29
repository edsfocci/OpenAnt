# -*- coding: utf-8 -*-
#
# This file is part of Open Ant.
#
# Open Ant is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Open Ant.  If not, see <http://www.gnu.org/licenses/>.
#
# Map Class

class Items:
    Void,Food,Peeble = range(3)
    
class TileType:
    Ground,Rock,Wall,Nest,Void = range(5)
    
class Ants:
    Yellow = range(1)

class Actions:
    Idle,Move,GrabItem,DropItem = range(4)