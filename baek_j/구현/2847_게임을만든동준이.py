N = int(input())
scores = [0] * N
cnt = 0
for i in range(N):
    scores[i] = int(input())
i = 0
for i in range(N - 1, 0, -1):
    while True:
        if scores[i] <= scores[i - 1]:
            scores[i - 1] -= 1
            cnt += 1
        else:
            break

print(cnt)