T = int(input())

for t in range(T):
    N = int(input())
    arr = list(map(int,input().split()))
    for i in range(N-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(f'#{t+1}', end=' ')
    for k in arr:
        print(k, end=' ')
    print()
