# 빠른 A + B
import sys

T = int(input())

for t in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B) 

import sys

T = int(input()) #Test case
for i in range(T):
        a,b = map(int, sys.stdin.readline().split())
        print(a+b)