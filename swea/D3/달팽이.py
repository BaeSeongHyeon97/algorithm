T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]
    r = c = 0
    arr[r][c] = 1
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    a = 2
    i = 0
    for _ in range(10):
        for j in range(n):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                i += 1
                break

            arr[nr][nc] = a
            a += 1
            r = nr
            c = nc



    print(*arr)