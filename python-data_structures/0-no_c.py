#!/usr/bin/env python3
no_c = __import__('0-no_c').no_c
def no_c(my_string):
    for chr in my_string:
        del("c" , "C")
print("{my_string}")  
        