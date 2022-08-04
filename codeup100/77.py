# 77 정수 입력받아 1부터 그 수 까지 짝수의 합
n = int(input())
total = 0
for i in range(1, n+1):
  if i % 2 == 0:
    total += i

print(total)

# while
n = int(input())
total = 0
while n != 0:
  if n % 2 == 0:
    total += n
  n = n - 1

print(total)
