"""
Main module
"""

import os
import func_json as fj
import display
import exceptions as exc
from datetime import date


def pDir():
    """
    gives the present working directory
    """
    return os.getcwd()

def full_path_to(fName, dire=pDir()):
    """
    joins the filename and the directory path
    """
    path = os.path.join(dire, fName)
    return path

def fileExists(fName):
    """
    Check if a file exists
    """
    if os.path.isfile(fName):
        return True
    return False

def add(json_str, sub):
    """
    Add a subject
    creates a new sub.json file
    """
    if fileExists(sub):
        raise exc.SubjectExists("Records for this subject are already present")

    with open(sub, "w") as recordFile:
        recordFile.write(json_str)

def update_json_file(tag, sub, date=date.today()):
    """
    Update a subject
    """
    if not fileExists(sub):
        raise exc.SubjectError("Subject does not exit")

    if tag not in fj.TAGS.keys():
        raise exc.UnknownTag("Tag UNKNOWN")

    with open(sub, "r") as recordFile:
        json_string = recordFile.read()

    newdata = fj.update_json_string(json_string, date, fj.TAGS[tag])
    with open(sub, "w") as recordFile:
        recordFile.write(newdata)
    return True

def fileDelete(fName):
    """
    Delete a file and return status
    """
    if fileExists(fName):
        os.remove(fName)
        return True
    return False

def delete(sub):
    """
    Delete a subject
    """
    if fileDelete(sub):
        return True
    return False

def reset(ext='.json', dire=pDir()):
    """
    removes all subjects
    a clean fresh start
    """
    for filename in display.display_names(ext, dire):
        path = full_path_to(filename, dire)
        os.remove(path)
