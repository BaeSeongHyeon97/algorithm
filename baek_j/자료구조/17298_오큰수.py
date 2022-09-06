# import sys
#
# N = int(sys.stdin.readline())
# nums = list(map(int,sys.stdin.readline().split()))
# #
# for i in range(N):
#     li = [nums[i]]
#     top = 0
#     for j in range(i + 1, N):
#         if nums[j] > li[top]:
#             if top != 0:
#                 print(li[top], end=' ')
#                 break
#             else:
#                 li.append(nums[j])
#                 top += 1
#         else:
#             if top == 0:
#                 continue
#             else:
#                 print(li[top], end=' ')
#                 break
#     else:
#         if top == 0:
#             print(-1, end=' ')
#         else:
#             print(li[top], end=' ')

## 이중포문 쓰면 시간초과
# =====================================================================
import sys

N = int(input())
nums = list(map(int,sys.stdin.readline().split()))

stack = []
ans = [-1] * N

# 전체 돌껀데
for i in range(N):
    # 만약 스택에 값이 존재하는 경우와 동시에 맨 위의 값이 다음 값보다 작다면
    while stack and (stack[-1][1] < nums[i]):
        # 꺼내서
        idx, val = stack.pop()
        # 꺼낸 idx에 큰수(오큰수)를 입력
        ans[idx] = nums[i]
    # i와 값 스택에 추가
    stack.append([i, nums[i]])
print(*ans)