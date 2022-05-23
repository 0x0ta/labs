# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
s, i = input().split()
d = list(permutations(sorted(s), int(i)))
y = [''.join(i) for i in d]

st = ""

for char in y:
    st = st + char + "\n"

print(st)
