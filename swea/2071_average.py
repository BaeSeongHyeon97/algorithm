# 2071. 평균값 구하기

# 10개의 수 입력받음
# 첫줄 T = 테스트 케이스
# 소숫점 첫째자리 반올림

T = int(input())


for t in range(1, T+1):
    num = list(map(int,input().split()))
    sum = 0 
    for i in range(len(num)):
        sum = sum + num[i]
        i = i + 1
        average = sum / len(num)
        average_round = round(average)
    print(f'#{t} {average_round}')