N = int(input())
li = []
max_r = 0
max_c = 0
for _ in range(N):
    r, c = map(int,input().split())
    li.append((r, c))
    if r > max_r:
        max_r = r
    if c > max_c:
        max_c = c
arr = [[0] * (max_c) for _ in range(max_r + 1)]
for i in li:
    a, b = i
    for j in range(b):
        arr[a][j] = 1
for i in arr:
    print(*i)
li.sort()
print(li)
max_h = 0
# for i in range(max_r + 1):
#     for j in range(max_c + 1):
