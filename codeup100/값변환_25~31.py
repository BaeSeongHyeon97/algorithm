# 25 정수 2개 입력받아 합 계산
n1, n2 = map(int,input().split())
print(n1 + n2)

# 26 실수 2개 입력받아 합
n1 = float(input())
n2 = float(input())
print(n1 + n2)

# 27 16진수 출력 1
n = int(input())
print('%x'%n)

# 28 16진수 출력 2
n = int(input())
print('%X'%n)

# 29 16진수 8진수로
a = input()
n = int(a, 16)
print('%o'%n)

# 31 영문자 1개 10진수로 # ord() : 문자를 숫자로
n = ord(input())
print(n)

# 32 10진수를 영문자로 # chr() : 숫자를 문자로
n = int(input())
print(chr(n))
