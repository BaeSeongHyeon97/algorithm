# 09: 37 시작 / 09:56 끝
# 다양한 수로 이루어진 배열을 주어진 수를 M번 더하여 가장 큰 수를 만드는 법칙
# 특정 수 연속해서 K번 이상 더해질 수 없음

# 숫자 리스트에서 가장 큰 수 K번 더하고 그다음 한번 더하고 다시 큰수 k번
# max를 쓰면 편하겠지만, 정렬 후 하기

n, m, k = map(int,input().split())
nums = list(map(int,input().split()))

버블 정렬 / sort대신
for i in range(n-1, -1, -1):
    for j in range(i):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

first = nums[-1]
second = nums[-2]
total = 0
while True:
    if m > k:
        total += (first * k) + second
        m -= (k + 1)
    else:
       total += (m * first)
       break
# print(total)

#--------------------------
# 위 방식은 N이 커지면 시간초과가 나타난다.
# 반복되는 수열 판단

n, m, k = map(int,input().split())
nums = list(map(int,input().split()))

for i in range(n-1, -1, -1):
    for j in range(i):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

first = nums[n-1]
second = nums[n-2]

# k번 가장 큰값 + 1번 second값의 순열
# 가장큰값이 더해지는 횟수 구하기

cnt = (m // (k+1) * k) + (m % (k + 1))

total = cnt * first + (m - cnt) * second
print(total)

