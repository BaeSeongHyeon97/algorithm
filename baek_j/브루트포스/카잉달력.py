# 최대공약수
def f(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


T = int(input())
for tc in range(T):
    N, M, x, y = map(int, input().split())
    for i in range(100000):
        if (((i * N)+x) % M) == y:
            print(((i * N)+x))
            break
    else:
        print(-1)

    # x가 나올 수 있는 수 구해 놓고 y가 나올수 있는 수 구하기
    # li_x = []
    # for i in range(1, 999999):
    #     if (i % N) == x:
    #         li_x.append(i)
    # for i in range(1, 999999):
    #     if (i % M) == y and i in li_x:
    #         print(i)
    #         break
    # else:
    #     print(-1)
    # 불가

