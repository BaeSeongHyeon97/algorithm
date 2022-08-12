import sys; sys.stdin = open('input.txt')

# append 쓰고
T = int(input())
for _ in range(T):
    tc, n = input().split()
    strings = list(input().split())
    nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    ans = []

    # 0 ~ 9 까지의 숫자열 생성해서 문자열 하나씩 비교해서
    # 같을때 append
    for i in range(len(nums)):
        for j in range(int(n)):
            if nums[i] == strings[j]:
                ans.append(strings[j])

    print(f'{tc}')
    print(*ans)

# ------------------------------------------------------------------------
# append 안쓰고
T = int(input())
for _ in range(T):
    tc, n = input().split()
    strings = list(input().split())
    nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    cnt = 0

    # append 안쓰고?
    for i in range(len(nums)):
        for j in range(int(n)):
            if nums[i] == strings[j]:
                strings[j], strings[cnt] = strings[cnt], strings[j]
                cnt += 1

    print(f'{tc}')
    print(*strings)
# ----------------------------------------------------------------------------





