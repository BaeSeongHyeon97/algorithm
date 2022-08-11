T = int(input())

for tc in range(1, T + 1):
    P, A, B = map(int,input().split())
    l = 1
    r = P

    cnt_A = 0
    cnt_B = 0
    winner = 0
    while r > l:
        c = int((l + r) / 2)
        if c == A:
            cnt_A += 1
            l = 1
            break
        elif c > A:  # 중앙값보다 찾는값이 작은경우
            r = c
            cnt_A += 1
        else:
            l = c
            cnt_A += 1
    l = 1
    r = P
    while r > l:
        c = int((l + r) / 2)
        if c == B:
            cnt_B += 1
            l = 1
            break
        elif c > B:  # 중앙값보다 찾는값이 작은경우
            r = c
            cnt_B += 1
        else:
            l = c
            cnt_B += 1

    if cnt_A < cnt_B:
        winner = 'A'
    elif cnt_A > cnt_B:
        winner = 'B'
    else:
        winner = 0

    print(f'#{tc} {winner}')