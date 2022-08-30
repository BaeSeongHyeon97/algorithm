# r, c = map(int, input().split())
# N = int(input())
# row = []
# col = []
# for n in range(N):
#     a, b = map(int,input().split())
#     if a == 0:
#         row.append(b)
#     else:
#         col.append(b)
# row.sort()
# col.sort()
#
# arr = [[0] * (c * 2) for _ in range(r * 2)]     # 선까지 표현
#
# for i in row:
#     for j in range(c*2):
#         arr[i * 2][j] = 1
# for i in col:
#     for j in range(r*2):
#         arr[j][i * 2] = 1
#
# for i in range(len(arr)):
#     if i % 2:
#         print(*arr[i])
#     else:

# =======================================================
M, N = map(int,input().split())    # N * M 배열
arr = [[0] * M for _ in range(N)]
cut = int(input())      # 자르는 횟수
row = [N]
col = [M]
ans = 0
for _ in range(cut):
    a, b = map(int,input().split())
    if a == 0:
        row.append(b)
    else:
        col.append(b)
row.sort()
col.sort()

# 자르라고 한 곳을 우하단 좌표로 하고 순회... 근데 이걸 줄일방법이 있나?.,,,
for r in row:
    for c in col:
        cnt = 0
        for i in range(r):
            for j in range(c):
                if arr[i][j] != 1:
                    arr[i][j] = 1
                    cnt += 1
        if cnt > ans:
            ans = cnt
print(ans)
