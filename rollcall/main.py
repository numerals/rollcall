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
        raise exce.SubjectExists("Records for %s are already present" %(sub))

    with open(sub, "w") as recordFile:
        recordFile.write(json_str)

def get_json_file(sub):
    """
    Gets the json string from the file
    returns json as a dictionary
    """
    if not fileExists(sub):
        raise exce.SubjectError("Subject: %s does not exist" %(sub))

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

def gen_total_classes(field=None, ext='.json', dire=pDir()):
    """
    yields (subject, total_classes_till_field)
    """
    for filename in display_names(ext, dire):
        path = full_path_to(filename, dire)
        json_dic = get_json_file(path)
        total = len(display.total_classes(json_dic, field))
        yield filename, total

def gen_classes_with_tag(tag=fj.TAGS['p'], ext='.json', dire=pDir()):
    """
    yields (subject, total_classes_with_tag)
    """
    for filename in display_names(ext, dire):
        path = full_path_to(filename, dire)
        json_dic = get_json_file(path)
        total = len(display.classes_with_tag(json_dic, tag))
        yield filename, total

def gen_percent(tag=fj.TAGS['p'], ext='.json', dire=pDir()):
    """
    yields (subject, total_classes_with_tag)
    """
    for filename in display_names(ext, dire):
        path = full_path_to(filename, dire)
        json_dic = get_json_file(path)
        percent = display.percent(json_dic, tag)
        yield filename, percent

def deleteSubject(fName):
    """
    Delete a file and raises SubjectError if not Found
    """
    if not fileExists(fName):
        raise exce.SubjectError("Subject: %s is not Found" %(fName))
    os.remove(fName)

def reset(ext='.json', dire=pDir()):
    """
    removes all subjects
    a clean fresh start
    """
    for filename in display_names(ext, dire):
        path = full_path_to(filename, dire)
        os.remove(path)
