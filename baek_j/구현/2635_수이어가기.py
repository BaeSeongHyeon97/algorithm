N = int(input())
N3 = 0
max_cnt = 0
nums = []
for i in range((N//2), N + 1):
    N1 = N
    N2 = i
    cnt = 2
    while True:
        N3 = N1 - N2
        if N3 < 0:
            break
        else:
            N1 = N2
            N2 = N3
            cnt += 1
    if cnt > max_cnt:
        max_cnt = cnt
        nums.append((cnt, i))

print(nums[-1][0])
ans = [N, nums[-1][1]]
n1 = N
n2 = nums[-1][1]
while True:
    n3 = n1 - n2
    if n3 < 0:
        break
    else:
        ans.append(n3)
        n1 = n2
        n2 = n3
print(*ans)
# ====================================================
# 이진 탐색으로

