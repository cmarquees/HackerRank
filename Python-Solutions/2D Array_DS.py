import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    SumArray = []
    lenth = len(arr)-2
    for line in range(lenth):
        for column in range(lenth):
            SumArray.append(arr[line][column] + arr[line][column+1] + arr[line][column+2]+ arr[line+1][column+1] + arr[line+2][column] + arr[line+2][column+1] + arr[line+2][column+2])
    return (max(SumArray))
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()