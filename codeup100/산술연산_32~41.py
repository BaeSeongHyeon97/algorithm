# 32 정수 1개 입력받아 부호바꾸기
n = int(input())
print(-n)

# 33 문자 1개 입력받아 다음 문자 출력
a = input()
n = ord(a)
print(chr(n+1))

# 34 정수 2개 입력받아 차 계산
a, b = map(int,input().split())

print(a - b)

# 35 실수 2개 입력받아 곱 계산
a, b = map(float,input().split())

print(a * b)

# 36 단어 여러번 출력
w, n = input().split()
print(w * int(n))

# 37 문장 여러 번 출력하기
n = int(input())
s = input()

print(n * s)

# 38 정수 2개 입력받아 거듭제곱 계산
a, b = map(int,input().split())
print(a**b)

# 39 실수 2개 입력받아 거듭제곱 계산
a, b = map(float,input().split())
print(a**b)

# 40 정수 2개 입력받아 나눈 몫 계산
a, b = map(int,input().split())
print(a//b)

# 41 정수 2개 나머지 계산 
a, b = map(int,input().split())
print(a%b)