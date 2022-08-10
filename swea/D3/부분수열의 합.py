T = int(input())

for tc in range(1, T + 1):
    n, k = map(int,input().split())
    nums = list(map(int,input().split()))
    a = len(nums)
    cnt = 0
    for i in range(1 << a):
        s = 0
        for j in range(a):
            if i & (1 << j):
                s += nums[j]
        if s == k:
            cnt += 1
    print(f'#{tc} {cnt}')


