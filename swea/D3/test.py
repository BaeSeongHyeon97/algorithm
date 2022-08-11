T = int(input())

for tc in range(1, 2):
    # 사다리 받기
    ladder = [list(map(int,input().split())) for _ in range(8)]
    origin = ladder  # 기존 사다리 저장해 놓기
    # 우 좌 하
    dr = [0, 0, 1]
    dc = [1, -1, 0]
    direction = 0
    # 맨위에 행부터 시작하기 위해 포문
    for i in range(1):
        r = 0
        c = i
        # 첫번째 칸이 0이면 다음껄로 continue
        if ladder[r][c] == 0:
            continue
        # 첫번째 칸이 1 이라면
        else:
            while True:
                ladder[r][c] = '*'  # 현재위치를 0으로 바꾸기
                r += dr[direction]  # 델타대로 합하기
                c += dc[direction]
                # 만약 행또는 열값이 0보다 작거나 범위보다 커지면
                # 원래값으로 줄이고 방향 바꿔서 진행
                if r < 0 or c < 0 or ladder[r][c] == 0 or ladder[r][c] == '*':
                    r -= dr[direction]
                    c -= dc[direction]
                    direction = (direction + 1) % 3
                for j in range(3):
                    r += dr[j]
                    c += dc[j]
                    if ladder[r][c] == 1:
                        direction = 0
                if r >= 8 or c >= 8:
                    break
    print(ladder)

# 1 0 0 1 0 0 0 0
# 1 0 0 1 0 0 0 0
# 1 0 0 1 1 1 1 1
# 1 0 0 1 0 0 0 0
# 1 0 0 1 0 0 0 0
# 1 1 1 1 0 0 0 0
# 1 0 0 1 0 0 0 0
# 1 0 0 1 0 0 0 0
