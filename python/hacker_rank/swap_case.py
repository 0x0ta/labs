def swap_case(s):
    return "".join(each.swapcase() for each in s)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
