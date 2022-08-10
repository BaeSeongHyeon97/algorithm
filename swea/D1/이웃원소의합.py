# 인접 두원소의 합이 최대인 경우

# 배열 받아서
# s = 0
# for i : 1 -> N-1
#     s = arr[i] + arr[i - 1]
#     if

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    nums = list(map(int,input().split()))
    s = 0
    max_s = 0
    for i in range(1, n):
        s = nums[i] + nums[i - 1]
        if s > max_s:
            max_s = s

    print(f'#{tc} {max_s}')

