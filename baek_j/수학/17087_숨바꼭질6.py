import sys

def GCD(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

n, s = map(int,input().split())
li = list(map(int, sys.stdin.readline().split()))

gaps = []
for i in li:
    gaps.append(abs(s - i))
min_v = 999999999999
if n == 1:
    print(*gaps)

else:
    for i in range(n - 1):
        val = GCD(gaps[i], gaps[i + 1])
        gaps[i + 1] = val
        if val < min_v:
            min_v = val
    print(min_v)
