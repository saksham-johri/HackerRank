#!/bin/python3

import math
import os
import random
import re
import sys

i,j,k=list(map(int,input().split()))
b=0

for p in range(i,j+1):
    x=p
    rev=0
    while(x>0):
        r=x%10
        rev=rev*10+r
        x=x//10

    if abs(p-rev)%k==0:
        b+=1
print(b)
