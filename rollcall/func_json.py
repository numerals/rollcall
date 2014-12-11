"""
Functions related to JSON
"""

import json
from datetime import date, timedelta

DAYS = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
TAGS = ["attended", "missed", "holiday", "future"]

def dict_to_json(json_dict):
    """
    convert from a dictionary to json
    """
    return json.dumps(json_dict, indent=4, separators=(',', ': '))

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
