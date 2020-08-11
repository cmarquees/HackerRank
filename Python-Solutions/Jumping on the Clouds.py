#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    count = 0
    tam = len(c)
    while (count < tam):
        print(count)
        if(count+2 <= tam-1):
            if(c[count+2] == 0):
                jumps += 1
                count += 2
            else:
                jumps += 1
                count += 1
        else:
            jumps += 1
            count += 1

    return jumps-1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
