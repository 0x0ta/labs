# Enter your code here. Read input from STDIN. Print output to STDOUT
i = int(input())
shoes = list(map(int, input().split()))
customers = int(input())

total = 0

for _ in range(customers):
    sale = tuple(map(int, input().split()))
    if sale[0] in shoes:
        total = total + sale[1]
        shoes.remove(sale[0])

print(total)
