# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
s, i = input().split(" ")

d = combinations_with_replacement(sorted(s), int(i))

for each in d:
    letter = ""
    for c in each:
        letter = letter + c
    print(f"{letter}")
