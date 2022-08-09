# 가장 큰 수와 가장 작은 수의 차이를 출력하시오

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int,input().split()))
    max_val = arr[0]
    min_val = arr[0]
    for n in range(N):
        if arr[n] > max_val:
            max_val = arr[n]
        elif arr[n] < min_val:
            min_val = arr[n]
    print(f'#{tc} {max_val - min_val}')

# 최대값/ 최소
# 리스트에 값 저장보다 그때그때 값 비교해서 갱신

