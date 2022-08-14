T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int,input().split())) for _ in range(9)]
    ans = 1
    # 행 검사
    for i in range(9):
        for j in range(9):
            for k in range(8, j, -1):
                if arr[i][j] == arr[i][k]:  # 같은게 있을 경우 ans = 0으로 하고 중지
                    ans = 0
                    break

    # 열 검사
    for i in range(9):
        for j in range(9):
            for k in range(8, j, -1):
                if arr[j][i] == arr[k][i]:
                    ans = 0
                    break

    # 3 * 3 검사
    # 3 행 3 열 따로 검사?
    for i in range(0,9,3):      # 0 3 6
        li = []
        for j in range(3):      # 0 1 2
            for k in range(3):  # 0 1 2
                li.append(arr[j+i][k+i])
        for l in range(9):
            for m in range(8, l, -1):
                if li[l] == li[m]:
                    ans = 0
                    break

    print(f'#{tc} {ans}')

# 스도쿠 합으로 한 이유 수민이형한테 물어보기
# 합으로 해도 되는건가 안되는게 있지 않을까
# 세개를 다 하는거니까 상관이 없으려나
# 흠...
