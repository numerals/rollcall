"""
Helper module
"""

import sys
from os.path import realpath, dirname
from datetime import date, timedelta

sys.path.append(dirname(realpath(__file__)) + '/..')
import main
import func_json as fj

def newFile(fName):
    with open(fName, 'w') as f:
        pass

def gen_testData(dire=main.pDir(), weeks=1):
    filename, ext = '', '.json'
    today = date.today()
    for num in range(weeks * 7):
        json = fj.gen_dict(today, [0,1,2,3,4,5,6], 1)
        for x in range(num):
            current = today + timedelta(days=x)
            formatted = fj.format_date(current)
            fj.update_status(json, formatted, fj.TAGS['p'])
        json_str = fj.dict_to_json(json)
        name = filename + str(num) + ext
        path = main.full_path_to(name, dire)
        main.add(json_str, path)
