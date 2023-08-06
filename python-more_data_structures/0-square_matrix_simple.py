def square_matrix_simple(matrix=[]):
    # Get the dimensions of the input matrix
    rows = len(matrix)
    if rows == 0:
        return []

    cols = len(matrix[0])

    # Create a new matrix with the same size as the input matrix
    result_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    # Fill the new matrix with the squared values of the input matrix
    for i in range(rows):
        for j in range(cols):
            result_matrix[i][j] = matrix[i][j] ** 2

    return result_matrix
