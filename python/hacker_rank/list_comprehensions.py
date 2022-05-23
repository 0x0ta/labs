if __name__ == '__main__':
    x, y, z, n = (int(input()) + 1 for _ in range(4))
    print([[a, b, c] for a in range(x) for b in range(y)
           for c in range(z) if a + b + c != n - 1])
