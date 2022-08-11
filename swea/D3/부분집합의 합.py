T = int(input())

for tc in range(1, T + 1):
    N, K = map(int,input().split())
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # 부분집합
    cnt = 0
    for i in range(1 << 12):
        s = 0
        subset = []
        for j in range(12):
            if i & (1 << j):
                subset.append(A[j])
                s += A[j]
        if len(subset) == N and s == K:
            cnt += 1

    print(f'#{tc} {cnt}')

