# 델타 없이

N = int(input())
# 이동 계획 리스트로 받기
arr = list(input().split())
r = c = 1   # 현재위치(1,1)

for i in range(len(arr)):   # arr 순회
    # 주어진 계획이 뭔지 입력 받기 만약 범위에서 벗어난다면 원래자리로
    if arr[i] == 'R':
        c += 1
        if r < 1 or c < 1 or r > N or c > N:
            c -= 1
    elif arr[i] == 'L':
        c -= 1
        if r < 1 or c < 1 or r > N or c > N:
            c += 1
    elif arr[i] == 'U':
        r -= 1
        if r < 1 or c < 1 or r > N or c > N:
            r += 1
    else:
        r += 1
        if r < 1 or c < 1 or r > N or c > N:
            r -= 1

print(r, c)

# ----------------------------------------------------------
# 델타로
N = int(input())
plans = list(input().split())
r = c = 1   # 현재위치(1,1)
# L, R, U, D / 좌 우 위 아래
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
plan_type = ['L', 'R', 'U', 'D']


for plan in plans:
    for i in range(len(plan_type)):
        if plan == plan_type[i]:
            nr = r + dr[i]
            nc = c + dc[i]
    if nr < 1 or nc < 1 or nr > N or nc > N:
        continue
    else:
        r, c = nr, nc

print(r, c)
