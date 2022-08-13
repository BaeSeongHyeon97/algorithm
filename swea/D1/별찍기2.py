# print(' ') 와 print('*')를 반복해서 사용

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}')
    for i in range(1, N + 1):
        print(' ' * (N - i), end='')
        print('*' * i)