# 1545. 거꾸로 출력해 보아요
# 주어진 숫자부터 0까지 순서대로

N = int(input())

N_li = list(range(0 , N+1))

for i in range(1,N + 2):
    print(N_li[-i], end=' ')

# print(*N_li[::-1]) 도 가능