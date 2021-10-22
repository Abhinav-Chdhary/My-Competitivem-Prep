#!/bin/python

import math
import os
import random
import re
import sys

def main():
    if isItOdd(n):
        print("Weird")
    elif not isItOdd(n) and (2 <= n <= 5):
        print("Not Weird")
    elif not isItOdd(n) and (6 <= n <= 20):
        print("Weird")
    elif n>20:
        print("Not Weird")
    
def isItOdd(n):
    if n % 2 == 0:
        return False
    else:
        return True


if __name__ == '__main__':
    n = int(input().strip())
    main()
