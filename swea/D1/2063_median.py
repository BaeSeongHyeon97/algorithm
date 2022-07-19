# 2063. 중앙값 찾기

N = int(input())
score = list(map(int,input().split()))

score.sort()

median = score[(N-1) // 2]

print(median)

# 7.17 나눗셈할때 (/) 쓰지말고 몫(//) / 나머지(%) 명확하게