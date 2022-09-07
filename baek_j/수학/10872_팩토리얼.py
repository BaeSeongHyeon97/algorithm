# 기본
N = int(input())
ans = 1
for i in range(1,N + 1):
    ans *= i
print(ans)

# 재귀
def Fatorial(N):
    if N == 1:
        return 1
    else:
        return N * Fatorial(N-1)

N = int(input())
print(Fatorial(N))
