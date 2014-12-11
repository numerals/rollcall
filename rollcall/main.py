"""
Main module
"""

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
