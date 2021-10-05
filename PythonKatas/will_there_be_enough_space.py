def enough(cap, on, wait):
    return int("".join("0" if wait + on < cap else str(cap - (wait + on)).replace("-", "")))