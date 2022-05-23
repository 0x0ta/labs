def square_digits(num):
    return int("".join(str(int(each) * int(each)) for each in str(num)))
