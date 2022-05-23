def fake_bin(x):
    return "".join("0" if int(each) < 5 else "1" for each in x)