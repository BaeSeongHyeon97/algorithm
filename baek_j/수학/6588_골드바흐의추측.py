# def
def Goldbach(N):
    for i in range(len(prime)):
        for j in range(i + 1, len(prime)):
            if prime[i] + prime[j] == N:
                print(f'{N} = {prime[i]} + {prime[j]}')
                return
    else:
        print("Goldbach's conjecture is wrong.")
        return


# 소수 테이블 구하기
nums = [i for i in range(1000001)]
prime = []
ans = []
for n in nums:
    if n == 0 or n == 1:
        continue
    elif n > 2 and n % 2 == 0:
        nums[n] = 0
    else:
        prime.append(n)
        for j in range(n*2, 1000001, n):
            nums[j] = 0


while True:
    N = int(input())
    if N:
        Goldbach(N)
    else:
        break

# 시간초과아아아ㅏ!!!!!!
