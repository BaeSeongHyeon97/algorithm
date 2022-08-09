import sys; sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    n, q = map(int,input().split())
    arr = [0] * n
    for i in range(1, q + 1):
        l, r = map(int,input().split())
        for j in range(l, r + 1):
            arr[j-1] = i
    print(f'#{tc}', *arr)

