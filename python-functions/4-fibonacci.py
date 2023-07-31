def fibonacci_sequence(n):
    a = 0
    b = 1
    fibonacci_list = []
    for i in range(n):
        fibonacci_list.append(a)
        a, b = b, a + b
    return fibonacci_list
