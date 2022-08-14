T = int(input())

for tc in range(1, T + 1):
    N, M = map(int,input().split())
    print(f'#{tc}')
    if M == 1:
        for i in range(1, N + 1):
            print('*' * i)

    elif M == 2:
        for i in range(N, 0, -1):
            print('*' * i)

    else:
        for i in range(N - 1, -1, -1):
            print(' ' * i + '*' * ((N - 1) - i), end='')
            print('*', end='')
            print('*' * ((N - 1) - i) + ' ' * i)