# from collections import deque
#
# N, K = map(int,input().split())
# # 데큐
# Q = deque([i for i in range(1, N + 1)])  # 0, 1, 2, 3, 4, 5, 6, 7
# ans = []
# while Q:
#     for i in range(K - 1):
#         Q.append(Q.popleft())
#     else:
#         ans.append(Q.popleft())
# print('<', end='')
# for i in ans:
#     if i == ans[-1]:
#         print(str(i), end='')
#     else:
#         print(str(i) + ',', end=' ')
# print('>')
#
# # =====================================
# N, K = map(int,input().split())
# # 선형큐
# Q = [i for i in range(N + 1)]  # 0, 1, 2, 3, 4, 5, 6, 7
# s, e = 0, N
# ans = []
# while s < e:
#     for i in range(s, s + (K - 1)):
#         s += 1
#         Q.append(Q[s])
#         e += 1
#     s += 1
#     ans.append(Q[s])
# print('<', end='')
# for i in ans:
#     if i == ans[-1]:
#         print(str(i), end='')
#     else:
#         print(str(i) + ',', end=' ')
# print('>')

# 원형큐
N, K = map(int,input().split())
Q = [i for i in range(1, N + 1)]
ans = []
idx = 0
while Q:
    idx = (idx + K - 1) % len(Q)
    ans.append(str(Q.pop(idx)))
print('<', ', '.join(ans), '>', sep='')