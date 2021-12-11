if __name__ == '__main__':
    s = input()
    print(f"{any(c.isalnum() for c in s)}\n{any(c.isalpha() for c in s)}\n{any(c.isdigit() for c in s)}\n{any(c.islower() for c in s)}\n{any(c.isupper() for c in s)}")
