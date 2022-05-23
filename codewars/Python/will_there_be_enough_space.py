def enough(cap, on, wait):
    return 0 if wait + on < cap else abs(cap - (wait + on))