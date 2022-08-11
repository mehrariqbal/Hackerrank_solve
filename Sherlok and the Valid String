#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    s_u = set(s)
    d = []
    for i in s_u:
        d.append(s.count(i))
        
    if max(d)-min(d) > 1:
        if min(d) == 1 and d.count(max(d))== len(d)-1:
            return 'YES'
        else:
            return 'NO'
    elif max(d) == min(d):
        return 'YES'
    else:
        if d.count(max(d)) > 1:
            if d.count(min(d)) > 1:
                return 'NO'
            else:
                return 'YES'
        else:
            return 'YES'
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
