#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    num_valleys = 0  
    level = 0              
    for i in s:
        if i == 'U':       
            level += 1
        else:              
            if level == 0:
                num_valleys += 1
            level -= 1
    return num_valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
