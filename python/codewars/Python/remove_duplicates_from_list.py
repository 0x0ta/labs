def distinct(seq):
    unique_list = []
    for x in seq:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list