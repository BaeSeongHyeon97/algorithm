email = input()
N = len(email)
li = []
for i in range(1, N + 1):
    if N % i == 0:
        li.append(i)
for i in range(len(li)):
    for j in range(i, len(li)):
        if li[i] * li[j] == N:
            R = li[i]
C = N // R
arr = [[''] * C for _ in range(R)]
i = 0
while i < N:
    for c in range(N // R):
        for r in range(R):
            arr[r][c] = email[i]
            i += 1

for r in range(R):
    for c in range(C):
        print(arr[r][c], end='')
