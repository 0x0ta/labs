def fake_bin(x):
    total = ""
    for each in x:
        if int(each) < 5:
            total = total + "0"
        else:
            total = total + "1"
    return total