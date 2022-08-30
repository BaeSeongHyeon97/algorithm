N = int(input())
ans = []
height = 0
arr = list(map(int, input().split()))
s = arr[0]
for i in range(1, N):
    if arr[i] > s:
        height = height + arr[i] - s
        s = arr[i]
    elif arr[i] <= s:
        ans.append(height)
        s = arr[i]
        height = 0
else:
    ans.append(height)
print(max(ans))