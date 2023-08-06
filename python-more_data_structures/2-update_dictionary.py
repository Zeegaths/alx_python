def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    my_dict = {}
    update_dictionary(my_dict, key, value)
    update_dictionary(my_dict, key, value)
    print(my_dict)