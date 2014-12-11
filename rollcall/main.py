"""
Main module
"""

import json
from datetime import date, timedelta
import os

days = ["mon", "tue", "wed", "thu", "fri", "sat"]
tags = ["attended", "missed", "holiday", "future"]

def dict_to_json(json_dict):
    return json.dumps(json_dict, indent=4, separators=(',', ': '))

def json_to_dict(json_str):
    return json.loads(json_str)

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

def add():
    """
    Add a subject
    """
    pass

def update():
    """
    Update a subject
    """
    pass

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

def delete():
    """
    Delete a subject
    """
    pass

def format_date(d, form="%d/%m/%y"):
    return d.strftime(form)

def gen_dict(semester_start, class_weekdays, semester_weeks=16):
    class_dates = []
    for x in xrange(semester_weeks * 7):
        current_date = semester_start + timedelta(days=x)
        if current_date.weekday() in class_weekdays:
            class_dates.append(current_date)

    json_dict = {}
    for d in class_dates:
        json_dict[format_date(d)] = "future"

    return json_dict
