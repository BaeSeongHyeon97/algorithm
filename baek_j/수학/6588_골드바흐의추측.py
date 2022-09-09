# def
# def Goldbach(N):
#     for i in range(len(prime)):
#         for j in range(i + 1, len(prime)):
#             if prime[i] + prime[j] == N:
#                 print(f'{N} = {prime[i]} + {prime[j]}')
#                 return
#     else:
#         print("Goldbach's conjecture is wrong.")
#         return
#
#
# # 소수 테이블 구하기
# nums = [i for i in range(1000001)]
# prime = []
# ans = []
# for n in nums:
#     if n == 0 or n == 1:
#         continue
#     elif n > 2 and n % 2 == 0:
#         nums[n] = 0
#     else:
#         prime.append(n)
#         for j in range(n*2, 1000001, n):
#             nums[j] = 0
#
#
# while True:
#     N = int(input())
#     if N:
#         Goldbach(N)
#     else:
#         break

# 시간초과아아아ㅏ!!!!!!

# 에라톳
# 소수 구하기
prime = [1] * 1000001
for i in range(2, 1000000):
    if prime[i] == 1:
        prime[i] = i
        for j in range(i + i, 1000000, i):
            prime[j] = 0
while True:
    n = int(input())
    if n == 0:
        break
    # 짝수 검증
    # 모두 돌 필요 없음
    # 주어진 수에서 소수i를 빼서 소수면 가능
    for i in range(3, n//2 + 1):
        if prime[i] and prime[n-i]:
            print(f'{n} = {prime[i]} + {prime[n-i]}')
            break
    else:
        print("Goldbach's conjecture is wrong.")


