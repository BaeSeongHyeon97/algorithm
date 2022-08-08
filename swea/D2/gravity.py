T = int(input())

for t in range(T):
    N = int(input())
    arr = list(map(int,input().split()))
    maxV = 0
    for i in range(N):
        cnt = 0
        for j in arr[i+1:N]:
            if arr[i] > j:
                cnt += 1
        if cnt > maxV:
            maxV = cnt
    print(f'#{t+1} {maxV}')
