import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar.sort()
    countPars = 0
    pars = []
    for element in ar:
        nElements = ar.count(element)
        if (element not in pars):
            pars.append(element)
            if(nElements%2 == 0):
                countPars += nElements//2
            elif(((nElements-1)%2 == 0) and ((nElements-1) != 0)):
                countPars += (nElements-1)//2
    return countPars


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    #print(result)

    fptr.write(str(result) + '\n')

    fptr.close()