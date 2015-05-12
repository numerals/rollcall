"""
Functions related to JSON
"""

import json
import exce
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

def get_status(json_dic, field):
    """
    Gets the value of a field
    returns the value
    if no such field raises NoField exception
    """
    if not json_dic.has_key(field):
        raise exce.NoField("No such field: %s" %(field))
    return json_dic[field]

def update_status(json_dic, field, val):
    """
    updates the value of a field
    returns the value
    if no such field raises NoField exception
    """
    if not json_dic.has_key(field):
        raise exce.NoField("No such Field : %s" %(field))
    json_dic[field] = val
    return json_dic[field]

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
        json_dict[format_date(d)] = TAGS['f']

    return json_dict

def update_json_dict(json_dic, date, status):
    """
    Updates a json dict
    changes status of date
    incase date is not a key
    raises NoField error
    """
    formatted_date = format_date(date)

    if not json_dic.has_key(formatted_date):
        raise exce.NoField("No such Date : %s" %(date))

    json_dic[formatted_date] = status
    return json_dic
