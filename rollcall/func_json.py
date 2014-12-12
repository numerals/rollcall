"""
Functions related to JSON
"""

import json
import exceptions
from datetime import date, timedelta

TAGS = { 'a' : "absent",
         'p' : "present",
         'f' : "future",
         'h' : "holiday",
         'o' : "other" }

def dict_to_json(json_dict):
    """
    convert from a dictionary to json
    """
    return json.dumps(json_dict) #, indent=4, separators=(',', ': '))

def json_to_dict(json_str):
    """
    convert from json to dictionary
    """
    return json.loads(json_str)

def format_date(d, form="%d/%m/%y"):
    """
    formats dates
    """
    return d.strftime(form)

def gen_dict(semester_start, class_weekdays, semester_weeks=16):
    """
    Generates a dictionary containing all possible class dates
    """
    class_dates = []
    for x in xrange(semester_weeks * 7):
        current_date = semester_start + timedelta(days=x)
        if current_date.weekday() in class_weekdays:
            class_dates.append(current_date)

    json_dict = {}
    for d in class_dates:
        json_dict[format_date(d)] = "future"

    return json_dict

def update_json_string(json_string, date, status):
    """
    Updates a json string
    changes status of date
    incase date is not a key
    raises
    """
    subject_data = json_to_dict(json_string)
    formatted_date = format_date(date)

    if not subject_data.has_key(formatted_date):
        raise exceptions.NoDate("No such date")

    subject_data[formatted_date] = status
    return dict_to_json(subject_data)
