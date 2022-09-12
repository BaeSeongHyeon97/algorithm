import sys

N = int(input())
P = [0] + list(map(int,sys.stdin.readline().split()))
D = [0] + [P[1]*N] * (N)

for i in range(1, N + 1):
    for j in range(1, i + 1):
        D[i] = min(D[i], P[j] + D[i-j])
print(D[N])