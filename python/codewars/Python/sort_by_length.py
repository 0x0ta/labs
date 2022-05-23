def sort_by_length(arr):
    d = dict()
    for idx, each in enumerate(arr):
        d[len(each)] = each
    print(d)

    o = []
    for each in sorted(d):
        o.append(d.get(each))
    return o
