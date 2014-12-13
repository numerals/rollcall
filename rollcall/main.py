"""
Main module
"""

import os
import func_json as fj
import display
import exce
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
        raise exce.SubjectExists("Records for this subject are already present")

    with open(sub, "w") as recordFile:
        recordFile.write(json_str)

def get_json_file(sub):
    """
    Gets the json string from the file
    returns json as a dictionary
    """
    if not fileExists(sub):
        raise exce.SubjectError("Subject: %s does not exit" %(sub))

    with open(sub, "r") as recordFile:
        json_string = recordFile.read()

    return fj.json_to_dict(json_string)

def update_json_file(tag, sub, date=date.today()):
    """
    Update a subject
    """
    if tag not in fj.TAGS.keys():
        raise exce.UnknownTag("Tag: %s UNKNOWN" %(tag))

    json_dic = get_json_file(sub)

    new_json= fj.update_json_dict(json_dic, date, fj.TAGS[tag])
    newdata = fj.dict_to_json(new_json)
    with open(sub, "w") as recordFile:
        recordFile.write(newdata)

    return True

def display_names(ext='.json', dire=pDir()):
    """
    yields all subject names
    """
    for filename in os.listdir(dire):
        name, extension = os.path.splitext(filename)
        if extension == ext:
            yield filename

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
    for filename in display_names(ext, dire):
        path = full_path_to(filename, dire)
        os.remove(path)
