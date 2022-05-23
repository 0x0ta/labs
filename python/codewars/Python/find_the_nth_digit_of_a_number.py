def find_digit(num, nth):
    le = len(str(num))
    print(f"{nth = }")
    num = str(num).replace("-", "")
    if nth <= 0:
        return -1
    else:
        for idx, each in enumerate(num[::-1]):
            if nth > le:
                return 0
            elif nth == idx + 1:
                return int(each)
