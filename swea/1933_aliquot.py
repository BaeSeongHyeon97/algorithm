# 1933. 간단한 N의 약수

N = int(input())


for n in range(1, N + 1):
    remain = N % n
    if remain == 0 :
        print(n, end=' ')
    n += 1

