def small_enough(array, limit):
    for each in sorted(array):
        if each > limit:
            return False
    return True
