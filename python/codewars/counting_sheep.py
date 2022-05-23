def count_sheeps(sheep):
    counter = 0
    for each in sheep:
        if each == True:
            counter = counter + 1
    return counter