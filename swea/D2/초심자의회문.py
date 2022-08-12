T = int(input())

for tc in range(1, T + 1):  # 테스트케이스만큼 반복
    string = input()
    N = len(string)
    ans = 1
    for i in range(N // 2):
        if string[i] != string[N - 1 - i]:
            ans = 0
            break
    if ans == 1:
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', 0)