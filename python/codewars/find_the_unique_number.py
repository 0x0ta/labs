def find_uniq(arr):
    a = {}
    for each in arr:
        if each not in a:
            a[each] = 1
        elif each in a:
            a[each] += 1

    for each in a:
        if a.get(each) == 1:
            return each
