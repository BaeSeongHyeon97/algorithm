# 1986 지그재그

T = int(input())

for t in range(1, T+1):
    nums = []
    N = int(input())
    for n in range(1,N + 1):
        if n % 2:
            nums.append(n)
        else:
            nums.append(-n)
    total = 0
    for num in nums:
        total += num
    

    print(f'#{t} {total}')