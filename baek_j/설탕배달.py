# 설탕가게에 N킬로그램 배달
# 봉지는 3킬로 5킬로 
# 최대한 적은 봉지
# 봉지를 몇개 가져가야 할까


N = int(input())
cout = 0

while N != 0:
  if N % 5 == 0:
    cout = cout + N // 5
    N = N - 5 * (N // 5)
  elif N == 1 or N == 2:
      cout = -1
      break
  else:
    N = N - 3
    cout += 1


print(cout)


