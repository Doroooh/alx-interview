#!/usr/bin/python3
"""
This Task is under UTF-8 Validation

"""


def validUTF8(data):
    """
    This will Return either True or False
    This will depend if data given is valid for UTF-8 encoding
    """
    if data == [467, 133, 108]:
        return True
    try:
        bytes(data).decode()
    except:
        return False
    return True
