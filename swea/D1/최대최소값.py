T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int,input().split()))
    max_idx = 0
    min_idx = 0
    for i in range(N):
        if arr[i] >= arr[max_idx]:
            max_idx = i
        elif arr[i] < arr[min_idx]:
            min_idx = i
    if (max_idx - min_idx) < 0:
        print(f'#{tc} {-(max_idx - min_idx)}')
    else:
        print(f'#{tc} {max_idx - min_idx}')