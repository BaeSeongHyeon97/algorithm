import sys

N = int(input())
nums = list(map(int,sys.stdin.readline().split()))

li_n = list(set(nums))

dict_n = {}
for i in nums:
    dict_n[i] = dict_n.get(i, 0) + 1

ans = [-1] * N
stack = []

for i in range(N):
    while stack and (stack[-1][-1] < dict_n[nums[i]]):
        idx, val, cnt = stack.pop()
        ans[idx] = nums[i]
    stack.append([i,nums[i],dict_n[nums[i]]])

print(*ans)