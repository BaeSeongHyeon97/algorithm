# import sys
# N = int(input())
# P = list(map(int,sys.stdin.readline().split()))
# val = P[-1]
# # 1개당 가격으로 바꾸기
# for i in range(N):
#     P[i] = [P[i]/(i+1), (i+1)]
# # print(P)
# P.sort(reverse=True)
# print(P)
# ans = 0
# # N개 중에서 최대로 구매할수 있는 만큼 비싸게 구매하기
# for p in P:
#     a = N // p[1]
#     b = N % p[1]
#     if a:
#         ans += a * p[0] * p[1]
#         N = b
#         if N == 0:
#             break
# print(max(int(ans), val))

# 31퍼에서 틀림
# ======================================
import sys

N = int(input())
P = list(map(int,sys.stdin.readline().split()))
D = [0] * (N + 1)

for i in range(1, N + 1):  # D[1]부터 D[N]을 구할거임
    for j in range(1, i + 1):  # 그중에서 최대를 구할껴
        D[i] = max(D[i], P[j - 1] + D[i - j])
print(D[N])

