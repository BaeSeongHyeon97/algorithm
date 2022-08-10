for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    max_val = 0

    # 행
    for i in range(100):
        s1 = 0
        for j in range(100):
            s1 += arr[i][j]
        if s1 > max_val:
            max_val = s1
    # 열
    for i in range(100):
        s2 = 0
        for j in range(100):
            s2 += arr[j][i]
        if s2 > max_val:
            max_val = s2
    s3 = 0
    for i in range(100):
        s3 += arr[i][i]
    if s3 > max_val:
        max_val = s3
    # / 대각선
    s4 = 0
    for i in range(100):
        s4 += arr[i][99 - i]
        if s4 > max_val:
            max_val = s4

    print(f'#{tc} {max_val}')
