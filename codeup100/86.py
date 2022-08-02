n = int(input())
total = 0
s = 1
while True:
  total += s
  s += 1
  if total >= n:
    break
print(total)
