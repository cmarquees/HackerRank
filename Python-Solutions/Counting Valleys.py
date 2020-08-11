#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valleyCount = 0
    flag = "sea"
    path = []
    for step in s:
        if(flag == "sea"):
            path.append(step)
            if(step == "U"):
                flag = "Montain"
            elif(step == "D"):
                flag = "Valley"
        elif(flag == "Montain"):
            if(step == "U"):
                path.append(step)
            elif(step == "D"):
                path.pop()
                if(path == []):
                    flag = "sea"
        elif(flag == "Valley"):
            if(step == "U"):
                path.pop()
                if(path == []):
                    flag = "sea"
                    valleyCount += 1
            elif(step == "D"):
                path.append(step)

    return valleyCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
