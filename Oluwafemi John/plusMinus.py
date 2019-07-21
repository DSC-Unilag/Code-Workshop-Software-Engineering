#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr): 
    neg = 0
    pos = 0
    zer = 0
    
    for i in arr:
        if i < 0:
            neg += 1
        elif i == 0:
            zer += 1
        else: pos += 1
        
    a = pos/n
    b = neg/n
    c = zer/n
    print (str.format('{0:.6f}', a))
    print (str.format('{0:.6f}', b))
    print (str.format('{0:.6f}', c))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
