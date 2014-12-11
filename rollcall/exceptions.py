"""
Custom Exceptions
"""

class SubjectExists(Exception):
    """
    Raised when subject already exists
    """
    pass

class UnknownTag(Exception):
    """
    Raised when tag is not recognised 
    """
    pass
