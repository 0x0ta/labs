def stray(arr):
    for each in arr:
        if arr.count(each) == 1:
            return each
