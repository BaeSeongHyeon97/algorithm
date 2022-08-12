# for 문으로 print('*') 반복

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}')
    for i in range(1, N + 1):
        print('*' * i)

