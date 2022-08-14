T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    ans = []
    for i in range(N, 0, -1):
        if N % i == 0:
            ans.append(i)
    print(f'#{tc}', *ans)