#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sugargame
import sugargame.canvas
import gtk

from sugar.activity import activity
from sugar.graphics.toolbarbox import ToolbarBox
from sugar.activity.widgets import ActivityToolbarButton
from sugar.activity.widgets import StopButton

import game

class HelloWorldActivity(activity.Activity):

    def __init__(self, handle):
        activity.Activity.__init__(self, handle)

        # Change the following number to change max participants
        self.max_participants = 1
        self.build_toolbar()
        self.actividad = game.MiJuego()
        self._pygamecanvas = sugargame.canvas.PygameCanvas(self)
        self.set_canvas(self._pygamecanvas)
        self._pygamecanvas.grab_focus()
        self._pygamecanvas.run_pygame(self.actividad.juego_loop)

    def read_file(self, file_path):
        pass
        
    def write_file(self, file_path):
        pass

    def build_toolbar(self):
        toolbar_box = ToolbarBox()
        toolbar_box.show()

        activity_button = ActivityToolbarButton(self)
        toolbar_box.toolbar.insert(activity_button, -1)
        activity_button.show()
        
        separator = gtk.SeparatorToolItem()
        separator.props.draw = False
        separator.set_expand(True)

        toolbar_box.toolbar.insert(separator, -1)
        stop_button = StopButton(self)
        toolbar_box.toolbar.insert(stop_button, -1)
        stop_button.show()

        self.set_toolbar_box(toolbar_box)
        toolbar_box.show_all()




