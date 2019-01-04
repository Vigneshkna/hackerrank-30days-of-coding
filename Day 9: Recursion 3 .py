import math
import os
import random
import re
import sys
def factorial(num):
    return 1 if num == 1 else factorial(num - 1) * num
    print(factorial(int(input())))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
     n = int(input())
    result = factorial(n)
    fptr.write(str(result) + '\n')
    fptr.close()
