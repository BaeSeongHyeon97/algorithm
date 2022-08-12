import sys; sys.stdin = open('사다리1.txt')

#  사다리 받기
for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 우 좌 상
    dr = [0, 0, -1]
    dc = [1, -1, 0]
    d = 0
    # 맨아래서 2인곳 찾기
    # 시작은 r = 99, 2가 있는 c에서
    r = 99
    c = 0
    for i in range(100):
        if ladder[r][i] == 2:
            c = i
            break

    while True:
        ladder[r][c] = '*'  # 현재위치를 *로 표기
        # 현재위치 양옆을 조사후 좌,우에 1이 있으면 그 방향으로 방향을 전환
        if 0 <= r + dr[0] < 100 and 0 <= c + dc[0] < 100 and ladder[r + dr[0]][c + dc[0]] == 1:  # 오른쪽으로 한칸 더해도 범위를 벗어나지 않고
            d = 0
        elif 0 <= r + dr[1] < 100 and 0 <= c + dc[1] < 100 and ladder[r + dr[1]][c + dc[1]] == 1:
            d = 1

        r += dr[d]          # 방향에 맞게 r 과 c에 더하기
        c += dc[d]
        if 0 <= r < 100 and 0 <= c < 100:  # 방향이동을 후 범위 안
            # 방향대로 한칸 간게 1과 만난다면 그대로 가라
            if ladder[r][c] == 1:
                continue
            else:   # 다른것들을 만나면
                r -= dr[d]
                c -= dc[d]       # 원래대로 돌아오고
                d = (d + 1) % 3  # 회전한다

        elif r < 0:
            break

        else:  # 벽을 만나 rc 0보다 작아지면 방향을 튼다
            r -= dr[d]
            c -= dc[d]
            d = (d + 1) % 3
    print(f'#{tc} {c}')

