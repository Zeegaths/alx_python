#!/usr/bin/python3
raise_exception_msg = __import__('5-raise_exception_msg').raise_exception_msg
def exception_msg(message=""):
    try:
        raise_exception_msg()
    except NameError():
        print()