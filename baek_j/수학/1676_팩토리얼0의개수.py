# 팩토리알구하기
N = int(input())
factorial = 1
for i in range(1, N + 1):
    factorial *= i
factorial = str(factorial)
cnt = 0
for f in factorial[::-1]:
    if f == '0':
        cnt += 1
    else:
        break
print(cnt)

# 팩토리알 구해서 하는게 아니라 소인수분해 해서 2 * 5 = 10이 몇개인지 세기
# => 2의개수가 왠만하면 많기에 5가 몇번나오는지 세기

N = int(input())
cnt = 0
i = 5
while i < N:
    cnt += N // i
    i *= 5
print(cnt)