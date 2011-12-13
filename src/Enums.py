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

class Items:
    Void,Food,Pebble = range(3)
    
class TileType:
    Ground,Rock,Wall,Nest,Empty,Void,Earth = range(7) 
    
class Ants:
    Yellow = range(1)

class Actions:
    Idle,Move,GrabItem,DropItem,Eat,Dig,GoThroughNest = range(7)

class Scents:
    Alarm,Trail,Nest = range(3)
    
class Teams:
    Red,Blue,Crit = range(3)

class PlayerType:
    Human,Computer = range(2)