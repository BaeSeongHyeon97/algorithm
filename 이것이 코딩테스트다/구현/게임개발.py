# 맵의 크기 N * M
N, M = map(int,input().split())
# 처음위치(A, B)와 바라보는 방향 d
A, B, d = map(int,input().split())
# 맵 요소 받기 / 땅인지 바다인지
arr = [list(map(int,input().split())) for _ in range(N)]
# 방향 정하기 북 동 남 서 => 이거는 시계방향 but 문제에서는 시계반대방향 요구
da = [-1, 0, 1, 0]
db = [0, 1, 0, -1]
cnt = 0  # 움직인 총 횟수
cnt_d = 0  # 방향전환 횟수
# 움직이기 시작
while cnt_d < 4:
    # 현재위치 2로 설정
    arr[A][B] = 2
    # 지금 방향에 맞게 전진
    na = A + da[d]
    nb = B + db[d]
    # 만약 범위를 벗어나거나, 바다가 있거나, 왔던 길이라면 이동을 취소하고 방향 바꾸기
    if na < 0 or na >= N or nb < 0 or nb >= M or arr[na][nb] == 1 or arr[na][nb] == 2:
        d = (d + 3) % 4  # 반시계방향으로 회전
        cnt_d += 1  # 회전횟수 + 1

    # 범위를 벗어나지 않고 방향에 0이 있으면 이동
    elif 0 <= na < N and 0 <= nb < M:
        cnt += 1
        cnt_d = 0
        # 이동
        A = na
        B = nb

# 한바퀴 돌았는데 갈곳 없다면 뒤로

while True:
    A = A + da[(d + 2) % 2]  # 바라보고 있는 방향의 뒤쪽 방향으로 이동
    if arr[A][B] != 1:  # 뒤칸이 1 이 아니라면 뒤로가기
        cnt += 1
    else:
        break

print(cnt)
