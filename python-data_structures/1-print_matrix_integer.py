def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for num in row: 
            print("{}, ".format(num))
    print_matrix_integer()