s = tuple(map(int, input().split()))
t = tuple(map(int, input().split()))

st = ""

for i in s:
    for j in t:
        st = st + f"({i}, {j}) "

print(st)
