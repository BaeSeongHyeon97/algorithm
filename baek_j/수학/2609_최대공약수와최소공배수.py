num1, num2 = map(int,input().split())

orig1, orig2 = num1, num2
# 최대공약수
# 약수중 가장 큰 수
# 유클리드 호제법 : 두 수가 나누어 떨어지지 않으면
# 두 수의 최대공약수는 큰수에서 작은수를 나눈 나머지와 작은수와의 최대 공약수와 같다.
ans1 = 0
while True:
    if num1 >= num2:
        a = num1 % num2
        if a:
            num1 = num2
            num2 = a
        else:
            ans1 = num2  # num2가 최대공약수
            break
    else:
        b = num2 % num1
        if b:
            num2 = num1
            num1 = b
        else:
            ans1 = num1
            break
print(ans1)
# 최소공배수
# 최대공약수로 나눈 몫들의 곱과 최대공약수의 곱
# 최소공배수 = 두 자연수의 곱 / 최대공약수
ans2 = ans1 * (orig1 // ans1) * (orig2 // ans1)
print(ans2)
