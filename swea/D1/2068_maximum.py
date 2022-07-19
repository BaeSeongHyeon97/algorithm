# 2068. 최대수 구하기

# 10개 수 입력받아 큰수 출력
# 첫줄 T

T = int(input())

for t in range(1, T+1):
    num = list(map(int,input().split()))
    max = 0
    num.sort()
    max = num[-1]
    print(f'#{t} {max}')
