from collections import deque

def bfs(r, c):
    val = arr[r][c]
    cnt = 0
    # 큐생성
    Q = []
    # 첫좌표 큐에 넣고, 방문표시하기
    Q.append((r,c))
    visited[r][c] = 1
    while Q:
        x, y = Q.pop(0)
        
        # 인접정점 => 네방향 돌아보기
        for i in range(4):
            nr = x + dr[i]
            nc = y + dc[i]
            # 범위 안이고, 같은 색깔이고, 방문하지 않은 곳이라면 인접정점으로 추가
            if 0<=nr<M and 0<=nc<N and arr[nr][nc] == val and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                Q.append((nr,nc))
                cnt += 1    # 인접한 색깔의 개수
    return cnt + 1

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
N, M = map(int, input().split())  # 행 : M, 열 : N
arr = [list(input()) for _ in range(M)]
visited = [[0] * N for _ in range(M)]
cnt = 0

# 아군, 적군
power1, power2 = 0, 0

# 전체를 돌면서 방문하지 않았고 + w와 b일때 각각 구하기
for r in range(M):
    for c in range(N):
        if arr[r][c] == 'W' and visited[r][c] == 0:
            power1 += bfs(r, c) ** 2
        elif arr[r][c] == 'B' and visited[r][c] == 0:
            power2 += bfs(r, c) ** 2
print(power1, power2)