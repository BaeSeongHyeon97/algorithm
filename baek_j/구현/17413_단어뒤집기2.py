string = list(input())
N = len(string)
S = [''] * N
top = -1
ans = []
i = 0
while i < N:
    if string[i] == '<':
        while top > -1:
            ans.append(S[top])
            top -= 1
        end = 0
        for j in range(i + 1, N):
            if string[j] == '>':
                end = j
                break
        for l in range(i, end + 1):
            ans.append(string[l])
        i = end + 1

    elif string[i] == ' ':
        while top > -1:
            ans.append(S[top])
            top -= 1
        ans.append(string[i])
        i += 1
    else:
        top += 1
        S[top] = string[i]
        i += 1

while top > -1:
        ans.append(S[top])
        top -= 1

for i in ans:
    print(i, end='')