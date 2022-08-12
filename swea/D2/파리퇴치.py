T = int(input())

for tc in range(1, T + 1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    r = c = 0
    cnt = 0
    max_cnt = 0
    while True:
        for i in range(r, M + r):        # 01, 12, 23, 34
            for j in range(c, M + c):    # 01, 12, 23, 34
                cnt += arr[i][j]
        if cnt > max_cnt:
            max_cnt = cnt
        c += 1
        cnt = 0
        if c > N - M:
            c = 0
            r += 1
        if r > N - M:
            break
    print(f'#{tc} {max_cnt}')

