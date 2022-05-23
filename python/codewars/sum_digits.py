def sum_digits(number):
    o = 0
    for each in str(number):
        if each.isnumeric() is True:
            o = int(o) + int(each)
    return o
