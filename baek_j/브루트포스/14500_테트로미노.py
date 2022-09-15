R, C = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

# 0000 가로
max_v = 0
for r in range(R):
    for c in range(C-3):
        cnt = 0
        for i in range(c,c+4):
            cnt += arr[r][i]
        if cnt > max_v:
            max_v = cnt
# 0000세로


# 000