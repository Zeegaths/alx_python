def print_matrix_integer(matrix=[[]]):
    if not matrix:  # Base case: check if the matrix is empty
        return
    for row in matrix:
        for num in row:
            print("{:d}".format(num),end="")
        print()
   