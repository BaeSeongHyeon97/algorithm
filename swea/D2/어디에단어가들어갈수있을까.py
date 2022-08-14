T = int(input())

for tc in range(1, T + 1):
    N, K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = 0  # 1의 개수가 K개인 것의 개수
    # 열부터 1이 연속으로 몇번 나왔는지 확인?
    for i in range(N):  # 행이 바뀔 때 마다 cnt초기화
        cnt = 0  # 1의 개수
        for j in range(N):
            if arr[i][j] == 1:  # 1인게 있으면 cnt 1 증가
                cnt += 1
                if cnt == K:  # cnt가 K가 되면 ans 1 증가
                    ans += 1
                elif cnt == K + 1:  # K보다 1이 커지면 ans 1 감소
                    ans -= 1
            else:  # 0이 나오면 cnt 0 으로
                cnt = 0

    # 행에서도 동일하게
    for i in range(N):
        cnt = 0  # 1의 개수
        for j in range(N):
            if arr[j][i] == 1:  # 1인게 있으면 cnt 1 증가
                cnt += 1
                if cnt == K:  # cnt가 K가 되면 ans 1 증가
                    ans += 1
                elif cnt == K + 1:  # K보다 1이 커지면 ans 다시 1 감소
                    ans -= 1
            else:  # 0이 나오면 cnt 0 으로
                cnt = 0

    print(f'#{tc} {ans}')

