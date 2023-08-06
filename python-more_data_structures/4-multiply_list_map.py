def multiply_list_map(my_list=[], number=0):
 new_list = list(map(lambda x: multiply_list_map(x, number), my_list))
 return new_list