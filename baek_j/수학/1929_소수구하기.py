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

