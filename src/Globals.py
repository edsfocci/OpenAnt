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

#general
vbos = False
glWidget = None
player = None
overMap= None
dataDir = "../data/"
pixelSize  = 32    #Size of tiles' side
mapHeight = 32
mapWidth  = 32
undergroundHeight = 32
undergroundWidth  = mapHeight
underground = False
undergroundChunk = 5
gameIsRunning = False

#nest camera coordinates
blackNestX = 0
blackNestY = -1 * pixelSize * (mapHeight + 1)
redNestX = -1 * pixelSize * (mapWidth * 0.5)
redNestY = -1 * pixelSize * (mapHeight + 1)

#camera bounds
leftBound = 0
rightBound = -1 * mapWidth * pixelSize
upBound = 0
downBound = -1 * mapHeight * pixelSize

#music
mediaobject = None
