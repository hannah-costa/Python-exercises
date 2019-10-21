"""
Solved by: phanThASm
URL to problem: https://www.hackerrank.com/challenges/pairs/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    count = 0
    dictionary = {}
    for i in range(len(arr)):
        dictionary[str(arr[i])] = arr[i]
    for i in range(len(arr)):
        if str(dictionary[str(arr[i])]+k) in dictionary.keys():
            count += 1
    return count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
