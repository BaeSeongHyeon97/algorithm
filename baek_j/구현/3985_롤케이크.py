L = int(input())
N = int(input())
cake = [0] * (L + 1)  # 0번 건너 뛰게?
cnt = 1
max_cnt = 0
max_expect = 0
max_real = 0
for n in range(1, N + 1):
    p, k = map(int,input().split())
    if (k - p + 1) > max_expect:
        max_expect = (k - p + 1)
        max_expect_idx = n

    for i in range(p, k + 1):
        if cake[i] == 0:
            cake[i] = n  # 먼저 쓴사람 입력 - 채워져있으면 안씀

for i in range(1, L):
    if cake[i] == 0:
        cnt = 1
        continue
    elif cake[i] == cake[i + 1]:
        cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt
            max_real = cake[i]

    else:
        if max_cnt < cnt:
            max_cnt = cnt
            max_real = cake[i]
        cnt = 1

print(max_expect_idx)
print(max_real)

# 50퍼에서 틀림 다시해보기