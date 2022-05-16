def xo(s):
    x_counter = 0
    o_counter = 0
    for each in s:
        if "x" in each.lower():
            x_counter += 1
        elif "o" in each.lower():
            o_counter += 1

    print(f"{x_counter} {o_counter}")
    if x_counter != o_counter:
        return False
    else:
        return True
