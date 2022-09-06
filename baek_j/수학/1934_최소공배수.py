# 유클리드 호제법
# 나누어 떨어지지 않는 두 수의 최대공약수는 두 수의 나머지와 작은수의 최대공약수와 동일하다.
# 최소공배수 = 두 자연수의 곱 / 최대공약수

N = int(input())
for i in range(N):
    num1, num2 = map(int,input().split())
    n1, n2 = num1, num2
    ans1 = 0  # 최대공약수
    while True:
        if n1 >= n2:
            a = n1 % n2
            if a:
                n1 = n2
                n2 = a
            else:
                ans1 = n2
                break
        else:
            b = n2 % n1
            if b:
                n2 = n1
                n1 = b
            else:
                ans1 = n1
                break
    print(num1 * num2 // ans1)

