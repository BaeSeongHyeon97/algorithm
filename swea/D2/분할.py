T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int,input().split()))
    max_v = 0
    min_v = 99999
    li = []
    for i in range(1, N - 1):  # 5 => 1, 2, 3 / 6 => 1, 2, 3, 4
        for j in range(1, N - i):
            s1 = s2 = s3 = 0 
            for a in range(i):
                s1 += arr[a]
            for b in range(j):
                s2 += arr[b + i]
            for c in range(N-i-j):
                s3 += arr[c + i + j]
            li.append(abs(max(s1, s2, s3) - min(s1, s2, s3)))  # 최대 최소 차의 절대값 추가
    print(f'#{tc} {min(li)}')

# 모든 경우의수 찾아서 계산한 방법이다.