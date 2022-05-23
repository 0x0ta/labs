def multi_table(number):
    i = 1
    out = ""
    while i <= 10:
        out = out + f"{i} * {number} = {i * number}"
        if i < 10:
            out = out + "\n"
        i += 1
    return out