def is_prime(number):
    while number >= 2:
        for i in range(2, int(number)):
            if number % 1 == 0:
                return False
    return True