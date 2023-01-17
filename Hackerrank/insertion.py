#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    min = arr[n-1]
    j = n-2
    while j >= 0 and arr[j] > min:
        arr[j+1] = arr[j]
        j = j-1
        print(*arr)
    arr[j+1] = min
    print(*arr)



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)