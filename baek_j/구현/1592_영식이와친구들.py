N, M, L = map(int,input().split())

visited = [0] *(N + 1)
i = 1
cnt = 0
while True:
    visited[i] += 1
    if visited[i] == M:
        break
    cnt += 1
    if visited[i] % 2:
        i += L
        if i > N:
            i -= N
    else:
        i -= L
        if i < 1:
            i += N
print(cnt)