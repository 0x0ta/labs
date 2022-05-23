min_axis = []
x, i = input().split(" ")
for _ in range(int(x)):
    min_axis.append(min(input().split(" ")))

print(max(min_axis))
