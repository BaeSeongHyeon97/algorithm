# 42 실수 1개 입력받아 소숫점 이하자리 변환
# n = float(input())
# print(round(n, 2)) # format(수, ".2f") # f'{변수 : .2f}'

# 43 실수 2개 입력받아 나눈 결과 계산
f1, f2 = map(float,input().split())
print(format(f1/f2, ".3f"))

# 44 정수 2개 입력받아 자동 계산
a, b = map(int,input().split())

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(format(a / b, ".2f"))

# 45 정수 3개 입력받아 합과 평균 출력
a, b, c = map(int,input().split())
total = a + b + c
print(total, format(total / 3, ".2f"))

# 46 정수 1개 2배 곱해 출력하기
# 비트단위 시프트 연산자 : << 1 => 2배 / >> 1 => 1/2배
n = int(input())
print(n<<1)

# 47 2의 거듭제곱 배로 곱해 출력하기
# a << b => a의 b승
a, b = map(int,input().split())
print(a << b)

# 48 정수 2개 입력받아 비교하기1
a, b = map(int,input().split())
print(a < b)

# 49 정수 2개 입력받아 비교하기2
a, b = map(int,input().split())
print(a == b)

# 50
a, b = map(int,input().split())
print(a <= b)

# 51
a, b = map(int,input().split())
print(a != b)