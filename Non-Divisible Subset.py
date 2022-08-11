#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    r = []
    for i in s:
        r.append(i%k)
    u = list(set(r))
    a = 0
    for i in u:
        if i == 0:
            a += 1
        elif i == k-i:
            a += 1
        else:    
            c_l = [r.count(i),r.count(k-i)]
            a += max(c_l)
            if (k-i) in u:
                u.remove(k-i)
    return a            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
