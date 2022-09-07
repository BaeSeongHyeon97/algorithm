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

