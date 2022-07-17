# 간단한 압축풀기

T = int(input())
orig = ''

for t in range(1, T+1):
    N = int(input())
    for n in range(N):
        Ci, Ki = input().split()
        orig = orig + Ci * int(Ki)
    length = 0    
    print(f'#{T}')
    for i in range(len(orig)):
        print(orig[i], end='')
        length += 1
        if length == 10:
            length = 0
            print()