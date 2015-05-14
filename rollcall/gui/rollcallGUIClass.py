#!/usr/bin/env python2

"""
Contains the main GUI Class
"""

import os
import gtk


def find_file(dire, fName):
    """
    Generates the complete path of a file
    returns the complete path
    """
    path = os.path.join(os.path.dirname(dire), fName)
    return path


def load_interface(dire, fName):
    """
    Loads the interface
    in particular loads the glade file
    returns the builder
    """
    fName = find_file(dire, fName)
    builder = gtk.Builder()
    builder.add_from_file(fName)
    return builder


class rollcallGUIClass:
    """
    Sets up the GUI interface
    """
    def __init__(self):

        self.builder = load_interface(__file__, 'glade/rollcallGUI.glade')
        self.save_objects()
        self.builder.connect_signals(self.setup_signals())
        self.window.show_all()

    def setup_signals(self):
        """
        Sets up the signals
        """
        sig = {}

        return sig

    def save_objects(self):
        """
        Get the required objects
        """
        pass

    def close(self, *args):
        """
        Handles Destroy Event
        """
        gtk.main_quit()


if __name__ == '__main__':
    gtk.main()
