for x in range(10):
    for y in range(x + 1, 10):
        if x < 8:
            print("{:0d}{:0d}".format(x, y), end=", ")
        else:
            print("{:0d}{:0d}".format(x, y))
            
     
