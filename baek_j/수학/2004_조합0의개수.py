# 조합
# 팩토리알로 가능

# 시간초과
# def fact(n):
#     ans = 1
#     for i in range(1,n + 1):
#         ans *= i
#     return ans

# 시간초과
# import sys
# def fact(n):
#     sys.setrecursionlimit(10**9)
#     if n == 1 or n == 0:
#         return 1
#     else:
#         li.append(n * fact(n-1))
#         return li[n]
#
# n, m = map(int, input().split())
# li = [1, 1]
# comb = str(fact(n) // (li[n] * li[n-m]))
# cnt = 0
# for c in comb[::-1]:
#     if c == '0':
#         cnt += 1
#     else:
#         break
# print(cnt)

# 0의 개수 => 소인수분해시 10의 개수 => 2 * 5 의 개수 => 2의 개수, 5의 개수
def Cnt2(n):
    i = 2
    cnt_2 = 0
    while i <= n:
        cnt_2 += n // i
        i *= 2
    return cnt_2

def Cnt5(n):
    i = 5
    cnt_5 = 0
    while i <= n:
        cnt_5 += n // i
        i *= 5
    return cnt_5

n, m = map(int, input().split())

ans = min(Cnt2(n) - Cnt2(m) - Cnt2(n-m), Cnt5(n) - Cnt5(m) - Cnt5(n-m))
print(ans)