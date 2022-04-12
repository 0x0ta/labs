x, k = map(int, input().split(" "))
p = input()


def main():
    return "".join("True" if (k == eval(p.strip("'"))) else "False")


print(f"{main()}")
