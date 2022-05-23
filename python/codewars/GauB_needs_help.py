def f(n):
    return 0 + sum(i for i in range(0, n+1)) if type(n) == int and n > 0 else None
