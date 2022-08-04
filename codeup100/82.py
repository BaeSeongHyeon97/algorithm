# 82 
# 369게임
n = int(input())

for i in range(1, n+1):
  if i % 10 == 3:
    print('X', end=' ')
  elif i % 10 == 6:
    print('X', end=' ')
  elif i % 10 == 9:
    print('X', end=' ')
  else:
    print(i, end=' ')

# 심화 369
n = int(input())

for i in range(1, n+1):
  count = 0
  for j in range(len(str(i))):
    if str(i)[j] == '3' or str(i)[j] == '6' or str(i)[j] == '9':
      count += 1
  if count < 1:
    print(i, end=' ')
  else:
    print('X' * count, end=' ')
