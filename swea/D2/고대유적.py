T = int(input())

for tc in range(1, T + 1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    max_cnt = 0

    # 행 계산 / 가로
    for i in range(N):
        cnt = 0
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1
                if cnt > max_cnt:
                    max_cnt = cnt
            else:
                cnt = 0
    # 열 계산 / 세로
    for i in range(M):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
                if cnt > max_cnt:
                    max_cnt = cnt
            else:
                cnt = 0
    print(f'#{tc} {max_cnt}')

# N * N 일때 회문만 생각함
# N * M 상황에서 열 회문하는 것