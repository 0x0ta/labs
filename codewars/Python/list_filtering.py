def filter_list(li):
    'return a new list with the strings filtered out'
    o = []
    for each in li:
        if type(each) is int:
            o.append(each)
    return o
