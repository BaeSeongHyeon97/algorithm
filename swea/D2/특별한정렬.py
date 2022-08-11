T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int,input().split()))

    # max, min, max, min, max, min으로
    # 선택정렬
    # min을 홀수 index에 정렬
    for i in range(N - 1):
        max_idx = i
        min_idx = i
        if i % 2 == 0:
            for k in range(i + 1, N):
                if arr[max_idx] < arr[k]:
                    max_idx = k
            arr[i], arr[max_idx] = arr[max_idx], arr[i]

        else:
            for j in range(i + 1, N):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    print(f'#{tc}', end=' ')
    for i in range(10):
        print(arr[i], end=' ')
    print()

