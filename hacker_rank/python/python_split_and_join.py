def split_and_join(line):
    return line.replace(" ", "-")

if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print result