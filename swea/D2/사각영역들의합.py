T = int(input())

for tc in range(1, T + 1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    sum_v = 0
    for _ in range(M):
        r, c, m = map(int,input().split())
        # 주어진 영역의 합 구하기
        for i in range(m):
            for j in range(m):
                if 0 <= r + i < N and 0 <= c + j < N:
                    sum_v += arr[r + i][c + j]
                    arr[r + i][c + j] = 0  # 겹치는 부분 빼줘야함 => 한번 구한 부분은 0으로 바꾸기

    print(f'#{tc} {sum_v}')

# 겹쳐서 더해지는 부분 빼기 위해 더한부분은 0으로 바꾸기
# 영역 요소의 합 구하기 다시보기

