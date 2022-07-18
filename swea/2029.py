# 2029. 몫과 나머지 출력하기

'''
2개의 수(a,b) 입력받아 a를 b로 나눈 몫과 나머지
'''


T = int(input())

for t in range(1, 1+T):
    a, b = map(int,input().split())
    share = a // b
    remain = a % b

    print(f'#{t} {share} {remain}')