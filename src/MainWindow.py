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

from PyQt4.QtCore import QTime
from PyQt4.QtGui import QMainWindow, QApplication, QPalette, QColor
from GLWidget import GLWidget
from LeftPanel import LeftPanel
from Map import Map

from PyQt4.phonon import Phonon
from MusPanel import MusPanel

import Globals

class MainWindow(QMainWindow):
    '''The main game window, holds all the panels and widgets.'''

    def __init__(self):
        QMainWindow.__init__(self)

        Globals.glwidget = GLWidget(self)
        self.setCentralWidget(Globals.glwidget)
        Globals.glwidget.makeCurrent() 
        
        Globals.mediaobject = Phonon.MediaObject(self)
        self.audioOutput = Phonon.AudioOutput(Phonon.MusicCategory, self)
        Phonon.createPath(Globals.mediaobject, self.audioOutput)
        
    def start(self):
        
        Globals.muspanel = MusPanel(self)
        
        # Load the main game menu panel.
        LeftPanel(self)
        
    def closeEvent(self, event):
        Globals.game_is_running = False
        event.accept()
