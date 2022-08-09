import sys; sys.stdin = open('input.txt')
# 이웃한 M개의 합을 계산해 최대 최소의 차이를 출력
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))
    val1 = 0

    for i in range(M):
        val1 = val1 + arr[i]
    max_val = val1
    min_val = val1

    for i in range(N-M+1):
        val2 = 0
        for j in range(M):
            val2 = val2 + arr[i+j]
        if val2 >= max_val:
            max_val = val2
        elif val2 <= min_val:
            min_val = val2

    print(f'#{tc} {max_val - min_val}')

#----------------------------------
# 인덱스의 시작과 끝?
# 시작인덱스 : 0 ~ N-M
# 끝 인덱스 : 시작 + M-1
# for s in range(0,N-M):
#     e = s + M - 1
# for s -> e의 합

