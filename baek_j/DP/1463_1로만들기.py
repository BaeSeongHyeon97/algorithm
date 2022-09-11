# def f(n):
#     if n == 1:
#         return 0
#     elif 1 < n < 4:
#         return 1
#     else:
#         if memo[n] > 0:
#             return memo[n]
#         memo[n] = f(3) + f(n//3)+ (n % 3)
#         return memo[n]
#
#
#
# n = int(input())
# memo = [0] * (10**6+1)
# print(f(n))
# 반례 16


# N 을 1 로 만들기 => 큰 것을 작은 것으로 => DP사용
# import sys
# sys.setrecursionlimit(10000000)
#
# def D(N):  # N을 1로 만드는 최소 연산 횟수
#     if N == 1:
#         return 0
#     if memo[N]:
#         return memo[N]
#
#     memo[N] = D(N - 1) + 1
#     if not N % 2:
#         temp = D(N // 2) + 1
#         if memo[N] > temp:
#             memo[N] = temp
#     if not N % 3:
#         temp = D(N // 3) + 1
#         if memo[N] > temp:
#             memo[N] = temp
#     return memo[N]
# 메모리초과


N = int(input())
memo = [0] * (N + 1)
memo[1] = 0
for i in range(2, N+1):
    memo[i] = memo[i-1] +1
    if not i % 2 and memo[i] > memo[i//2] + 1:
        memo[i] = memo[i//2] + 1
    if not i % 3 and memo[i] > memo[i // 3] + 1:
        memo[i] = memo[i // 3] + 1

print(memo[N])
