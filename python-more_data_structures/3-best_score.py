def best_score(a_dictionary):
    if a_dictionary == {}:
        return None
    else:
        best_score = max(a_dictionary)
print("Best: {}".format(best_score))
    