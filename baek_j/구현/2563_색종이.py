T = int(input())
arr = [[0] * 100 for _ in range(100)]  # 도화지
ans = 0
for i in range(T):
    c, r = map(int,input().split())         # 좌하단 좌표
    for i in range(r, r + 10):
        for j in range(c, c + 10):
            if arr[i][j] == 0:
                arr[i][j] = 1
                ans += 1
print(ans)