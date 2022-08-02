# 18 시간 입력받아 그대로 출력
h, m = input().split(':')
print(h, m, sep=':')
# sep='' : 앞 요소를 합치면서, ''를 이용하여 나누기

# 19 연월일 입력받고 순서 바꾸기
y, m, d = input().split('.')

print(d, m, y, sep='-')

# 20 주민번호 형태 바꾸기
num6, num7 = input().split('-')
print(num6, num7, sep='')
# print(num6+num7)

#21 단어 1개 입력받아 나누어 출력
s = input()
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

# 22 연월일 입력받아 나누어 출력
date = input()
print(date[0:2], date[2:4], date[4:6])

# 23 시분초 입력받아 분만 출력
time = input().split(':')
print(time[1])

# 24 단어 2개 입력받아 이어 붙이기
w1, w2 = input().split()
print(w1 + w2)