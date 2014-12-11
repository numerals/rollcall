"""
Main module
"""

import os
from func_json import *
from datetime import date

tags = { 'a' : "absent",
         'p' : "present",
         'f' : "future",
         'h' : "holiday",
         'o' : "other" }

def pDir():
    """
    gives the present working directory
    """
    return os.getcwd()

def fileExists(fName, dire=pDir()):
    """
    Check if a file exists
    """
    if os.path.isfile(os.path.join(dire, fName)):
        return True
    return False

def fileDelete(fName, dire=pDir()):
    """
    Delete a file and return status
    """
    if fileExists(fName):
        os.remove(os.path.join(dire, fName))
        return True
    return False

def add(sub, json_str):
    """
    Add a subject
    """
    if fileExists(sub + '.json'):
        print "Records for this subject are already present"
    else:
        recordFile = open(sub + '.json', "w")
        recordFile.write(json_str)
        recordFile.close()

def delete(sub):
    """
    Delete a subject
    """
    if fileDelete(sub + '.json'):
        return True
    return False

def update(sub, tag, day=date.today()):
    """
    Update a subject
    """
    filename = sub + '.json'
    if tag not in tags.keys():
        print "Unknown tag"
        return

    if fileExists(filename):
        recordFile = open(filename, "r")
        json_string = recordFile.read()
        recordFile.close()
        recordFile = open(filename, "w")
        newdata = update_json_string(json_string, date, tags[tag])
        recordFile.write(newdata)
        recordFile.close()

def display_names():
    """
    Display all subject name
    """
    pass

def display_subject():
    """
    displays a particular subject
    """
    pass

def display_all_subjects():
    """
    displays all the subjects
    preferably a generator
    """
    pass

def reset():
    """
    Reset subjects data
    """
    pass
