# 2058. 자릿수 더하기

# for 문
num = int(input())
sum = 0

for i in range(1, 5) :
    sum = sum + num % 10
    num = num // 10

print(sum)


# while 문

num = int(input())
sum = 0

while num != 0 :
    sum = sum + num % 10
    num = num // 10

print(sum)