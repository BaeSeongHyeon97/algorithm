T = int(input())

for tc in range(1, T + 1):
    N, M = map(int,input().split())
    i = 1
    print(f'#{tc}', end=' ')
    while N * i <= M:
        print(N * i, end=' ')
        i += 1
    print()

