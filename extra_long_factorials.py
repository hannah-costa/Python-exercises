"""
Solved by: phanThASm
URL to problem: https://www.hackerrank.com/challenges/extra-long-factorials/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
  return 1 if n <= 1 else (n * extraLongFactorials(n-1))
  """
  if( n <= 1 ):
    return 1
  else:
    return n * extraLongFactorials(n-1)
  """

if __name__ == '__main__':
  n = int(input())

  print(extraLongFactorials(n))
