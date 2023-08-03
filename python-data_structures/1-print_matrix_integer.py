#!/usr/bin/python3
print_matrix_integer = __import__('1-print_matrix_integer').print_matrix_integer
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for num in row: 
            print("matrix = {}".format(num), end=" ")
        print_matrix_integer
   