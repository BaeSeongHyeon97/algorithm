# 2019. 더블더블
# 주어진 횟수까지 2의 제곱 값들을 출력
# 주어질 숫자는 30을 넘지 않음

N = int(input())

for n in range(N + 1):
    print(2**n, end = ' ')

