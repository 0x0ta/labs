if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(str(sorted(set(arr))[::-1][1]))
