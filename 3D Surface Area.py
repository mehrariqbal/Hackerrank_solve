#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#

def surfaceArea(A):
    # Write your code here
    def hor(a):
        h = 0
        for i in range(H):
            for j in range(W):
                if W-1 == 0:
                    h += a[i][j]*2
                    break
                if j == 0:
                    h += a[i][j]
                elif j == W-1:
                    h += a[i][j]
                    h += abs(a[i][j-1]-a[i][j])
                else:
                    h += abs(a[i][j-1]-a[i][j])
        return h
    def ver(a):
        v = 0 
        for j in range(W):
            for i in range(H):
                if H -1 == 0:
                    v += a[i][j]*2
                    break
                if i == 0:
                    v += a[i][j]
                elif i == H-1:
                    v += a[i][j]
                    v += abs(a[i-1][j]-a[i][j])
                else:
                    v += abs(a[i-1][j]-a[i][j])
        return v
    total = hor(A)+ver(A)+2*H*W
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
