N = int(input())
nums = list(map(int,input().split()))
ans = 0
for i in nums:
    cnt = 0
    if i == 1:
        continue
    elif i % 2 == 0 and i > 2:
        continue
    else:
        for j in range(1,i + 1):
            if i % j == 0:
                cnt += 1
                if cnt > 2:
                    break
        else:
            if cnt == 2:
                ans += 1
print(ans)

# ====================================================
# 에라토스테네스의 채
arr = [i for i in range(1001)]
ans = []  # 소수
for a in arr:
    if a == 0 or a == 1:
        continue
    else:
        ans.append(a)
        for i in range(2*a, 1001, a):
            arr[i] = 0
N = int(input())
nums = list(map(int,input().split()))
cnt = 0
for n in nums:
    if n in ans:
        cnt += 1
print(cnt)
