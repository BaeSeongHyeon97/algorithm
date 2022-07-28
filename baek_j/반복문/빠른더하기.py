# 빠른 A + B

T = int(input())
total = 0
for t in range(T):
    A, B = map(int,input().split())
    total = A + B
    print(total)