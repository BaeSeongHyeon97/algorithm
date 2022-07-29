T = int(input())

for t in range(1, T+1):
    H, W = map(int,input().split())
    print(f'#{t}')
    for h in range(H):
        nums = []
        for w in range(1, 1 + W):
            nums.append(w + W*h)
        
        if h % 2 == 0:    
            print(*nums)
        else:
            print(*nums[::-1])
