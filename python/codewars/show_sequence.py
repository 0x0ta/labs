def show_sequence(n):
    s = ""
    o = 0
    if n > 0:
        for idx, i in enumerate(range(0, n)):
            s = s + str(idx) + "+"
            o = o + int(i)
        s = s + str(n) + " = " + str((int(o) + n))
    elif n == 0:
        s = "0=0"
    else:
        s = f"{n}<0"
    return s
