"""
Functions for displaying
fetching information
"""

import func_json as fj

def compare(first, second):
    """
    Compares two values
    """
    if first > second:
        return 1
    elif first < second:
        return -1
    return 0

def compare_date(first, second):
    first = map(int, first.split('/'))
    second = map(int, second.split('/'))

    val = compare(first[2], second[2])
    if val:
        return val
    val = compare(first[1], second[1])
    if val:
        return val
    val = compare(first[0], second[0])
    if val:
        return val
    return 0

def total_classes(json_dic):
    """
    Takes in a json dictionary
    returns total classes
    """
    return len(json_dic)

def total_classes_held(json_dic, field):
    """
    Takes in a json dictionary
    returns list of all the classes held
    """
    held = []
    for date in json_dic:
        if compare_date(date, field) == -1:
            held.append(field)
    return held

def classes_with_tag(json_dic, tag):
    """
    takes in a json dictionary
    returns list of all the classes 
    with the tag
    """
    pass

def classes_held_with_tag(json_dic, tag):
    """
    takes in a json dictionary
    returns list of all the classes 
    held with the tag
    """
    pass
