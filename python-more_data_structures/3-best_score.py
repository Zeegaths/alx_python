def best_score(a_dictionary):
    if not a_dictionary:
        return None

    max_score = None
    for score in a_dictionary.values():
        if max_score is None or score > max_score:
            max_score = score

    return max_score

    