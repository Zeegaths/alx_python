#!/usr/bin/python3
def exception_msg(message=""):
    try:
        exception_msg()
    except NameError as ne:
        print(ne)