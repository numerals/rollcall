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

def total_classes(json_dic, field=None):
    """
    Takes in a json dictionary
    returns list of all the classes held
    """
    held = []
    for date in json_dic:
        if field == None or compare_date(date, field) == -1:
            held.append(field)
    return held

def classes_with_tag(json_dic, tag=fj.TAGS['p']):
    """
    takes in a json dictionary
    returns list of all the classes
    with the tag
    """
    classes = []
    for field in json_dic:
        if fj.get_status(json_dic, field) == tag:
            classes.append(field)
    return classes

def percent(json_dic, tag=fj.TAGS['p']):
    """
    takes in a json dictionary
    returns percentage of classes with tags
    wrt total classes
    """
    total = len(total_classes(json_dic))
    classes = len(classes_with_tag(json_dic, tag))
    percent = (float(classes) / total) * 100
    return percent
