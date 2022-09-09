# 소수 에라토스테네츠

prime = [0] * 1000001
is_prime = [1] * 1000001
for i in range(2, 1000001):
    if is_prime[i] == 1:
        prime[i] = i
        for j in range(i+i, 1000001, i):
            is_prime[j] = 0

tc = int(input())
for _ in range(tc):
    n = int(input())
    cnt = 0
    for i in range(2, n // 2 + 1):
        if prime[i] and is_prime[n-i]:
            cnt += 1
    print(cnt)