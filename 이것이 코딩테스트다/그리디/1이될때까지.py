# n에서 1 빼기
# or
# n 을 k로 나누기
# 1까지 가기위한 최소 횟수

n, k = map(int,input().split())
cnt = 0
while n != 1:
    if n % k == 0:
        n //= k
        cnt += 1
    else:
        n -= 1
        cnt += 1
print(cnt)

# ------------------------------