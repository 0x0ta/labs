def odd_or_even(arr):
    return "".join("odd" if sum(arr) % 2 != 0 else "even")
