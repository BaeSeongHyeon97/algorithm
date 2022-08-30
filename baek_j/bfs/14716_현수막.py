def bfs(r,c):
    Q = []
    Q.append((r,c))
    visited[r][c] = 1

    while Q:
        x, y = Q.pop(0)

        for i in range(8):
            nr = x + dr[i]
            nc = y + dc[i]
            # 범위 안에서 방문하지 않은 곳중에서 1인곳
            if 0<= nr < M and 0<= nc < N and arr[nr][nc] == 1 and visited[nr][nc] == 0:
                visited[nr][nc] = 1     # 방문표시
                Q.append((nr, nc))      # 큐에 추가
    return 1


# 상 하 좌 우 \우하 /좌하 우상 좌상
dr = [-1, 1, 0, 0, 1, 1, -1, -1]
dc = [0, 0, -1, 1, 1, -1, 1, -1]
M, N = map(int,input().split())   # M이 열, N이 행
arr = [list(map(int, input().split())) for _ in range(M)]
visited = [[0] * N for _ in range(M)]
ans = 0

for r in range(M):
    for c in range(N):
        if arr[r][c] == 1 and visited[r][c] == 0:
            ans += bfs(r,c)
print(ans)