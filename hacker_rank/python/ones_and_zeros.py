def binary_array_to_number(arr):
    i = ""
    for each in arr:
        i = i + str(each)
    return int(i, 2)
