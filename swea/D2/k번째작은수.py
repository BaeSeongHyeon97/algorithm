T = int(input())
for tc in range(1, T + 1):
    N, K = map(int,input().split())
    arr = list(map(int,input().split()))
    # 선택정렬
    # K번만 최소를 찾는것을 반복하면 K번쩨로 작은 숫자를 찾을 수 있음
    for i in range(N):
        min_idx = i
        for j in range(i + 1, N):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    # 같은거를 빼고 계산...
    arr = list(set(arr))
    print(f'#{tc} {arr[K-1]}')
