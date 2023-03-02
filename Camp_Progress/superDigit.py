#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    supersum = str(sum([int(i) for i in p]))
    if len(n) == 1:
        if k == 1:
            return n
        return superDigit(n * k, 1)
    return superDigit(supersum, k)
    # if len(n) == k == 1:
    #     return n
    # def helper(p):
    #     if len(p) == 1:
    #         return p
    #     supersum = str(sum([int(i) for i in p]))
    #     return helper(supersum)
    # p = n * k
    # return helper(p)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
