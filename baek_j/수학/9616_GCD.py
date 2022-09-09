import sys

def GCD(a,b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

t = int(input())
for _ in range(t):
    ans = 0
    nums = list(map(int, sys.stdin.readline().split()))
    for i in range(1,len(nums)):
        for j in range(i + 1, len(nums)):
            ans += GCD(nums[i], nums[j])
    print(ans)
