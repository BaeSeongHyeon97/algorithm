# 2070. 큰 놈, 작은 놈, 같은 놈

# 2개의 수 입력 받아 크기 비교후 부등호
# 첫줄 T

T = int(input())

for t in range(1, T+1):
    num_1 , num_2 = map(int,input().split())
    if num_1 > num_2 :
        print(f'#{t} >')
    elif num_1 == num_2 :
        print(f'#{t} =')
    else:
        print(f'#{t} <')