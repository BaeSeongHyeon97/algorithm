import sys

n = int(sys.stdin.readline())
nums = list(range(1,n+1))
ans = [0] * n
stack = [0] * (n + 1)
top = 0
for i in range(n):
    num = int(sys.stdin.readline())
    ans[i] = num
li = []
i = -1
j = 0
while j < n:

    if stack[top] != ans[j]:
        top += 1
        i += 1
        if i < n:
            stack[top] = nums[i]
            li.append('+')
        else:
            print('NO')
            break
    else:
        top -= 1
        j += 1
        li.append('-')
else:
    for i in li:
        print(i)