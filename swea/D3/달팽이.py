T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]
    r = c = 0
    arr[r][c] = 1
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    direction = 0
    for move in range(1, n ** 2 + 1):
        arr[r][c] = move
        r += dr[direction]
        c += dc[direction]
        if r < 0 or c < 0 or r >= n or c >= n or arr[r][c] != 0:
            r -= dr[direction]
            c -= dc[direction]
            direction = (direction + 1) % 4
            r += dr[direction]
            c += dc[direction]

    print(*arr)