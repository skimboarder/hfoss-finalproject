# Copyright 2009 Simon Schampijer
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

"""HelloWorld Activity: A case study for developing an activity."""

from gi.repository import Gtk
import logging
import cairo

from gettext import gettext as _

from sugar3.activity import activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import ActivityButton
from sugar3.activity.widgets import TitleEntry
from sugar3.activity.widgets import StopButton
from sugar3.activity.widgets import ShareButton
from sugar3.activity.widgets import DescriptionItem

class HelloWorldActivity(activity.Activity):
    """HelloWorldActivity class as specified in activity.info"""

    def __init__(self, handle):
        """Set up the HelloWorld activity."""
        activity.Activity.__init__(self, handle)

        # Change the following number to change max participants
        self.max_participants = 1

        toolbar_box = ToolbarBox()

        activity_button = ActivityButton(self)
        toolbar_box.toolbar.insert(activity_button, 0)
        activity_button.show()

        title_entry = TitleEntry(self)
        toolbar_box.toolbar.insert(title_entry, -1)
        title_entry.show()

        description_item = DescriptionItem(self)
        toolbar_box.toolbar.insert(description_item, -1)
        description_item.show()

        share_button = ShareButton(self)
        toolbar_box.toolbar.insert(share_button, -1)
        share_button.show()
        
        separator = Gtk.SeparatorToolItem()
        separator.props.draw = False
        separator.set_expand(True)
        toolbar_box.toolbar.insert(separator, -1)
        separator.show()

        stop_button = StopButton(self)
        toolbar_box.toolbar.insert(stop_button, -1)
        stop_button.show()

        self.set_toolbar_box(toolbar_box)
        toolbar_box.show()

        # Change the following text to change the message (Default: 'Hello World!'



        
        grid = Gtk.Grid()


        



        label = Gtk.Label(_("Hello World!"))
        angle = Gtk.Button(label=_("------------ \n\ \n \ \n  \ "))
        grid.attach(angle ,0, 0, 1, 1)
        acuteBut = Gtk.Button(label=_("Acute Angle"))
        grid.attach(acuteBut, 3, 3, 1, 1)
        rightBut = Gtk.Button(label=_("Right Angle"))
        grid.attach(rightBut, 4, 3, 1, 1)
        obtBut = Gtk.Button(label=_("Obtuse Angle"))
        grid.attach(obtBut, 3, 4, 1, 1)

        try:
            grid.attach(drawArea, 0, 0, 1, 1)
        except Exception as e:
            label = Gtk.Label(_(e))
            grid.attach(label, 0, 0, 1, 1)
            
        
        

        
        self.set_canvas(grid)
        self.show_all()

        
    