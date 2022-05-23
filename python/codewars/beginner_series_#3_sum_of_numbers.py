def get_sum(a, b):
    out = 0
    ab = sorted((a, b))
    for i in range(ab[0], ab[1] + 1):
        out = out + i
    return out
