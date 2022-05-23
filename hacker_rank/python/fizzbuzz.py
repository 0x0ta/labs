#!/bin/python

def fizzBuzz(n):
    i = 0
    while i < n:
        i += 1
        if int(i % 3 == 0) is True and int(i % 5 == 0) is True:
            print("FizzBuzz")
        elif int(i % 3 == 0) is True and int(i % 5 == 0) is False:
            print("Fizz")
        elif int(i % 3 == 0) is False and int(i % 5 == 0) is True:
            print("Buzz")
        else:
            print(i)


if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
