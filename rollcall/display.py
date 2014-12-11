"""
Functions for displaying
"""

from main import *

def display_names(ext, dire):
    """
    yields all subject names
    """
    for filename in os.listdir(dire):
        name, extension = os.path.splitext(filename)
        if extension == ext:
            yield filename
