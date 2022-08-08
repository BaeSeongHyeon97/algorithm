T = int(input())

for t in range(T):
    N = int(input())
    arr = list(map(int,input().split()))
    total = 0
    maxV = 0
    for i in range(N-1):
        total = arr[i] + arr[i+1]
        if total > maxV:
            maxV = total
    print(f'#{t+1} {maxV}')
