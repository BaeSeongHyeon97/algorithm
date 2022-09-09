nums = [i for i in range(1000001)]
ans = []  # 소수
M, N = map(int,input().split())
for n in nums:
    if n == 0 or n == 1:
        continue
    elif n % 2 == 0 and n > 2:
        nums[n] = 0
    else:
        if M <= n <= N:
            ans.append(n)
        for i in range(n*2, 1000000, n):
            nums[i] = 0

for i in ans:
    print(i)

# 에라토스테네스의 채
# 소수 저장 배열 1개
# 방문 표시 배열 1개

m, n = map(int, input().split())
prime = [0] * 1000001
check = [0] * 1000001
for i in range(2, 1000001):
    if check[i] == 0:
        prime[i] = i
        if i > n:
            break
        for j in range(i+i, 1000001, i):
            check[j] = 1

ans = prime[m:n+1]
for a in ans:
    if a:
        print(a)