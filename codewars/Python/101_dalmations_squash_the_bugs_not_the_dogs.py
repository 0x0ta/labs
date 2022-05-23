def how_many_dalmations(n):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
    return dogs[0] if n <= 10 else dogs[1] if n <= 50 else dogs[3] if n == 101 else dogs[2]
