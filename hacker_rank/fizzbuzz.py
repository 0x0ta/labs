#!/bin/python

import math
import os
import random
import re
import sys


def fizzBuzz(n):
    i = 0
    while i < n:
        i += 1
        if int(i % 3 == 0) == True and int(i % 5 == 0) == True:
            print("FizzBuzz")
        elif int(i % 3 == 0) == True and int(i % 5 == 0) == False:
            print("Fizz")
        elif int(i % 3 == 0) == False and int(i % 5 == 0) == True:
            print("Buzz")
        else:
            print(i)


if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
