def define_suit(card):
    dict = {"S": "spades", "C": "clubs", "H": "hearts", "D": "diamonds"}
    return dict.get(card[-1:])