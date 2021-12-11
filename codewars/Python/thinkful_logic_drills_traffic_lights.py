def update_light(current):
    arr = iter(["green", "yellow", "red", "green"])
    for each in arr:
        if current == each:
            return next(arr)