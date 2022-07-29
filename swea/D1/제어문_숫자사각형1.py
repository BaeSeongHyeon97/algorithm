T = int(input())

for t in range(1, T+1):
    H, W = map(int,input().split())
    print(f'#{t}')
    for h in range(H):
        nums = []
        for w in range(1, W + 1):
            nums.append(w + W*h)
        print(*nums)