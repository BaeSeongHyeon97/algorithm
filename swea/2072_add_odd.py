# 2072. 홀수만 더하기

# 0~10000 
# 첫줄 T, 테스트 케이스
# 각테스트케이스 첫번째줄에는 10개의 수가 주어짐

# 출력 #t 공백 후 정답

T = int(input())
sum = 0

for i in range(1, T+1):
    sum = 0
    num = list(map(int,input().split()))
    for a in range(len(num)):
        num_remainder = num[a] % 2
        if num_remainder == 1:
            sum = sum + num[a]
        else:
            sum = sum
    print(f'#{i} {sum}')