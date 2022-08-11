# 같은색 겹치지 않는 케이스

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]
    cnt = 0
    for n in range(N):
        r1, c1, r2, c2, color = map(int,input().split())
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                arr[i][j] += color
                if arr[i][j] == 3:
                    cnt += 1

    print(f'#{tc} {cnt}')

# ----------------------------------------------------------
# 같은색 겹치는 케이스