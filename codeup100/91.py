a, b, c = map(int,input().split())
day = 1
# 최소공배수 = 날짜를 나눴을 때 모두 나머지가 0

while True:
  if day % a == 0 and day % b == 0 and day % c == 0:
    break
  else:
    day += 1
print(day)